import csv


def get_all_registers(f: str) -> tuple:
    with open(f) as csv_file:
        d = csv.reader(csv_file, delimiter=',')
        h = next(d)
        t = tuple(tuple(r) for r in d)

    return (h, t)


def get_only_winner_home_team(h: list[str], registers: tuple) -> tuple:
    # return tuple(filter(lambda r: r[5] == 'H', registers))
    return tuple(filter(lambda r: r[h.index("FTR")] == 'H', registers))


def get_all_total_goals(h: list[str], registers: tuple) -> list[dict]:
    # nombres = set(map(lambda r: r[2], registers))
    nombres = set(map(lambda r: r[h.index("AwayTeam")], registers))

    # return [{
    #     'HomeTeam':
    #     nombre,
    #     'TotalFTHG':
    #     sum(
    #         map(lambda r: int(r[3]), filter(lambda r: r[2] == nombre,
    #                                         registers))),
    #     'TotalFTAG':
    #     sum(
    #         map(lambda r: int(r[4]), filter(lambda r: r[2] == nombre,
    #                                         registers))),
    # } for nombre in nombres]

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


def print_goals_as_home_team(h: list[str], registers: list[dict]) -> None:
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
    h, registers = get_all_registers('soccer_df3.csv')
    print(h)
    print("Ejercicio 2:\n", registers[:50], end='\n\n\n')

    # Imprimir ejercicio 3
    registers = get_only_winner_home_team(h, registers)
    print("Ejercicio 3:\n", registers[:50], end='\n\n\n')

    # Imprimir ejercicio 4
    registers = get_all_total_goals(h, registers)
    print("Ejercicio 4:\n", registers[:50], end='\n\n\n')

    # Imprimir ejercicio 5
    print("Ejercicio 5:")
    print_goals_as_home_team(h, registers)


if __name__ == "__main__":
    main()