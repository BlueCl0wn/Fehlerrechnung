from function import *
import numpy as np

#------ Spannungsverstärker ------
# Potentiometer R_E auf 20 Ohm

F = [0.3,0.9,1.94,3,4.5,5.86,10,15,23.2,34,42.5,60,92,193]
U_a = np.array([88,88,88,88,88,88,88,88,88,88,88,88,88,88])
U_e = np.array([0.36,0.88,1.2,1.32,1.42,1.42,1.42,1.42,1.42,1.42,1.42,1.42,1.42,1.42])
v = U_e / U_a

graph(F,v,xlabel='Frequenz',ylabel='Verstärkung', xlog=True)

