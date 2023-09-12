from function import *
import numpy as np

#------ Spannungsverstärker ------
# Potentiometer R_E auf 20 Ohm

F = [0.3,0.9,1.94,3,4.5,5.86,10,15,23.2,34,42.5,60,92,193]
U_a = np.array([88,88,88,88,88,88,88,88,88,88,88,88,88,88])
U_e = np.array([0.36,0.88,1.2,1.32,1.42,1.42,1.42,1.42,1.42,1.42,1.42,1.42,1.42,1.42])
v = U_e / U_a

graph(F,v,xlabel='Frequenz',ylabel='Verstärkung', xlog=True)

R_C = 300
R_E = [5.4, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
v_2 = [19.5, 18.64,16,12.05,9.55,7.41,5.98,5.24,4.61,4.05,3.68,3.26]

graph (R_E,v_2,xlabel='Potentiometer-Widerstand',ylabel='Verstärkung')


