from kernel.block import Block


class MeasurementBlock(Block):

    def __init__(
        self,
        period,
        rng,
        sigma_m
    ):

        super().__init__(
            name="Measurement",
            period=period,
            priority=20
        )

        self.rng = rng
        self.sigma_m = sigma_m

    def update(
        self,
        t,
        bus
    ):

        x = bus.read(
            "plant_state"
        )

        if x is None:
            return

        y = (
            x
            +
            self.sigma_m
            * self.rng.normal()
        )

        bus.publish(
            "measurement",
            y,
            t
        )