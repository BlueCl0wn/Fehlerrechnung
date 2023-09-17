import numpy as np
from function import *

L = 39.9 * 10 ** -3  # in m, Länge der Vakuumzelle
s_L = 0.1 * 10 ** -3  # Messfehler der Länge der Vakuumzelle in meter
lambda_ = 632.8 * 10**-9  # Wellenlänge in m
dp = [100, 200, 300, 400, 500, 600, 650, 700, 750, 780]  # Druckunterschied in Pascal
p = 101300  # Druck in Pascal
m = [4, 8, 11, 14, 17, 20, 23, 25, 27, 29]  # m

b, a, s_b, s_a = wert_xy(dp, m)
dn_dp = b/(2*L/lambda_)
s_dn_dp = s_b/(2*s_L/lambda_)
print(f"dn_dp = {dn_dp} +- {s_dn_dp}")
n = 1+ p *dn_dp
s_n = 1 + p * s_dn_dp
print(f"n = {n} +- {s_n}")
