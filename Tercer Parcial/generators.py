import math


def generator_alphabet():

    def alphabet():
        for c in 'abcd':
            yield c

    for x in alphabet():
        print(x)

    g = alphabet()

    x = next(g)
    print(f'- {x}')

    x = next(g)
    print(f'- {x}')

    x = next(g)
    print(f'- {x}')

    x = next(g)
    print(f'- {x}')


# generador que produce un iterable
def generator_fibo():

    def fibonacci():
        c = 0
        n = 1
        while (True):
            yield c
            c, n = n, c + n

    for i in fibonacci():
        print(i)
        if (i > 100):
            break


def generator_identity():

    def identity(it):
        for x in it:
            yield x

    for i in identity(range(4)):
        print(i)


def generator_chain():

    def chain(it1, it2):
        for x in it1:
            yield x

        for x in it2:
            yield x

    for i in chain(range(4), reversed(range(3))):
        print(i)


# generators comprehensions

# crea un generador que no ocupa memoria hasta ser solicitado
a = (str(i) for i in range(100))

# filter map
l = [-1, 2, 7, 4, -6, 9, -3]
m = map(math.sqrt, filter(lambda x: x >= 0, l))
g = (math.sqrt(x) for x in l if x >= 0)


def main():
    pass


if __name__ == "__main__":
    main()