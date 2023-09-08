import math
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

I = 5


def mean(l: list) -> int:
    return sum(l) / len(l)


def list_varianz(l: list) -> list:
    return [(i - mean(l)) ** 2 for i in l]


def sum_varianz(x):
    return sum(list_varianz(x))


def get_xx(x) -> int:
    xx = 0
    for i in range(len(x)):
        xx += x[i] ** 2
    return xx


def get_xy(x: list, y: list) -> int:
    xy = 0
    for i in range(len(x)):
        xy += x[i] * y[i]
    return xy


def sum_d_i2(x, y):
    b = get_b(x, y)
    a = get_a(x, y)

    d = 0
    for i in range(len(x)):
        d += (y[i] - b * x[i] - a) ** 2
    return d


def get_s_x(x: list) -> float:
    return math.sqrt(1 / (len(x) * (len(x) - 1)) * sum_varianz(x))


def get_b(x: list, y: list) -> float:
    xy = get_xy(x, y)
    xx = get_xx(x)
    return (xy - len(x) * mean(x) * mean(y)) / (xx - len(x) * mean(x) ** 2)


def get_a(x, y):
    return mean(y) - get_b(x, y) * mean(x)


def get_s_b(x, y):
    s = (1 / (len(x) - 2)) * ((sum_d_i2(x, y)) / (sum_varianz(x)))
    return math.sqrt(s)


def get_s_a(x, y):
    xx = get_xx(x)
    s = xx / len(x) * get_s_b(x, y) ** 2
    return math.sqrt(s)


def wert_x(x: list, name: str = None) -> tuple:
    x_mean = mean(x)
    s_x_mean = get_s_x(x)
    perc = s_x_mean / x_mean if x_mean != 0 else 9999999999
    if name is not None:
        print(f"{name: .3e}_mean = {x_mean: .3e} +- {s_x_mean: .3e}    (+- {perc: .3e})")
        print()
    return x_mean, s_x_mean


def wert_xy(x: list, y: list, name: str = None) -> tuple:
    if name is not None:
        print(f"{name}:")
    b = get_b(x, y)
    s_b = get_s_b(x, y)
    b_perc = s_b / b if b != 0 else 999999999999999

    a = get_a(x, y)
    s_a = get_s_a(x, y)
    a_perc = s_a / a if a != 0 else 999999999999999

    if name is not None:
        print(f" -  b = {b: .3e} +- {s_b: .3e}  (+- {b_perc: .3e})")
        print(f" -  a = {a: .3e} +- {s_a: .3e}  (+- {a_perc: .3e})")
        print()

    return b, a, s_b, s_a


def get_trendlinie(x: list, y: list):
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    return p(x)


def graph(x: list, y: list | tuple, trendlinie: bool = False, title: str = None, xlabel: str = None,
          ylabel: str = None, xlog=False, ylog=False):
    fig, ax = plt.subplots(layout='constrained')

    if type(y) == tuple:
        for y_i in y:
            ax.scatter(x, y_i[0], linewidths=1, label=y_i[1])
            if trendlinie:
                b, a, s_b, s_a = wert_xy(x, y_i[0])
                ax.plot(x, [(b * i + a) for i in x], color="grey", linestyle="dashed",
                        label=rf"{y_i[1]}: Trendlinie: {b: .2e}$*x + {a: .2e}$")
        ax.legend()

    else:
        ax.scatter(x, y, linewidths=2)
        if trendlinie:
            b, a, s_b, s_a = wert_xy(x, y)
            ax.plot(x, [(b * i + a) for i in x], color="grey", linestyle="dashed",
                    label=rf"Trendlinie: {b: .2e}$*x + {a: .2e}$")
            ax.legend()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if xlog:
        ax.set_xscale("log")
    if ylog:
        ax.set_yscale("log")
    ax.set_title(title)
    ax.grid()
    plt.show()
