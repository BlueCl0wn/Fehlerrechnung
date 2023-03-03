from function import *
n = [12, 20, 24, 22]
c = [0.133, 0.123, 0.103, 0.0725]

def x(n, c) -> list:
    return [(2*n_i)/(c_i) for n_i, c_i in zip(n, c)]

x_list = x(n, c) # x Werte berechnet nach 7.6 zum plotten

y_0 = [80, 160, 240, 320] # Spaltbreite in mikrometer
y = [round(i*10**-6, 15) for i in y_0] # Spaltbreite in Meterns

wert_xy("lambda", x_list, y)