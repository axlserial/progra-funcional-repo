def pot(exp):
    return lambda base: base ** exp

def addn(n):
    def add(x):
        return x + n

    return add

def main():
    potencia = pot(2)
    print(potencia(2))

    a = [1.1, 2.2, 3.3, 4.4]
    d = map(addn(2), a)
    print(list(d))

if __name__ == "__main__":
    main()