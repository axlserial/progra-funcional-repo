from timeit import default_timer as timer


def hanoi_recursivo(n: int, origen: str, destino: str, auxiliar: str):
    if n == 1:
        print(f"Mover disco de {origen} a {destino}")
    else:
        hanoi_recursivo(n - 1, origen, auxiliar, destino)
        hanoi_recursivo(1, origen, destino, auxiliar)
        hanoi_recursivo(n - 1, auxiliar, destino, origen)


def main():
    n = int(input("Ingrese la cantidad de discos: "))

    # Medida de tiempo
    inicio = timer()
    hanoi_recursivo(n, "A", "B", "C")
    final = timer()

    print(f"\nTiempo de ejecución: {final - inicio} segundos")


if __name__ == "__main__":
    main()