"""
Q-SYNTH actuator model.

Implements a delayed optical-tweezer actuator.

INPUTS
------
control_command:
    Event-like requested trap position lambda_cmd.
    A new entry is produced only when the controller
    generates a ratchet command.

plant_state:
    Current bead position x.

OUTPUTS
-------
actuator_state:
    Current physically applied trap position lambda_actual.

trap_move:
    Event produced only when the physical trap position
    actually changes.

actuator_command_event:
    Records each accepted controller command together with
    command and scheduled application timestamps.

ATTRIBUTES / STATE
------------------
lambda_actual:
    Current applied trap position.

command_queue:
    Pending actuator commands.

last_command_time:
    Timestamp of the last controller command already
    accepted into the actuator queue.

PARAMETERS
----------
period:
    Actuator execution period.

delay:
    Command-to-physical-application latency.

FUNCTION
--------
At every actuator update:

1. Check whether the controller produced a new command.
2. Add new commands to the delayed queue.
3. Find commands whose application time has arrived.
4. Apply matured commands in chronological order.
5. Compute trap work for physical moves.
6. Publish actuator state.

For an instantaneous shift of a harmonic trap:

    W_trap =
        0.5*kappa*(x-lambda_new)^2
        -
        0.5*kappa*(x-lambda_old)^2

Positive W_trap:
    work supplied by trap actuation.

Negative W_trap:
    energy returned during trap actuation.
"""


from kernel.block import Block
from config import physical


class Actuator(Block):

    def __init__(
        self,
        period,
        delay
    ):

        super().__init__(
            name="Actuator",
            period=period,
            priority=50
        )

        self.delay = delay

        # Current physically applied trap position
        self.lambda_actual = 0.0

        # Pending commands
        #
        # Each entry is:
        #
        # {
        #     "command_time": ...,
        #     "apply_time": ...,
        #     "lambda_command": ...
        # }
        self.command_queue = []

        # Used to ensure each controller command
        # is inserted into the actuator queue only once.
        self.last_command_time = None


    def update(
        self,
        t,
        bus
    ):

        # ====================================================
        # 1. CHECK FOR A NEW CONTROLLER COMMAND
        # ====================================================

        command_history = bus.history.get(
            "control_command",
            []
        )

        if command_history:

            command_time, command = (
                command_history[-1]
            )

            is_new_command = (
                self.last_command_time is None
                or
                command_time > self.last_command_time
            )

            if is_new_command:

                apply_time = (
                    command_time
                    + self.delay
                )

                command_event = {

                    "command_time":
                        command_time,

                    "apply_time":
                        apply_time,

                    "lambda_command":
                        command
                }

                self.command_queue.append(
                    command_event
                )

                self.last_command_time = (
                    command_time
                )

                # Optional diagnostic/history event
                bus.publish(
                    "actuator_command_event",
                    command_event,
                    command_time
                )


        # ====================================================
        # 2. FIND COMMANDS WHOSE DELAY HAS EXPIRED
        # ====================================================

        matured = [

            item
            for item in self.command_queue

            if item["apply_time"] <= t
        ]


        # Explicit chronological ordering.
        #
        # For fixed delay this is normally already true,
        # but sorting makes the model robust against later
        # introduction of variable delay or timing jitter.
        matured.sort(
            key=lambda item:
                item["apply_time"]
        )


        # ====================================================
        # 3. APPLY MATURED COMMANDS
        # ====================================================

        for item in matured:

            lambda_old = (
                self.lambda_actual
            )

            lambda_new = (
                item["lambda_command"]
            )

            command_time = (
                item["command_time"]
            )

            apply_time = (
                item["apply_time"]
            )


            # ------------------------------------------------
            # Register only actual physical trap changes
            # ------------------------------------------------

            if lambda_new != lambda_old:

                x = bus.read(
                    "plant_state"
                )

                if x is not None:

                    # Harmonic potential before move
                    U_before = (
                        0.5
                        * physical.kappa
                        * (
                            x
                            - lambda_old
                        )**2
                    )

                    # Harmonic potential after move
                    U_after = (
                        0.5
                        * physical.kappa
                        * (
                            x
                            - lambda_new
                        )**2
                    )

                    trap_work = (
                        U_after
                        - U_before
                    )


                    trap_move = {

                        "command_time":
                            command_time,

                        "apply_time":
                            apply_time,

                        "latency":
                            apply_time
                            - command_time,

                        "lambda_old":
                            lambda_old,

                        "lambda_new":
                            lambda_new,

                        "delta_lambda":
                            lambda_new
                            - lambda_old,

                        "bead_position":
                            x,

                        "trap_work":
                            trap_work
                    }


                    bus.publish(
                        "trap_move",
                        trap_move,
                        apply_time
                    )


                # Physical actuator state changes here
                self.lambda_actual = (
                    lambda_new
                )


        # ====================================================
        # 4. REMOVE APPLIED COMMANDS FROM QUEUE
        # ====================================================

        self.command_queue = [

            item
            for item in self.command_queue

            if item["apply_time"] > t
        ]


        # ====================================================
        # 5. PUBLISH CURRENT PHYSICAL ACTUATOR STATE
        # ====================================================

        bus.publish(
            "actuator_state",
            self.lambda_actual,
            t
        )