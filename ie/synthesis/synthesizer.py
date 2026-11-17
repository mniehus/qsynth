from dataclasses import dataclass

from config import (
    Q_phys,
    R_phys,
    sigma_eq
)

class QSynthesizer:
    """
    Q-SYNTH SYNTHESIS — OFFLINE
    ===========================

    Inputs
    ------
    physical plant model
    measurement model
    actuator/hardware model
    timing constraints
    FPGA-resource constraints
    performance objective J

    Outputs
    -------
    Policy library / parameter maps.

    Example policy:

        phi = {Q_eff, R_eff}
        psi = {alpha, XT}

    Function
    --------
    Performs computationally expensive design-stage
    evaluation and optimization.

    Candidate computing platforms
    -----------------------------
    P1:
        desktop CPU/GPU software

    P4:
        quantum-assisted / QPU computation

    Important
    ---------
    The example implementation below does NOT yet perform
    optimization.

    It merely constructs two illustrative policy sets.

    This class is the location where classical and later
    quantum-assisted synthesis algorithms will be inserted.
    """

    def synthesize(self):

        nominal = Policy(

            name="nominal",

            Q_eff=Q_phys,

            R_eff=R_phys,

            alpha=2.0,

            XT=0.0
        )


        robust = Policy(

            name="robust",

            # Example only:
            # trust plant model less
            Q_eff=2.0 * Q_phys,

            R_eff=R_phys,

            alpha=1.3,

            XT=0.25 * sigma_eq
        )


        return {

            "nominal":
                nominal,

            "robust":
                robust
        }


@dataclass
class Policy:
    """
    One estimator/controller parameter set.

    Estimator parameters
    --------------------
    Q_eff:
        Effective process-noise variance.

    R_eff:
        Effective measurement-noise variance.

    Controller parameters
    ---------------------
    alpha:
        Ratchet feedback gain.

    XT:
        Trigger threshold [m].
    """

    name: str

    Q_eff: float
    R_eff: float

    alpha: float
    XT: float