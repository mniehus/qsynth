from dataclasses import dataclass
import numpy as np


@dataclass
class PhysicalParameters:
    kB: float = 1.380649e-23
    T: float = 298.15
    eta: float = 1.0e-3
    radius: float = 1.5e-6
    delta_rho: float = 1000.0
    kappa: float = 7.3e-6
    g: float = 9.81


@dataclass
class TimingParameters:
    plant_period: float = 20e-6
    measurement_period: float = 20e-6
    estimator_period: float = 20e-6
    controller_period: float = 20e-6
    actuator_period: float = 20e-6

    statistics_period: float = 1e-3
    supervisor_period: float = 100e-3

    actuator_delay: float = 20e-6


@dataclass
class SensorParameters:
    sigma_m: float = 2e-9


physical = PhysicalParameters()
timing = TimingParameters()
sensor = SensorParameters()


gamma = 6.0 * np.pi * physical.eta * physical.radius

D = physical.kB * physical.T / gamma

tau_r = gamma / physical.kappa

sigma_eq = np.sqrt(
    physical.kB
    * physical.T
    / physical.kappa
)

volume = (
    4.0 / 3.0
    * np.pi
    * physical.radius**3
)

m_eff = (
    volume
    * physical.delta_rho
)

x_g = (
    m_eff
    * physical.g
    / physical.kappa
)

a_ref = np.exp(
    -timing.plant_period
    / tau_r
)

Q_phys = (
    sigma_eq**2
    * (1.0 - a_ref**2)
)

R_phys = sensor.sigma_m**2