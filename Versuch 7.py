from function import *

# 1. Beugung am Spalt -------------------------
# 1.)
print("1.1.)")

# l : lambda
l = [517.30844, 574.095682, 600.9334889, 615.25405749]
wert_x(l, name="lambda", print_info=True)

# 2.)
print("1.2.)")
print("Bestimme Lambda und Y_0 mittels linearer Regression\n"
      "b = lambda\n"
      "a = y_0")
n = [12, 20, 24, 22]  # n Grad
c = [0.133, 0.123, 0.103, 0.0725]

# 2.)

def x(n, c) -> list:
    """
    x-Achsenwerte nach Gleichung 7.6
    :param n:
    :param c:
    :return:
    """
    return [(2 * n_i) / (c_i) for n_i, c_i in zip(n, c)]


x_list = x(n,
           c)  # x Werte berechnet nach 7.6 zum plotten

print("Die Werte für x sind: x=", x_list)


y_mikrom = [80, 160, 240, 320]  # Spaltbreite in mikrometer
y_meter = [round(i * 10 ** -6, 15) for i in y_mikrom]  # Spaltbreite in Meterns

wert_xy( x_list, y_meter, name="lambda", print_info=True)


lambd, y_0 = wert_xy(x_list, y_mikrom, name="lambda")

graph(x_list, y_mikrom, trendlinie=True, title="Test", xlabel=r"$x_i$ in $1/\mu m$", ylabel=r"$y_{i}$ in $\mu m$")
