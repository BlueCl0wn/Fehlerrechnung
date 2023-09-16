import numpy as np
from function import *
import csv

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
Messwerte = Messwerte_.astype(float).transpose(0, 2, 1)
x = Messwerte[0, 0]
Messwerte = Messwerte[0:12, 1, 0:3000]

print(type(Messwerte[0,0]))


#  ---------- Teil 1 -----------
graph(x, Messwerte[0]-Messwerte[8], title="Nettospektrum der Kalibrierungsquelle", xlabel="Ordnungszahl der Pixel", ylabel="Intensität")

