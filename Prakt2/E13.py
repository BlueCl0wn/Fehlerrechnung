import numpy as np

from function import *

# ------ Spannungsverstärker ------
# Potentiometer R_E auf 20 Ohm

F = [0.3, 0.9, 1.94, 3, 4.5, 5.86, 10, 15, 23.2, 34, 42.5, 60, 92, 193]
U_a = np.array([88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88])/1000
U_e = np.array([0.36, 0.88, 1.2, 1.32, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42])
v = U_e / U_a

graph(F, v, xlabel='Frequenz in $kHz$', ylabel='Verstärkung', xlog=True)

# -----------------------------------
# v(R_E)
v = np.array([3.260869565, 3.681818182, 4.045454545, 4.613636364, 5.244444444, 5.97826087, 7.409090909, 9.545454545, 12.04545455,
     15.90909091, 18.63636364, 19.54545455])

R_E = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 6, 5.4]

def v_(R_E_, R_C_):
    return -R_C_/R_E_


graph(R_E, ((v, r"gemessene Verstärkung"), (v_(np.array(R_E), -320), r"Fit, $R_C=-320 \Omega$")), xlabel=r"$R_E$ in $\Omega$", ylabel=r"Verstärkung")
graph(R_E, 1/v, trendlinie=True, xlabel=r"$R_E$ in $\Omega$", ylabel=r"Kehrwert der Verstärkung")