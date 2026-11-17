import numpy as np

from kernel.block import Block


class StatisticsBlock(Block):
    """
    Slow statistical regime characterization.

    INPUTS
    ------
    relative_position:
        Estimated bead displacement relative to trap center

            z_n = xhat_n - lambda_n

    innovation:
        Kalman innovation

            nu_n = y_n - xhat[n|n-1]

    ratchet_event:
        Boolean controller trigger history.

    OUTPUT
    ------
    statistics:
        Dictionary containing slow regime descriptors.

    PARAMETERS
    ----------
    period:
        Execution period of the statistics block.

    controller_period:
        Fast controller sampling period.

    window:
        Duration of the moving statistical window.

    FUNCTION
    --------
    Characterizes the fluctuation dynamics relative to the
    current trap position rather than using absolute bead
    position, which contains the intentional ratchet drift.
    """

    def __init__(
        self,
        period,
        controller_period,
        window=0.1
    ):

        super().__init__(
            name="Statistics",
            period=period,
            priority=60
        )

        self.window = window
        self.controller_period = controller_period


    @staticmethod
    def _extract_recent(
        entries,
        t,
        window
    ):
        """
        Extract values from the interval:

            t-window <= time <= t
        """

        return np.array(
            [
                value
                for time, value in entries
                if time >= t - window
            ],
            dtype=float
        )


    def update(
        self,
        t,
        bus
    ):

        # ====================================================
        # 1. RELATIVE POSITION
        # ====================================================

        relative_position = self._extract_recent(
            bus.history.get(
                "relative_position",
                []
            ),
            t,
            self.window
        )


        # ====================================================
        # 2. KALMAN INNOVATION
        # ====================================================

        innovations = self._extract_recent(
            bus.history.get(
                "innovation",
                []
            ),
            t,
            self.window
        )


        # ====================================================
        # 3. RATCHET EVENTS
        # ====================================================

        events = self._extract_recent(
            bus.history.get(
                "ratchet_event",
                []
            ),
            t,
            self.window
        )


        # Need sufficient samples for meaningful statistics
        if len(relative_position) < 10:
            return


        # ====================================================
        # 4. BASIC FLUCTUATION STATISTICS
        # ====================================================

        mean = np.mean(
            relative_position
        )

        std = np.std(
            relative_position
        )


        # ----------------------------------------------------
        # Normalized central moments
        # ----------------------------------------------------

        if std > 0:

            z = (
                relative_position
                - mean
            ) / std

            skewness = np.mean(
                z**3
            )

            excess_kurtosis = (
                np.mean(
                    z**4
                )
                - 3.0
            )

        else:

            skewness = 0.0
            excess_kurtosis = 0.0


        # ====================================================
        # 5. LAG-1 AUTOCORRELATION
        # ====================================================

        if len(relative_position) > 2:

            rho1 = np.corrcoef(
                relative_position[:-1],
                relative_position[1:]
            )[0, 1]

        else:

            rho1 = np.nan


        # ====================================================
        # 6. INNOVATION STATISTICS
        # ====================================================

        if len(innovations):

            innovation_mean = np.mean(
                innovations
            )

            innovation_rms = np.sqrt(
                np.mean(
                    innovations**2
                )
            )

        else:

            innovation_mean = np.nan
            innovation_rms = np.nan


        # ====================================================
        # 7. RATCHET EVENT RATE
        # ====================================================

        if len(events):

            ratchet_count = np.sum(
                events.astype(bool)
            )

            window_duration = (
                len(events)
                * self.controller_period
            )

            if window_duration > 0:

                event_rate = (
                    ratchet_count
                    / window_duration
                )

            else:

                event_rate = np.nan

        else:

            ratchet_count = 0
            event_rate = np.nan


        # ====================================================
        # 8. PUBLISH REGIME DESCRIPTOR
        # ====================================================

        statistics = {

            # Relative coordinate statistics
            "relative_mean":
                mean,

            "relative_std":
                std,

            "relative_skewness":
                skewness,

            "relative_excess_kurtosis":
                excess_kurtosis,

            "relative_rho1":
                rho1,


            # Kalman innovation statistics
            "innovation_mean":
                innovation_mean,

            "innovation_rms":
                innovation_rms,


            # Ratchet statistics
            "ratchet_count_window":
                int(ratchet_count),

            "ratchet_rate":
                event_rate,


            # Metadata
            "window":
                self.window,

            "sample_count":
                len(relative_position)
        }


        bus.publish(
            "statistics",
            statistics,
            t
        )