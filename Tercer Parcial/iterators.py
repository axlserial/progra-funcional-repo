from math import sqrt


def iterable_func():
    # iterable
    numbers = [1, 2, 3, 4, 5]

    # iterador
    numbers_iter = iter(numbers)

    # use of next
    try:
        while True:
            print(next(numbers_iter), end=" ")

    except StopIteration:
        print("\nTerminado")

    # over map realizing
    temperatures = [12.11, 33.44, 29.78, 40.91]
    b = map(round, temperatures)
    print(list(b))

    # int value of chars list
    chars = [97, 93, 45, 64, 65]
    c = map(chr, chars)
    print(''.join(c))


def unpacking():
    # unpacking
    def mult(x, y, z):
        return x * y * z

    t = [3, 5, 7]
    print(mult(*t))


def euclidian_dist():
    # euclidian distance func
    def distance(a: tuple, b: tuple):
        return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

    point_one = ((3, 5), (4, 5), (3, 9))
    point_two = ((6, 9), (2, 9), (0, 3))

    res = map(lambda x: distance(*x), list(zip(point_one, point_two)))
    print(list(res))


def main():
    euclidian_dist()


if __name__ == "__main__":
    main()