import numpy as np

from kernel.block import Block

from config import (
    tau_r,
    sigma_eq,
    x_g
)


class LangevinPlant(Block):

    def __init__(
        self,
        period,
        rng
    ):

        super().__init__(
            name="Plant",
            period=period,
            priority=10
        )

        self.rng = rng

        self.x = -x_g

    def update(
        self,
        t,
        bus
    ):

        lambda_actual = bus.read(
            "actuator_state",
            0.0
        )

        a = np.exp(
            -self.period
            / tau_r
        )

        Q = (
            sigma_eq**2
            * (1.0 - a**2)
        )

        noise = (
            np.sqrt(Q)
            * self.rng.normal()
        )

        self.x = (
            a * self.x
            +
            (1.0 - a)
            * (
                lambda_actual
                - x_g
            )
            +
            noise
        )

        bus.publish(
            "plant_state",
            self.x,
            t
        )