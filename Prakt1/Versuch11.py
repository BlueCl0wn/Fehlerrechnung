from function import *

# -------------- Messwerte ------------
# Einheiten sind in SI, wenn nicht anders im Variablennamen angegeben.

# 3. Versuchsteil Test
R = 500 #in Hz

f_kHz = [1.103, 3.103, 5.09, 7.11, 9.10, 10.10, 10.6, 10.85, 10.90, 11.0, 11.03, 11.32, 12.33, 17.33, 18.33, 28.33, 48.33, 78.33, 98.33, 111.33]  # in kHz
f = [f_i * 10**3 for f_i in f_kHz]

U_FGK_mV = [1140, 1120, 1080, 1040, 940, 880, 880, 860, 860, 860, 860, 880, 960, 1020, 1020, 1080, 1100, 1100, 1120, 1120]  # in mV
U_FGK = [U_i * 10**-3 for U_i in U_FGK_mV]

U_B_mV = [100, 158, 284, 427, 680, 800, 820, 800, 800, 800, 800, 800, 760, 416, 384, 282, 124, 68.8, 52, 42.4]  # in mV
U_B = [U_i * 10**-3 for U_i in U_B_mV]

dt_mus = [236, 74, 58.4, 26.8, 9.8, 3.8, 2.06, 0.7, 0.6, 0.2, -0.01, -1.7, -5.72, -10.36, -9.6, -7.5, -4.68, -2.96, -2.2, -2.1]  # in mikro Sekunden
dt = [-1 * dt_i * 10**-6 for dt_i in dt_mus]

I_0 = [U_i/R for U_i in U_B]

graph(f, I_0, xlabel=r"Frequenz $f$ in $Hz$", ylabel=r"Stromstärke in $A$", title=r"Amplitudenresonanzkurve")

p_hi = [2 * np.pi * f_i * dt_i for f_i, dt_i in zip(f, dt)]

graph(f, p_hi, xlabel=r"Frequenz $f$ in $Hz$", ylabel=r"Phasendifferenz in rad", title=r"Phasenresonanzkurve")




# 4. Versuchsteil

dt_4_mus = [0, 24, 50, 74, 100, 150, 200, 300, 400] # in mikro Sekunden
dt_4 = [dt_i_4 * 10**-6 for dt_i_4 in dt_4_mus]
R_4 = [1500]*len(dt_4)

U_R_mV = [1680, 880, 540, 380, 260, 160, 120, 60, 20] # in mV
U_R = [U_R_i * 10**-3 for U_R_i in U_R_mV]
ln_U_R = [np.log(U_i) for U_i in U_R]

graph(dt_4, ln_U_R, xlabel=r"Zeit $t$ in $s$", ylabel=r"$ln(U_R(t))$ in $V$",
      title=r"Exponetieller Abfall von $U_R(t)$", trendlinie=True)

b, a, s_b, s_a = wert_xy(dt_4, ln_U_R, name="ln(U_R(t))")

tau = -1/b
s_tau = -1/b**2 * s_b
C = tau/(1550)
s_C = 1/1550 * s_tau
print(f"tau = {tau: .3e}")
print(f"s_tau = {s_tau: .3e}")
print(f"C = {C: .3e}")
print(f"s_C = {s_C: .3e}")