from function import *

# Messwerte

# I(x)
x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
     36, 37, 38]
I_x_random = [11.3, 11.5, 11.8, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.2, 12.5, 13.0, 13.1, 13.3, 13.5, 14.0, 14.5,
              14.8, 15.0, 15.5, 16.0, 16.5, 17.0, 17.0, 16.5, 14.8, 12, 8, 4.5, 2.0, 1.0, 0.8, 0]
I_x = [i * (10 ** -12 / 39.3) for i in I_x_random]

# I(U_k)
U = [39.1, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10, 7, 4, 3, 2, 1, 0.9, 0.6, 0.3, 0]
I_U_random = [17.5, 18, 17, 17, 16.5, 17, 17, 17, 17, 16, 16, 15.5, 15, 14.5, 14, 13.5, 13, 13, 12.5, 12]

I_U = [i * (10 ** -12 / 39.3) for i in I_U_random]

graph(x, I_x, xlabel=r"$x$ in $mm$", ylabel=r"$I(x)$ in $A$", title=r"Bragg'sche Kurve")
plt.show()
graph(U, I_U, xlabel=r"$U$ in $V$", ylabel=r"$I(U)$ in $A$", title=r"Kammerkennlinie")
plt.show()

print(f"R = {0.32 * sqrt(5.3 ** 3)}")
