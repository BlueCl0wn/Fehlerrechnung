from function import *
import numpy as np

# --- Quecksilber ---
# Nr.1
Minima_Ordnung = np.arange(4, 13)  # [4, 5, 6, 7, 8, 9, 10, 11, 12]

T_1 = 155
Delta_min_T_1 = np.array([4.78, 4.87, 4.94, 4.92, None, None, None, None, None])

T_2 = 190
Delta_min_T_2 = np.array([None, None, 4.69, 4.87, 4.81, 4.76, 4.89, 4.9, 4.96])

graph(Minima_Ordnung, ((Delta_min_T_1, rf"T = ${T_1}°C$"), (Delta_min_T_2, rf"T = ${T_2}°C$")), trendlinie=True)