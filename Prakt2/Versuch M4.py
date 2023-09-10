from function import *
import numpy as np

phi_e = 5

# ------ Teil 1 ---------
maxima_t = [0.62, 2.59, 4.55, 6.55, 8.52, 10.48, 12.47, 14.45]
maxima_phi = [24.8, 18.3, 12.8, 9.3, 6.3, 4.3, 3.3, 1.8]

b, a, s_b, s_a = wert_xy(maxima_t, maxima_phi, "Teil 1")
delta_1 = b

omega_1 = 3.173
omega_0_1 = np.sqrt(omega_1 ** 2 + delta_1 ** 2)


# -------- Teil 2 -----


def phi_erz(omega_e: int, omega_0, phi_e) -> int:
    """
    Berechent theoretische Amplitudenresonanzkurve
    :param phi_e: Ampltiude des Erregers
    :param omega_0: ungedämpftes Omega
    :param omega_e: Omega des Erregers
    :return:
    """
    return omega_0 ** 2 / np.sqrt((omega_0 ** 2 - omega_e ** 2) ** 2 + 4 * delta_1 ** 2 * omega_e ** 2) * phi_e


omegas = np.linspace(0.2, 1.4, 1000)
y_ampkurve = phi_erz(omegas, omega_0_1, phi_e)
graph(omegas, y_ampkurve, title="Amplitudenresonanzkurve", xlabel=r"\omega", ylabel=r"Amplitude")


# -------- Teil 5 -----
I = [0.7,0.6,0.5,0.4,0.3]
U = [5.9,5.1,4.3,3.4,2.5]

