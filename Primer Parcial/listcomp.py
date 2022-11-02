import random


def run():
    x = random.randint(1, 100)
    print(x)

    students = ['Ana', 'Roberto', 'Enrique', 'Maria']

    # aleatorios = [random.randint(1, 100) for _ in range(1, 11)]
    # print(aleatorios)

    l = [[name, random.randint(1, 10)] for name in students]
    t = tuple([(name, random.randint(1, 10)) for name in students])
    d = {name: random.randint(1, 10) for name in students}
    c = {(name, random.randint(1, 10)) for name in students}

    print(l, t, d, c)


if __name__ == "__main__":
    run()