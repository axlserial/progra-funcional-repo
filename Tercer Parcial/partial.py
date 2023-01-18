def maxn(n):

    def f(x):
        return max(n, x)

    return f


max0 = maxn(0)
print(max0(3))
print(max0(-1))

m = map(maxn(3), [1, 2, 3, 4, 5])
print(list(m))


def quad(a, b, c, x):
    return a * x * x + b * x + c


def quad_abc(a, b, c):

    def f(x):
        return quad(a, b, c, x)

    return f


my_quad = quad_abc(1, -3, 2)
print(my_quad(0))
print(my_quad(1))
print(my_quad(2))

# para no definir closures
from functools import partial

max_zero = partial(max, 0)
print(max_zero(3))
print(max_zero(-1))

m = map(partial(max, 0), [1, 2, -3, 4, -5])

quad3 = partial(quad, 1, -3, 2)
print(quad3(0))
print(quad3(1))
print(quad3(3))

quad2 = partial(quad, 1, -3)
print(quad2(2, 0))
print(quad2(2, 1))
print(quad2(2, 3))