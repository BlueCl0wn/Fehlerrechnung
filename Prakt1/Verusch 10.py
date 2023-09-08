from function import *

# Konstanten
e = 1.6022 * 10 ** -19

# Auswertung für Versuch 10


# ----------------- Messwerte ---------------------


# Versuchsteil 1

C = 7.48 * 10 ** -4
s_C = 0.05 * 10 ** -4

s_U_B = 1

s_d = 0.001

# Messreihe a
U_B_a = 298
I_a = [1.48, 1.74, 2.08, 2.30, 2.70, 3.04, 3.34, 3.60, 4.56, 5.10]
d_a_mm = [97.4, 79.1, 66.2, 59.2, 50.4, 45.3, 41.0, 38.85, 31.0, 27.6]
d_a = [d * 10 ** -3 for d in d_a_mm]

# Messreihe b
I_b = 1.45
U_B_b = [98, 118, 138, 158, 178, 198, 218, 238, 258, 278]
d_b_mm = [39.7, 48.4, 52.2, 56.9, 62.2, 65.4, 71.3, 75.7, 83.0, 93.5]
d_b = [d * 10 ** -3 for d in d_b_mm]

# Messreihe c
d_c = 67.3 * 10 ** -3
U_B_c = [184, 196, 210, 224, 240, 250, 263, 280, 287, 299]
I_c = [1.21, 1.34, 1.48, 1.55, 1.76, 1.76, 1.85, 2.01, 2.04, 2.06]


def e_m(U_B_, d_, I_):
    def e_m_single(U_B, d, I__):
        return (2 * U_B) / (C * I__ * (d / 2)) ** 2

    def s_e_m_single(U_B, d, I__):
        a = (2 / (C * I__ * (d / 2)) ** 2 * s_U_B) ** 2
        b = ((2 * U_B) / (C * I__ ** 1.5 * (d / 2)) ** 2 * I__ * 0.012) ** 2
        c = ((2 * U_B) / (C ** 1.5 * I__ * (d / 2)) ** 2 * s_C) ** 2
        d = ((2 * U_B) / (C * I__ * (d ** 1.5 / 2)) ** 2 * s_d) ** 2
        return sqrt(a + b + c + d)

    e_m_ = [e_m_single(U_B, d, I_i) for U_B, d, I_i in zip(U_B_, d_, I_)]
    s_e_m_ = [s_e_m_single(U_B, d, I_i) for U_B, d, I_i in zip(U_B_, d_, I_)]

    return e_m_, s_e_m_


def m_e(U_B_, d_, I_):
    def m_e_single(U_B, d, I__):
        return (C * I__ * (d / 2)) ** 2 / (2 * U_B)

    def s_m_e_single(U_B, d, I__):
        a = ((C * I__ * (d / 2)) ** 2 / (2 * U_B ** 2) * s_U_B) ** 2
        b = (I__ * (C * (d / 2)) ** 2 / (2 * U_B) * I__ * 0.012) ** 2
        c = (C * (I__ * (d / 2)) ** 2 / (2 * U_B) * s_C) ** 2
        d = (d * (C * I__ * (1 / 2)) ** 2 / (2 * U_B) * s_d) ** 2
        return sqrt(a + b + c + d)

    m_e_ = [m_e_single(U_B, d, I_i) for U_B, d, I_i in zip(U_B_, d_, I_)]
    s_m_e_ = [s_m_e_single(U_B, d, I_i) for U_B, d, I_i in zip(U_B_, d_, I_)]

    return m_e_, s_m_e_


def m(U_B_, d_, I_):
    def m_single(U_B, d, I__):
        return e * (((C * I__ * (d / 2)) ** 2) / (2 * U_B))

    def s_m_single(U_B, d, I__):
        a = (e * (C * I__ * (d / 2)) ** 2 / (2 * U_B ** 2) * s_U_B) ** 2
        b = (e * I__ * (C * (d / 2)) ** 2 / (2 * U_B) * I__ * 0.012) ** 2
        c = (e * C * (I__ * (d / 2)) ** 2 / (2 * U_B) * s_C) ** 2
        d = (e * d * (C * I__ * (1 / 2)) ** 2 / (2 * U_B) * s_d) ** 2
        return sqrt(a + b + c + d)

    m_ = [m_single(U_B, d, I_i) for U_B, d, I_i in zip(U_B_, d_, I_)]
    s_m_ = [s_m_single(U_B, d, I_i) for U_B, d, I_i in zip(U_B_, d_, I_)]

    return m_, s_m_


def calc(U_, d_, I_):
    if type(U_) != list:
        U_ = [U_] * len(d_)
    if type(d_) != list:
        d_ = [d_] * len(U_)
    if type(I_) != list:
        I_ = [I_] * len(U_)

    e_m_, s_e_m_ = e_m(U_, d_, I_)
    print(f"e/m = {e_m_}")
    e_m_mean = mean(e_m_)
    s_e_m_mean = mean(s_e_m_)
    print(f"e/m_mean = {e_m_mean: .3e} +- {s_e_m_mean: .3e}")
    a, b = wert_x(e_m_)
    s_e_m_mean_2 = sqrt(s_e_m_mean ** 2 + b ** 2)
    print(f"s_e/m_mean_kombiniert = {s_e_m_mean_2: .3e}")

    m_e_, s_m_e_ = m_e(U_, d_, I_)
    print(f"m/e = {m_e_}")
    m_e_mean = mean(m_e_)
    s_m_e_mean = mean(s_m_e_)
    print(f"m/e_mean = {m_e_mean: .3e} +- {s_m_e_mean: .3e}")
    a, b = wert_x(m_e_)
    s_m_e_mean_2 = sqrt(s_m_e_mean ** 2 + b ** 2)
    print(f"s_m/e_mean_kombiniert = {s_m_e_mean_2: .3e}")

    m_, s_m_ = m(U_, d_, I_)
    print(f"m = {m_}")
    m_mean = mean(m_)
    s_m_mean = mean(s_m_)
    print(f"m_mean = {m_mean: .3e} +- {s_m_mean: .3e}")
    a, b = wert_x(m_)
    s_m_mean_2 = sqrt(s_m_mean ** 2 + b ** 2)
    print(f"s_m_mean_kombiniert = {s_m_mean_2: .3e}")

    headline = ["I / A", "U_B / V", "d / mm", "e/m / C/kg", "s_e/m / C/kg", "m/e / kg/C", "s_m/e / kg/C", "m / kg",
                "s_m / kg"]
    temp = [I_, U_, d_, e_m_, s_e_m_, m_e_, s_m_e_, m_, s_m_]
    arr = np.array(np.asarray(temp))
    # print(f"test = {arr}")
    return arr


print("\n-------- a --------")
aa = calc(U_B_a, d_a, I_a)
print("\n-------- b --------")
bb = calc(U_B_b, d_b, I_b)
print("\n-------- c --------")
cc = calc(U_B_c, d_c, I_c)
