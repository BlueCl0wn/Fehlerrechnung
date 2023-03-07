from function import *

MY_0 = 4 * np.pi * 10 ** (-7)

print("\n---------------- 1. magnetfeld eines stromdurchlossenen Leiters -------------")

# ------------ Kalibrierung ----------
I_1 = 10
U_H_1 = [0.208, 0.156, 0.132, 0.092, 0.068, 0.064]
d_v_mm = [4.2, 7.8, 11.3, 18.0, 22.6, 28.55]
d_v = [(i * 10 ** (-3)) for i in d_v_mm]


def y_kalibrierung(U_h_: list) -> list:
    return [(MY_0 * I_1 / (2 * np.pi * i)) for i in U_h_]


C_H, C_H__d_0 = wert_xy(d_v, y_kalibrierung(U_H_1), name="d_v(y(U_h))")

# ---------- Vermessung der Spule ---------

# konstant für alle Aufgabenteile
D = 45.25 * 10 ** (-3)  # Dicke der Spule
N = 31

# Berechnungsmethode 1 für B
I_2 = [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
U_H_2 = [0, 0.313, 0.616, 0.937, 1.249, 1.560, 1.876]


def B_1(U_H_: list | float):
    if type(U_H_) == list:
        return [C_H * i for i in U_H_]
    else:
        return C_H * U_H_


print(f"B mit erster Berechnungsmethode C_h * U_H_i: {B_1(U_H_2)}")

print("\n\n---------------- 2. Magnetische Induktion einer Spule -------------")

# -- 2a. Variation der  Stromstärke --

# MY_R = 1 daher ignoriert

L_1 = 133.7 * 10 ** (-3)  # Länge der Spule


def B_M(I: list) -> list:
    return [MY_0 * (N * i) / (math.sqrt(L_1 ** 2 + D ** 2)) for i in I]


graph(I_2, B_M(I_2), trendlinie=True, xlabel="$I$ in $A$", ylabel=r"$B_M(I)$ in $T$")

# -- 2b. Variation des Ortes --

U_H_3 = [0.965, 0.990, 0.990, 0.955, 0.902, 0.658, 0.053, 0.032, 0.022, 0.15, 0.17, 0.14]
d_M_mm = [0.0, 17, 33, 47, 62, 99, 153, 167, 189, 227, 253, 275]
d_M = [d * 10 ** (-3) for d in d_M_mm]
I_3 = 5.0
L_3 = 0.22


def B_x(d_M_: list) -> list:
    first = MY_0 * (N * I_3) / (2 * L_3)

    def second(x: int) -> float:
        return (L_3 + 2 * x) / (math.sqrt(D ** 2 + (L_3 + 2 * x) ** 2))

    def third(x: int) -> float:
        return (L_3 + 2 * x) / (math.sqrt(D ** 2 + (L_3 - 2 * x) ** 2))

    return [first * (second(x) + third(x)) for x in d_M_]


B_x_1 = B_1(U_H_3)
B_x_2 = B_x(d_M)

graph(d_M, ((B_x_1, r"$B_t (x)$"), (B_x_2, r"$B(x)$")), xlabel=r"$d_M$ in $m$", ylabel=r"$B(x)$ in $T$")

# -- 2c. Variation der Spulenlänge --

# I aus 2b also I_3 = 5

U_H_4 = [0.788, 0.940, 1.241, 1.750, 2.486, 2.909]
L_4 = [0.273, 0.226, 0.172, 0.119, 0.079, 0.061]


def B_M_4(L_: list) -> list:
    return [(MY_0 * (N * I_3) / (math.sqrt(D ** 2 + l ** 2))) for l in L_]


graph(L_4, ((B_M_4(L_4), r"B_M(L)"), (B_1(U_H_4), r"B(U_H)")), xlabel=r"Spulenlänge $L$ in $m$",
      ylabel=r"$B_M(L)$ in $T$")

# -- 2d. Variation des Materials --

L_5 = 0.1
I_5 = 3

U_H_Eisen = 2.132
U_H_Luft = 0.369


def MY_R(B: int) -> int:
    return (B * math.sqrt(D ** 2 + L_5 ** 2)) / (MY_0 * N * I_5)


print(f"Magnetische Induktion mit Eisenkern: B={B_1(U_H_Eisen)}")

print(f"Magnetische Induktion ohne Eisenkern: B={B_1(U_H_Luft)}")

print(f"MY_R von Eisen: B={MY_R(B_1(U_H_Eisen))}")

# --------------- 3. magnetischer Dipol ------------------------------
# -- 3a. Bestimmung der Federkonstante --
print("\n---------------- 3. magnetischer Dipol -------------")

m_g = [0, 1, 2, 3, 4, 5]
m = [i * 10 ** (-3) for i in m_g]
# dL_cm = [-0.4, 0.7, 1.7, 2.8, 3.9, 5.0] in nächster Zeile als Betrag
dL_cm = [0, 1.1, 2.1, 3.2, 4.3, 5.4]
dL = [i * 10 ** (-2) for i in dL_cm]


def F(m_: list) -> list:
    return [m_i * 9.81 for m_i in m_]


graph(dL, F(m), trendlinie=True, xlabel=r"$dL$ in $m$", ylabel=r"$F(m)$ in $N$")
wert_xy(dL, F(m), name="Federkonstante D, wobei b=D")


# -- 3b. Messung der magnetischen Induktion B --

U_H_20 = [0.700, 0.718, 0.723, 0.725, 0.716]  # Umlaufsinn gleich
U_H_21 = [0.331, 0.190, 0.008, -0.188, -0.324]  # Umlaufsinn entgegengesetzt
z = [-3, -1.5, 0, 1.5, 3]
I_20 = 3

B_20 = B_1(U_H_20)
B_21 = B_1(U_H_21)
graph(z, ((B_20, r"Stromrichtung gleich"), (B_21, r"Stromrichtung entgegengesetzt")), xlabel=r"$z$ in $m$", ylabel=r"$B(z$ in $T$")
dB_dz_20, a_20, s_dB_dz_20, s_a_20 = wert_xy(z, B_20, name="Magnetfeld bei Stromrichtung gleich")
dB_dz_21, a_21, s_dB_dz_21, s_a_21 = wert_xy(z, B_20, name="Magnetfeld bei Stromrichtung entgegengesetzt")

print(f"Quotient B/I bei z = 0:")
print(f"\tStromrichtung gleich: {B_20[2] / I_20}")
print(f"\tStromrichtung entgegengesetzt: {B_21[2] /  I_20}")

print(f"(dB/dz)/I bei z = 0:")
print(f"\tStromrichtung gleich: {dB_dz_20 / I_20}")
print(f"\tStromrichtung entgegengesetzt: {dB_dz_21 / I_20}")


# -- 3b. Bestimmung des magnetischen Dipolmoments my --














