import numpy as np
from function import *

t_pos1_1 = np.arange(0, 916, 15)

x_pos1_1 = np.array(
    [6, 2, -3, -11, -7, -15, -19, -22, -25, -27, -29.5, -31, -31.5, -31.5, -31, -30, -28, -26, -23.5, -21, -18, -14.5,
     -11, -7.5, -4, -1, 2, 5, 7.5, 9.5, 11, 12, 13, 13.5, 13, 12.5, 11.5, 10, 8, 6, 4, 1.5, -1, -4, -6, -9, -11, -13.5,
     -15.5, -17.5, -19, -20, -21, -21.5, -21.5, -21.5, -21, -20, -19, -17.5, -15.5, -14])

t_pos1_2 = np.arange(0, 856, 15)
x_pos1_2 = np.array(
    [14, 17, 20.5, 23.5, 26, 28, 30, 31, 31.5, 32, 32, 31.5, 30.5, 29.5, 27.5, 25.5, 23.5, 21, 18, 15.5, 13, 10, 7, 5.5,
     3, 1, 0.5, -1.5, -2.5, -3, -3.5, -3.5, -3, -2, -0.5, 0.5, 2.5, 4, 6, 8, 10, 12.5, 14, 16.5, 18, 21, 22.5, 23.5, 24,
     24.5, 24.5, 24.5, 24, 23, 22, 21, 20, 18])

t_pos2_1 = np.arange(0, 841, 15)
x_pos2_1 = np.array(
    [-3, -4, -5, -5.5, -5.5, -5, -4, -3, -2, 0, 1.5, 3.5, 5.5, 8, 10, 12.5, 14.5, 16.5, 18.5, 20, 21, 22.5, 23, 24, 24,
     24, 23.5, 23, 22, 21, 20, 18, 17, 15, 13.5, 11.5, 10, 8, 6.5, 5, 4, 3, 2.5, 2, 1.5, 1.5, 1.5, 2, 2.5, 3, 4, 5, 6,
     7.5, 8.5, 10, 11.5])

t_pos2_2 = np.arange(0, 841, 15)
x_pos2_2 = np.array(
    [9, 5.5, 2, -1, -4, -6, -8, -9, -10, -10.5, -10, -9.5, -8.5, -7, -5, -3, -0.5, 2.5, 5, 8, 11, 14, 17, 19, 21, 23.5,
     25, 26.5, 27.5, 28, 28, 27.5, 27, 26, 25, 23.5, 21.5, 19.5, 17.5, 15, 12.5, 10, 8, 6, 4, 2, 0.5, -1, -1.5, -2,
     -2.5, -2.5, -2, -1.5, -0.5, 0.5, 1.5])

graph(t_pos1_1, ((x_pos1_1, "Pos1_V1", "scatter"), (np.repeat(-6.06802, x_pos1_1.size), "A_{1,2}", "plot")), title=r"Kugeln in Position 1, Durchführung 1",  xlabel=r"Zeit $t$ in $s$", ylabel=r"Auslenkung in Skalenteilen")
graph(t_pos1_2, ((x_pos1_2, "Pos1_V2", "scatter"), (np.repeat(12.15354, x_pos1_2.size), "A_{1,2}", "plot")), title=r"Kugeln in Position 1, Durchführung 2",  xlabel=r"Zeit $t$ in $s$", ylabel=r"Auslenkung in Skalenteilen")
graph(t_pos2_1, ((x_pos2_1, "Pos2_V1", "scatter"), (np.repeat(11.56372, x_pos2_1.size), "A_{1,2}", "plot")), title=r"Kugeln in Position 2, Durchführung 1",  xlabel=r"Zeit $t$ in $s$", ylabel=r"Auslenkung in Skalenteilen")
graph(t_pos2_2, ((x_pos2_2, "Pos2_V2", "scatter"), (np.repeat(10.98184, x_pos2_2.size), "A_{1,2}", "plot")), title=r"Kugeln in Position 2, Durchführung 2",  xlabel=r"Zeit $t$ in $s$", ylabel=r"Auslenkung in Skalenteilen")
