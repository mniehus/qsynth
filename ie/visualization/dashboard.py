from kernel.block import Block

class Dashboard(Block):

    def __init__(
        self,
        period=10e-3
    ):

        super().__init__(
            name="Dashboard",
            period=period,
            priority=100
        )

    def update(
        self,
        t,
        bus
    ):

        # read latest:
        #
        # plant_state
        # measurement
        # estimate
        # actuator_state
        # ratchet_event
        # statistics
        #
        # update matplotlib artists
        pass