from kernel.block import Block


class RatchetController(Block):

    def __init__(
        self,
        period,
        alpha,
        XT
    ):

        super().__init__(
            name="Controller",
            period=period,
            priority=40
        )

        self.alpha = alpha
        self.XT = XT

    def set_parameters(
        self,
        alpha,
        XT
    ):

        self.alpha = alpha
        self.XT = XT

    def update(
        self,
        t,
        bus
    ):

        xhat = bus.read(
            "estimate"
        )

        lambda_actual = bus.read(
            "actuator_state",
            0.0
        )

        if xhat is None:
            return

        relative_position = (
            xhat
            - lambda_actual
        )

        trigger = (
            relative_position
            > self.XT
        )

        # Always publish diagnostic/controller state
        bus.publish(
            "relative_position",
            relative_position,
            t
        )

        bus.publish(
            "ratchet_event",
            trigger,
            t
        )

        if trigger:

            lambda_cmd = (
                lambda_actual
                +
                self.alpha
                * relative_position
            )

            # Only a true ratchet event generates
            # an actuator command event.
            bus.publish(
                "control_command",
                lambda_cmd,
                t
            )