from function import *
import numpy as np

# ------ Teil 1 ---------
maxima_t = [0.62, 2.59, 4.55, 6.55, 8.52, 10.48, 12.47, 14.45]
maxima_phi =  [24.8, 18.3, 12.8, 9.3, 6.3, 4.3, 3.3, 1.8]

b, a, s_b, s_a = wert_xy(maxima_t, maxima_phi, "Teil 1")
delta_1 = b

omega_1 = 3.173
omega_0_1 = np.sqrt(omega_1**2 + delta**2)


# -------- Teil 2 -----

omega_0 = None
phi_e = None


def phi_erz(omega_e: int) -> int:
    """
    Berechent theoretische Amplitudenresonanzkurve
    :param omega_e:
    :return:
    """
    return omega_0**2 / np.sqrt((omega_0**2 - omega_e**2)**2 + 4 * delta**2 * omega_e**2) * phi_e

omegas = np.linspace(0.2, 1.4, 1000)
y_ampkurve = phi_erz(omegas)#
graph(omegas, y_ampkurve, title="Amplitudenresonanzkurve", xlabel=r"\omega", ylabel=r"Amplitude")
