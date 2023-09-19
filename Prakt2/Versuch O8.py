import numpy as np
from function import *

D_1 = 98.46  # *10**-3
D_2 = 592.46  # *10**-3
w_D1 = 282  # *10**-6
w_D2 = 474  # *10**-6

graph([D_1, D_2], [w_D1, w_D2], title="Bestimmung Divergenzwinkel und Ursprung", xlabel=r"$D$ in $mm$",
      ylabel="$w(D)$ in $\mu m$", trendlinie=True)

# ------- Teil 2.4
# b)
L = np.array([26, 28.5, 29.5, 31, 33])
W = np.array([70,63,15,33,20])
graph(L, W, title=r"$P_{HeNe}(L)$", xlabel=r"$L$ in $cm$", ylabel=r"$P_{HeNe}$ in $mW$")