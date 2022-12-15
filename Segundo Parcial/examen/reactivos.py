import csv


def get_all_registers(f: str) -> tuple:
    with open(f) as csv_file:
        d = csv.reader(csv_file, delimiter=',')
        next(d)  # saltar encabezado
        t = [tuple(r) for r in d]

    return tuple(t)


def get_only_winner_home_team(registers: tuple) -> tuple:
    return tuple(filter(lambda r: r[5] == 'H', registers))


def get_all_total_goals(registers: tuple) -> list[dict]:
    nombres = set(map(lambda r: r[2], registers))

    return [{
        'HomeTeam':
        nombre,
        'TotalFTHG':
        sum(
            map(lambda r: int(r[3]), filter(lambda r: r[2] == nombre,
                                            registers))),
        'TotalFTAG':
        sum(
            map(lambda r: int(r[4]), filter(lambda r: r[2] == nombre,
                                            registers))),
    } for nombre in nombres]


def print_goals_as_home_team(registers: list[dict]) -> None:
    equipos = list(
        map(
            lambda e: {
                'HomeTeam':
                e['HomeTeam'],
                'porcentaje': (e['TotalFTHG'] /
                               (e['TotalFTHG'] + e['TotalFTAG']) * 100)
            },
            filter(
                lambda r: r['TotalFTHG'] /
                (r['TotalFTHG'] + r['TotalFTAG']) > 0.85, registers)))

    # ordenar descendiente
    equipos.sort(key=lambda e: e['porcentaje'], reverse=True)

    # imprimir HomeTeam y porcentaje de victorias como local
    for equipo in equipos:
        print(f"{equipo['HomeTeam']}: {equipo['porcentaje']:.2f}%")


def main():
    # Imprimir ejercicio 2
    registers = get_all_registers('soccer_df3.csv')
    print("Ejercicio 2:\n", registers[:50], end='\n\n\n')

    # Imprimir ejercicio 3
    registers = get_only_winner_home_team(registers)
    print("Ejercicio 3:\n", registers[:50], end='\n\n\n')

    # Imprimir ejercicio 4
    registers = get_all_total_goals(registers)
    print("Ejercicio 4:\n", registers[:50], end='\n\n\n')

    # Imprimir ejercicio 5
    print("Ejercicio 5:")
    print_goals_as_home_team(registers)


if __name__ == "__main__":
    main()