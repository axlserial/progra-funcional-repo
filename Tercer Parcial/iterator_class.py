from math import factorial, exp


class Taylor():

    def __init__(self, x: int) -> None:
        self.sum: float = 1
        self.n: int = 1
        self.x = x

    def __iter__(self):
        return self

    def __next__(self):
        result = self.sum
        self.sum += (1 / factorial(self.n)) * self.x**self.n
        self.n += 1

        return result


def main():
    x = int(input("Ingresa x: "))
    val = exp(x)
    for i in Taylor(x):
        print(i)

        if abs(val - i) < 0.00001:
            break


if __name__ == "__main__":
    main()