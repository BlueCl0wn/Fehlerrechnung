import math

x_1 = [6.3, 6.6, 6.7, 6.8, 6.7, 6.5, 7.0, 6.5, 6.4, 6.9]
x_2 = [7.8, 7.9, 7.7, 6.6, 7.6, 7.8, 7.6, 7.6, 8.0, 8.0]

T_1 = [21.7, 24.3, 24.9, 25.8, 26.7, 27.5, 28.5, 29.2, 30.2, 30.9, 31.8, 32.7, 33.7, 34.5,
       35.4, 36.2, 37.1, 37.9, 38.7, 39.4, 40.3, 41.1, 41.9, 42.7, 43.4, 44.2, 44.9, 45.7, 46.4, 47.2, 47.8, 48.5, 49.3,
       50.0
       ]
T = [21.7, 24.3, 24.9, 25.8, 26.7, 27.5, 28.5]

t = [0, 1, 2, 3, 4, 5, 6]

U = [0.006, 0.088, 0.102, 0.157, 0.188, 0.219, 0.252,
     0.282, 0.314, 0.343, 0.376, 0.406, 0.443, 0.468, 0.502,
     0.530, 0.561, 0.591, 0.619, 0.649, 0.681, 0.711, 0.740,
     0.768, 0.798, 0.826, 0.852, 0.880, 0.907, 0.932, 0.959,
     0.981, 1.009, 1.036]


def mean(l: list) -> int:
    return sum(l) / len(l)


def list_varianz(l):
    return [(i - mean(l))**2 for i in l]


def sum_varianz(l):
    return sum(list_varianz(l))


def sum_d_i(x, y):
    d = 0
    b = get_b(x, y)
    a = get_a(x, y)
    for i in range(len(x)):
        d += (x[i] - b * x[i] - a) ** 2

    return d


def s_x(l: list) -> float:
    return math.sqrt(1 / (len(l) * (len(l) - 1)) * sum_varianz(l))


def get_b(x: list, y: list) -> float:
    xy = 0
    xx = 0
    for i in range(len(x)):
        xy += x[i] * y[i]
        xx += x[i] ** 2

    return (xy - len(x) * mean(x) * mean(y)) / (xx - len(x) * mean(x) ** 2)


def get_a(x, y):
    return mean(y) - get_b(x, y) * mean(x)


def s_b(x, y):
    s = 1 / (len(x) - 2) * (sum_d_i(x, y)) / (sum_varianz(x))

    return math.sqrt(s)


def s_a(x, y):
    xx = 0
    for i in range(len(x)):
        xx += x[i] ** 2

    s = xx / len(x) * s_b(x, y) ** 2
    return math.sqrt(s)


def calc(l: list) -> None:
    print(f"\ts_t={s_x(l)}")
    print(f"\tx_mean={mean(l)}")


if __name__ == "__main__":
    calc(x_1)
    calc(x_2)
    print(f"b = {get_b(t, T)}")
    print(f"s_b = {s_b(t, T)}")
    print(f"a = {get_a(t, T)}")
    print(f"s_a = {s_a(t, T)}")
