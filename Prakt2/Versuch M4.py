from function import *
import numpy as np

phi_e = 5

# ------ Teil 1 ---------
maxima_t_gebremst = [0.62, 2.59, 4.55, 6.55, 8.52, 10.48, 12.47, 14.45]
maxima_phi_gebremst = [24.8, 18.3, 12.8, 9.3, 6.3, 4.3, 3.3, 1.8]

delta_1_gebremst, a, s_b, s_a = wert_xy(maxima_t_gebremst, np.log(maxima_phi_gebremst), "Teil 1 gebremst")
omega_1_gebremst = 3.173
omega_0_1_gebremst = np.sqrt(omega_1_gebremst ** 2 + delta_1_gebremst ** 2)

maxima_t_ungebremst = [0.76, 2.75, 4.73, 6.70, 8.68, 10.66, 12.63]
maxima_phi_ungebremst = [29.8, 29.3, 28.8, 28.3, 27.8, 27.3, 26.8]

delta_1_ungebremst, a, s_b, s_a = wert_xy(maxima_t_ungebremst, np.log(maxima_phi_ungebremst), "Teil 1 ungebremst")
omega_1_ungebremst = 2 * np.pi / (2.75 - 0.76)
omega_0_1_ungebremst = np.sqrt(omega_1_ungebremst ** 2 + delta_1_ungebremst ** 2)

omega_0_1_average = (omega_0_1_ungebremst + omega_0_1_gebremst) / 2

# -------- Teil 2 -----

motorfrequenzen = [0.2, 0.35, 0.45, 0.47, 0.5, 0.501, 0.502, 0.503, 0.505, 0.51, 0.52, 0.55, 0.6, 0.7, 0.74, 0.8, 0.9,
                   1, 1.1, 1.2, 1.4]

schwingerposition = [110, 100, 118, 132, 175, 174, 177, 178, 185, 195, 217, 246, 260, 270, 271, 270, 275, 270, 276, 272,
                     268, ]
phasendifferenz = [20, 10, 28, 42, 85, 84, 87, 88, 95, 105, 127, 156, 170, 180, 181, 180, 185, 180, 186, 182, 178, ]
amplitude = [6.9, 10.6, 25, 34.3, 54, 55, 55, 55.5, 56, 54.2, 48.5, 27.6, 13.3, 6.3, 4.9, 3.8, 2.5, 1.7, 1.6, 0.9,
             0.7, ]

omega_es = 2 * np.pi * np.array(motorfrequenzen)

table(data=[omega_es.round(2), amplitude, phasendifferenz],
      colLabels=[r"$\omega_e$ in $1/s$", r"Amplitude in Grad", r"Phasendifferenz in Grad"])

graph(omega_es, amplitude, title=r"gemessene Amplitudenresonanzkurve", xlabel=r"$\omega$ in $1/s$",
      ylabel=r"Amplitude in $Grad$")


def phi_erz(omega_e: int, omega_0, phi_e_, delta) -> int:
    """
    Berechnet theoretische Amplitudenresonanzkurve
    :param delta: 
    :param phi_e_: Amplitude des Erregers
    :param omega_0: ungedämpftes Omega
    :param omega_e: Omega des Erregers
    :return:
    """
    bruch = np.sqrt((omega_0 ** 2 - omega_e ** 2) ** 2 + (4 * delta ** 2 * omega_e ** 2))
    return omega_0 ** 2 / bruch * phi_e_


omegas = np.linspace(0.2 * 2 * np.pi, 1.4 * 2 * np.pi, 1000)

y_ampkurve = phi_erz(omegas, omega_0_1_average, phi_e, delta_1_gebremst)
graph(omegas, y_ampkurve, title="berechnete Amplitudenresonanzkurve", xlabel=r"$\omega$ in $rad/s$",
      ylabel=r"Amplitude in $Grad$")

# -------- Teil 5 -----
I = [0.7, 0.6, 0.5, 0.4, 0.3]
U = [5.9, 5.1, 4.3, 3.4, 2.5]
