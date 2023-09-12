from function import *
import numpy as np

# ------ Aufgabe 1: Schallgeschwindigkeit in Medien ------
L = 1.422  # m
f = [3, 4, 5, 6, 7, 8, 9]  # MHz +-1Hz
lambd = 654  # nm

# ------ Schallgeschwindigkeit in Wasser ------

# Beugungsmaxima-Abstand zum 0. Maximum in mm +-0.1mm
pos_1 = np.array([2, 2.6, 3.1, 4, 4.3, 5, 5.6])
pos_2 = np.array([3.8, 5, 6.2, 7.4, 8.5, 9.8, None])
pos_3 = np.array([5.4, 7.6, None, None, None, None, None])
neg_1 = np.array([2, 2.5, 3, 3.5, 4.3, 5, 5.5])
neg_2 = np.array([3.8, 5, 6, 7.3, 8.6, 9.9, None])
neg_3 = np.array([None, 7.5, None, 11, 13, None, None])
n = np.arange(1, 3)
maxima_wasser = np.array([(neg_1[0:-1] + pos_1[0:-1]) / 2, (neg_2[0:-1] + pos_2[0:-1]) / 2])

steigungen_wasser = [wert_xy(f[0:-1], maxi)[0] for maxi in maxima_wasser]


def c(maxi, n):
    steigung = wert_xy(f[0:-1], maxi)[0]
    return n * lambd * L / steigung


print("c ordnung 1 wasser: ", c((neg_1[0:-1] + pos_1[0:-1]) / 2, n=1))
print("c ordnung 2 wasser: ", c((neg_2[0:-1] + pos_2[0:-1]) / 2, n=2))

# ------ Schallgeschwindigkeit in Ethanol ------
epos_1 = np.array([2.3, 3.6, 4, 4.5, 5.5, 6, 6.8])
epos_2 = np.array([4.5, 6.4, 7.4, 9, 10.4, 12, None])
epos_3 = np.array([None, ])
eneg_1 = np.array([2.7, 3.9, 4, 4.5, 5.4, 6, 7])
eneg_2 = np.array([5.1, 5.7, 7.4, 9.1, 10.3, 12.4, None])
eneg_3 = np.array([None, ])

print("c ordnung 1 ethanol: ", c((eneg_1[0:-1] + epos_1[0:-1]) / 2, n=1))
print("c ordnung 2 ethanol: ", c((eneg_2[0:-1] + epos_2[0:-1]) / 2, n=2))

# ------- Aufgabe 2 -----
f_ultraschall = 64087000  # Hz

Uss_Ordnung_0 = 350  # mV
f_ordnung_0 = 12.8  # MHz

Uss_Ordnung_1 = 170  # mV
f_ordnung_1 = 12.8  # MHz

Uss_Ordnung_2 = 6.7  # mV
f_ordnung_2 = 12.8  # MHz

U_ohne = 900  # mV

delta_phi_0_1 = np.pi
delta_phi_1_2 = np.pi / 4

# ----------- Aufgabe 2.2 -----------
frequenzposition = np.array([3.5373, 3.5492, 3.5589, 3.5694, 3.5796])  # MHz
frequenzposition *= 10e6
dif_frequenzposition = frequenzposition - frequenzposition[0]

m = np.arange(1, 6)
h = 73.1e-3  # m

steigung2 = wert_xy(m, dif_frequenzposition)[0]
c2 = steigung2*2*h
print("Aufgabe 2.2, c = ", c2)


# ------------- Aufgabe 3 ------------

