import numpy as np
from function import *
import csv
from scipy.signal import find_peaks

URI = "Messwerte-O7/"
with open(URI + "Hg 1 IZeit0,1s.csv") as csvdatei:
    HG_1_Zeit_100ms = csv.reader(csvdatei, delimiter=';')
    HG_1_Zeit_100ms = [row for row in HG_1_Zeit_100ms]
with open(URI + "Hg Zwei Gitter IZeit0,1s.csv") as csvdatei:
    HG_2_Gitter_Zeit_100ms = csv.reader(csvdatei, delimiter=';')
    HG_2_Gitter_Zeit_100ms = [row for row in HG_2_Gitter_Zeit_100ms]
with open(URI + "Ar IZeit200s.csv") as csvdatei:
    Ar_Zeit_200000ms = csv.reader(csvdatei, delimiter=';')
    Ar_Zeit_200000ms = [row for row in Ar_Zeit_200000ms]
with open(URI + "Ar IZeit200s 2222.csv") as csvdatei:
    Ar_2_Zeit_200000ms = csv.reader(csvdatei, delimiter=';')
    Ar_2_Zeit_200000ms = [row for row in Ar_2_Zeit_200000ms]
with open(URI + "H2 IZeit100s.csv") as csvdatei:
    H2_zeit_100000ms = csv.reader(csvdatei, delimiter=';')
    H2_zeit_100000ms = [row for row in H2_zeit_100000ms]
with open(URI + "He IZeit200s.csv") as csvdatei:
    He_Zeit_200000ms = csv.reader(csvdatei, delimiter=';')
    He_Zeit_200000ms = [row for row in He_Zeit_200000ms]
with open(URI + "Leuchtstoff IZeit 1,2s.csv") as csvdatei:
    Leuchtstoff_Zeit_1200ms = csv.reader(csvdatei, delimiter=';')
    Leuchtstoff_Zeit_1200ms = [row for row in Leuchtstoff_Zeit_1200ms]
with open(URI + "Ne IZeit200s.csv") as csvdatei:
    Ne_Zeit_200000ms = csv.reader(csvdatei, delimiter=';')
    Ne_Zeit_200000ms = [row for row in Ne_Zeit_200000ms]
with open(URI + "Dunkelspektrum IZeit 0,1s.csv") as csvdatei:
    Dunkel_zeit_100ms = csv.reader(csvdatei, delimiter=';')
    Dunkel_zeit_100ms = [row for row in Dunkel_zeit_100ms]
with open(URI + "Dunkelspektrum IZeit 1,2s.csv") as csvdatei:
    Dunkel_zeit_1200ms = csv.reader(csvdatei, delimiter=';')
    Dunkel_zeit_1200ms = [row for row in Dunkel_zeit_1200ms]
with open(URI + "Dunkelspektrum IZeit 100s.csv") as csvdatei:
    Dunkel_zeit_100000ms = csv.reader(csvdatei, delimiter=';')
    Dunkel_zeit_100000ms = [row for row in Dunkel_zeit_100000ms]
with open(URI + "Dunkelspektrum IZeit 200s.csv") as csvdatei:
    Dunkel_zeit_200000ms = csv.reader(csvdatei, delimiter=';')
    Dunkel_zeit_200000ms = [row for row in Dunkel_zeit_200000ms]

Messwerte_ = [HG_1_Zeit_100ms, HG_2_Gitter_Zeit_100ms, Ar_Zeit_200000ms, Ar_2_Zeit_200000ms, H2_zeit_100000ms,
              He_Zeit_200000ms, Leuchtstoff_Zeit_1200ms, Ne_Zeit_200000ms, Dunkel_zeit_100ms, Dunkel_zeit_1200ms,
              Dunkel_zeit_100000ms, Dunkel_zeit_200000ms]

Messwerte_ = np.asarray(Messwerte_)
Messwerte_ = np.core.defchararray.replace(Messwerte_, ",", ".")
Messwerte = Messwerte_.astype(float).transpose(0, 2, 1)
x = Messwerte[0, 0]
Messwerte = Messwerte[0:12, 1, 0:3000]


#  ---------- Teil 1 -----------


def find_maxima(x) -> np.ndarray:
    temp = find_peaks(x, prominence=0.015)
    return np.array(temp[0])


Nettospektrum_Hg = Messwerte[0] - Messwerte[8]
graph(x, Nettospektrum_Hg, graph="plot", title="Nettospektrum von Quecksilber nach Ordnung",
      xlabel="Wellenlänge in $m$", ylabel="Intensität")

Maxima_Nettospektrum_Hg = find_maxima(Nettospektrum_Hg)
wavelength_hg = np.array([578.966, 576.959, 546.074, 435.835, 407.781, 404.656, np.nan]) * 10 ** -9
data_Hg = (Maxima_Nettospektrum_Hg, np.around(Nettospektrum_Hg[Maxima_Nettospektrum_Hg], 3), wavelength_hg)
# print(data_Hg)
table(data=data_Hg, colLabels=[r"Ordnung $z_i$", r"Intensität", r"Wellenlänge $\lambda_i$"])

graph(data_Hg[0][0:-1], data_Hg[2][0:-1], trendlinie=True, xlabel=r"Ordnungszahl $z_i$",
      ylabel=r"Wellenlänge $\lambda_i$")

wavelengths = -7.35 * 10 ** -11 * x + 5.81 * 10 ** -7
graph(wavelengths, Nettospektrum_Hg, graph="plot", title="Nettospektrum von Quecksilber nach der Wellenlänge",
      xlabel="Wellenlänge in $m$", ylabel="Intensität")

graph(wavelengths[2370:2430], Nettospektrum_Hg[2370:2430], xlabel="Wellenlänge in $m$", ylabel="Intensität",
      title=r"Ausschnitt des Spektrums", graph="plot")


# -------- Teil 2 ----------

def do_stuff_for_teil_2(br, d, material="TEST"):
    netto = br - d
    graph(wavelengths, netto, graph="plot", title=f"Nettospektrum von {material} nach der Wellenlänge",
          xlabel="Wellenlänge in $m$", ylabel="Intensität")


"""
HG_1_Zeit_100ms, HG_2_Gitter_Zeit_100ms, Ar_Zeit_200000ms, Ar_2_Zeit_200000ms, H2_zeit_100000ms,
He_Zeit_200000ms, Leuchtstoff_Zeit_1200ms, Ne_Zeit_200000ms, Dunkel_zeit_100ms, Dunkel_zeit_1200ms,
Dunkel_zeit_100000ms, Dunkel_zeit_200000ms"""

# He
do_stuff_for_teil_2(Messwerte[5], Messwerte[11], material="Helium")
# Ar
do_stuff_for_teil_2(Messwerte[3], Messwerte[11], material="Argon")
# H2
do_stuff_for_teil_2(Messwerte[4], Messwerte[10], material="Wasserstoff")
# Ne
do_stuff_for_teil_2(Messwerte[7], Messwerte[11], material="Neon")
# Leuchstoffbirne
do_stuff_for_teil_2(Messwerte[6], Messwerte[9], material="Leuchtstoff")


def stuff(filename, delimiter=';'):
    with open(URI + filename) as csvdatei:
        file = csv.reader(csvdatei, delimiter=delimiter)
        list_ = [row for row in file]
    list_ = np.core.defchararray.replace(list_, ",", ".")

    list__ = list_.astype(float).transpose()
    return list__[1]


handy_brutto = np.array(list(map(stuff, ["Handy ohne Glas IZeit0,3s.csv", "Handy, L1 = 4,9mm IZeit0,3s.csv",
                                         "Handy, L2 = 0,95mm IZeit0,3s.csv", "Handy, L3 = 3mm IZeit0,3s.csv"])))

handy = handy_brutto - Messwerte[8]


def transmission(Lj, Li):
    return Li / Lj


transmission3_2 = transmission(handy[2], handy[0])
transmission3_1 = transmission(handy[1], handy[0])
transmission2_1 = transmission(handy[1], handy[2])
"""print(f"Transmission_(L3-L2) = {transmission2_1}")
print(f"Transmission_(L3-L2) = {transmission3_1}")
print(f"Transmission_(L2-L1) = {transmission3_2}")"""

transmissions = ((transmission3_2, r"Transmission $T_(L_3-L_2) (\lambda)$", 'plot'),
                 (transmission3_1, r"Transmission $T_(L_3-L_1) (\lambda)$", 'plot'),
                 (transmission2_1, r"Transmission $T_(L_2-L_1) (\lambda)$", 'plot'))

transmissions_free = [transmission2_1, transmission3_2, transmission3_1]

graph(wavelengths, transmissions, graph="plot", xlabel=r"Wellenlänge $\lambda$", ylabel=r"Transmission", multiple=True)

x1 = 625
x2 = 260
lambda1 = wavelengths[625]
lambda2 = wavelengths[260]
print(f"lambda1 = {lambda1},  lambda2 = {lambda2}")

dL = [2.05, 1.95, 3.95]
graph(dL, [transmission2_1[x1], transmission3_2[x1], transmission3_1[x1]],
      title=r"$T(\Delta L)$ für $\lambda=534,989 nm$", xlabel=r"$\Delta L, [L2-1, L3-2, L3-1]$", ylabel="Transmission")
graph(dL, [transmission2_1[x2], transmission3_2[x2], transmission3_1[x2]],
      title=r"$T(\Delta L)$ für $\lambda=561,816 nm$", xlabel=r"$\Delta L, [L2-1, L3-2, L3-1]$", ylabel="Transmission")


def absorp(trans, dL_):
    trans[trans < 0] = 0
    return -1 / dL_ * np.log(trans)


kappas = ((absorp(transmission2_1, 2.05), r"$\kappa$ für $T_(L_3f-L_2) (\lambda)$", 'plot'),
          (absorp(transmission3_2, 1.95), r"$\kappa$ für $T_(L_3-L_1) (\lambda)$", 'plot'),
          (absorp(transmission3_1, 3.95), r"$\kappa$ für $T_(L_2-L_1) (\lambda)$", 'plot'))

graph(wavelengths, kappas,
      title=r"$\kappa$ nach $\lambda$", xlabel=r"$\lambda$ in $m$", ylabel=r"$\kappa$", graph="plot")

# ----- TEil 4 ------
do_stuff_for_teil_2(np.flip(Messwerte[1]), np.flip(Messwerte[8]), "Quecksilber mit 2 Gittern")
do_stuff_for_teil_2(Messwerte[0], Messwerte[8], "Quecksilber mit 1 Gittern")

"""vergleich = ((Messwerte[0] - Messwerte[8], "Hg mit 1 Gitter", 'plot'),
             (Messwerte[1] - Messwerte[8], "Hg mit 2 Gittern", 'plot'))

graph(wavelengths, vergleich, graph="plot", title=f"Nettospektrum von HG nach der Wellenlänge. Vergleich 1 und 2 Gitter",
          xlabel="Wellenlänge in $m$", ylabel="Intensität", multiple=True)"""
