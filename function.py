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


def s_x(x: list) -> float:
    return math.sqrt(1 / (len(x) * (len(x) - 1)) * sum_varianz(x))


def get_b(x: list, y: list) -> float:
    xy = get_xy(x, y)
    xx = get_xx(x)
    return (xy - len(x) * mean(x) * mean(y)) / (xx - len(x) * mean(x) ** 2)


def get_a(x, y):
    return mean(y) - get_b(x, y) * mean(x)


def s_b(x, y):
    s = (1 / (len(x) - 2)) * ((sum_d_i2(x, y)) / (sum_varianz(x)))
    return math.sqrt(s)


def s_a(x, y):
    xx = get_xx(x)
    s = xx / len(x) * s_b(x, y) ** 2
    return math.sqrt(s)


def wert_x(name: str, x: list) -> None:
    print(f"{name}:")
    print(f" -  {name}_mean = {round(mean(x), 9)}")
    print(f" -  s_{name} = {round(s_x(x), 9)}")


def wert_xy(name: str, x: list, y: list) -> None:
    print(f"{name}:")
    print(f" -  b = {round(get_b(x, y), 9)} +- {round(s_b(x, y), 9)}")
    print(f" -  a = {round(get_a(x, y), 9)} +- {round(s_a(x, y), 9)}")
    print()