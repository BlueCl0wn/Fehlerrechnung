from function import *

n = [0, 8, 16, 24, 32, 40, 48, 56, 64]
range = [16, 38.6, 80, 133.5, 197, 268.9, 348.5, 435, 528]
ln_range = [np.log(i) for i in range]
energy_usage = [16, 36.74, 80, 174.04, 376.02, 818.36, 1770, 3810, 8210]
ln_energy_usage = [np.log(i) for i in energy_usage]

graph(n, ((range, "range"), (energy_usage, "energy_usage")))
graph(n, ((ln_range, "range"), (ln_energy_usage, "energy_usage")), trendlinie=True)
wert_xy(n, ln_range, name="ln_range")
