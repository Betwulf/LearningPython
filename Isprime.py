from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def next_prime(start=3, end=100000000000000000):
    x = start
    yield x
    x = x + 1
    while x < end:
        while is_prime(x) is False:
            x = x + 1
        yield x
        x = x + 1



