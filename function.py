import math
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


def wert_x(name: str, x: list) -> None:
    print(f"{name}:")
    x_mean = round(mean(x), 9)
    s_x_mean = round(get_s_x(x), 9)
    perc = round(s_x_mean/x_mean, 6)
    print(f" -  {name}_mean = {x_mean} +- {s_x_mean}    (+- {perc})")
    print()


def wert_xy(name: str, x: list, y: list) -> None:
    print(f"{name}:")
    b=round(get_b(x, y), 9)
    s_b = round(get_s_b(x, y), 9)
    b_perc = round(s_b/b, 6)

    a = round(get_a(x, y), 9)
    s_a = round(get_s_a(x, y), 9)
    a_perc = round(s_a/a, 6)
    print(f" -  b = {b} +- {s_b}  (+- {b_perc})")
    print(f" -  a = {a} +- {s_a}  (+- {a_perc})")
    print()