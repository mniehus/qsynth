import numpy as np

from kernel.block import Block

from config import (
    tau_r,
    x_g,
    sigma_eq
)


class KalmanEstimator(Block):

    def __init__(
        self,
        period,
        Q,
        R
    ):

        super().__init__(
            name="Estimator",
            period=period,
            priority=30
        )

        self.Q = Q
        self.R = R

        self.xhat = -x_g
        self.P = sigma_eq**2

        self.K = 0.0
        self.innovation = 0.0

    def set_parameters(
        self,
        Q,
        R
    ):

        self.Q = Q
        self.R = R

    def update(
        self,
        t,
        bus
    ):

        y = bus.read(
            "measurement"
        )

        if y is None:
            return

        lambda_actual = bus.read(
            "actuator_state",
            0.0
        )

        a = np.exp(
            -self.period
            / tau_r
        )

        x_pred = (
            a * self.xhat
            +
            (1.0 - a)
            * (
                lambda_actual
                - x_g
            )
        )

        P_pred = (
            a**2
            * self.P
            +
            self.Q
        )

        self.innovation = (
            y
            - x_pred
        )

        self.K = (
            P_pred
            /
            (
                P_pred
                + self.R
            )
        )

        self.xhat = (
            x_pred
            +
            self.K
            * self.innovation
        )

        self.P = (
            (1.0 - self.K)
            * P_pred
        )

        bus.publish(
            "estimate",
            self.xhat,
            t
        )

        bus.publish(
            "covariance",
            self.P,
            t
        )

        bus.publish(
            "innovation",
            self.innovation,
            t
        )