from config import sensor


REGIMES = {
    "baseline_noise": sensor.sigma_m,
    "elevated_noise": 3.0 * sensor.sigma_m,
}
