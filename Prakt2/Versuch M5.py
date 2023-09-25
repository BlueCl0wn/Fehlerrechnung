from function import *
import numpy as np

# ------ Aufgabe 1: Schallgeschwindigkeit in Medien ------
L = 1.422  # m
f = np.arange(3, 10)  # [3, 4, 5, 6, 7, 8, 9] MHz +-1Hz
lambd = 654  # nm


def c(maxi, n_):
    steigung, a, s_steigung, s_a = wert_xy(f[0:-1], maxi)

    print("sdsdd", s_steigung)
    print("jhkhjkhjk", steigung)
    return n_ * lambd * L / steigung



# ------ Schallgeschwindigkeit in Wasser ------

# Beugungsmaxima-Abstand zum 0. Maximum in mm +-0.1mm
pos_1 = np.array([2, 2.6, 3.1, 4, 4.3, 5, 5.6])  # 1 Ordnung oben
pos_2 = np.array([3.8, 5, 6.2, 7.4, 8.5, 9.8, None])  # 2 Ordnung oben
pos_3 = np.array([5.4, 7.6, None, None, None, None, None])  # 3 Ordnung oben
neg_1 = np.array([2, 2.5, 3, 3.5, 4.3, 5, 5.5])  # 1 Ordnung unten
neg_2 = np.array([3.8, 5, 6, 7.3, 8.6, 9.9, None])  # 2 Ordnung unten
neg_3 = np.array([None, 7.5, None, 11, 13, None, None])  # 3 Ordnung unten

# ------ Schallgeschwindigkeit in Ethanol ------
epos_1 = np.array([2.3, 3.6, 4, 4.5, 5.5, 6, 6.8])  # 1 Ordnung oben
epos_2 = np.array([4.5, 6.4, 7.4, 9, 10.4, 12, None])  # 2 Ordnung oben
eneg_1 = np.array([2.7, 3.9, 4, 4.5, 5.4, 6, 7])  # 1 Ordnung unten
eneg_2 = np.array([5.1, 5.7, 7.4, 9.1, 10.3, 12.4, None])  # 2 Ordnung unten

print("Aufgabe 1.1: Messwerte")

columnLabel = np.char.add(np.array([-3, -2, -1, 1, 2, 3]).astype(str), ". Ordnung")
table(data=np.array([pos_3, pos_2, pos_1, neg_1, neg_2, neg_3]), colLabels=columnLabel, rowLabels=f)

# für ethanol
columnLabel = np.char.add(np.array([-2, -1, 1, 2]).astype(str), ". Ordnung")
table(data=np.array([epos_2, epos_1, eneg_1, eneg_2]), colLabels=columnLabel, rowLabels=f)

print("Aufgabe 1.2: Bestimmung der Schallgeschwindigkeit durch Lineare Regression.")
c_Wasser_1, b = c((neg_1[0:-1] + pos_1[0:-1]) / 2, n_=1)
c_Wasser_2, b2 = c((neg_2[0:-1] + pos_2[0:-1]) / 2, n_=2)
c_Ethanol_1,  = c((eneg_1[0:-1] + epos_1[0:-1]) / 2, n_=1)
c_Ethanol_2, = c((eneg_2[0:-1] + epos_2[0:-1]) / 2, n_=2)

print("c Ordnung 1 Wasser: ", c_Wasser_1, )
print("c Ordnung 2 Wasser: ", c_Wasser_2)
print("c_Wasser_average = ", (c_Wasser_1 + c_Wasser_2) / 2)
print()
print("c Ordnung 1 Ethanol: ", c_Ethanol_1)
print("c Ordnung 2 Ethanol: ", c_Ethanol_2)
print("c_Wasser_average = ", (c_Ethanol_1 + c_Ethanol_2) / 2)

print("\nGeschätzter Fehler ist jeweil '+- 100 m/s'")
print("-----\n")

# ------- Aufgabe 2.1 -----
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
c_Wasser_Aufgabe2 = steigung2 * 2 * h
print("Aufgabe 2.2, c = ", c_Wasser_Aufgabe2)
print(f"Ähnlich zu Wert aus Aufgabe 1. Differenz = {(c_Wasser_1 + c_Wasser_2) / 2 - c_Wasser_Aufgabe2}")

# ------------- Aufgabe 3 ------------

print("\nAus zeitlichen und technischen Gründen sind wir nicht zu Aufgabenteil 3 gekommen.\n")
