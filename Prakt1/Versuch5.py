from function import *

T_1 = [21.7, 24.3, 24.9, 25.8, 26.7, 27.5, 28.5, 29.2, 30.2, 30.9, 31.8, 32.7, 33.7, 34.5,
       35.4, 36.2, 37.1, 37.9, 38.7, 39.4, 40.3, 41.1, 41.9, 42.7, 43.4, 44.2, 44.9, 45.7, 46.4, 47.2, 47.8, 48.5, 49.3,
       50.0
       ]

U_th = [0.006, 0.088, 0.102, 0.157, 0.188, 0.219, 0.252,
        0.282, 0.314, 0.343, 0.376, 0.406, 0.443, 0.468, 0.502,
        0.530, 0.561, 0.591, 0.619, 0.649, 0.681, 0.711, 0.740,
        0.768, 0.798, 0.826, 0.852, 0.880, 0.907, 0.932, 0.959,
        0.981, 1.009, 1.036]

T = [21.7, 24.3, 24.9, 25.8, 26.7, 27.5, 28.5]
t = [0, 1, 2, 3, 4, 5, 6]
U_H = [10.1, 10.2, 10.2, 10.2, 10.2, 10.2]
I_H = [0.73, 0.73, 0.73, 0.73, 0.73, 0.73]

n = [5, 10, 15, 20]
R = [5.9900225,14.2062717,14.4678010,18.6938857]

##t_2 = [0, 60, 120, 180, 240, 300, 360, 420, 480]
t_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

ln_dT_Papier_5 = [3.203481101, 2.905374511, 2.57069707, 2.238816785, 1.906417873, 1.560141637, 1.245273424, 0.933685831]
ln_dT_Papier_10 = [3.169579549, 3.025151565, 2.853135292, 2.683353084, 2.572786935, 2.434172559, 2.306448185,
                   2.175637883, 2.067513026]
ln_dT_Papier_15 = [3.288638909, 3.095648396, 2.943558298, 2.806314795, 2.673963344, 2.549554633, 2.42453393,
                   2.295489172, 2.175637883]
ln_dT_Papier_20 = [3.212330716, 3.060380257, 2.953594224, 2.830805815, 2.750225329, 2.658753925, 2.572786935,
                   2.42453393, 2.300983691]

lndT_Holz = [3.241632867, 3.117681111, 3.011782382, 2.900873378, 2.806314795, 2.694505616, 2.627623007, 2.54097089,
             2.455525684]

lndT_Styro = [3.158018727, 3.065495358, 3.026478705, 2.980337549, 2.943558298, 2.906870398, 2.862554514, 2.838837987,
              2.784592972]


print("5.1:")
wert_x(U_H, name="U_H")

wert_x(I_H, name="I_H")

wert_xy(t, T, name="T(t)")

wert_xy(T_1, U_th, name="U_th(T)")

print("R_kontakt_1 = 0.5*a")
wert_xy(n, R, name="R_ges(n)")

# Lineare Regression von Papier
wert_xy(t_2[:6], ln_dT_Papier_5, name="dT(t) Papier5")
wert_xy(t_2, ln_dT_Papier_10, name="dT(t) Papier10")
wert_xy(t_2, ln_dT_Papier_15, name="dT(t) Papier15")
wert_xy(t_2, ln_dT_Papier_20, name="dT(t) Papier20")

print("\n5.2:")

# Lineare Regression von Holz
wert_xy(t_2, lndT_Holz, name="dT(t) Holz")

# Lineare Regression von Styropor
wert_xy(t_2, lndT_Styro, name="dt(t) Styro")