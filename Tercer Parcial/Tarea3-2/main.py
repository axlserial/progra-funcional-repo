from functools import reduce
from pprint import pprint
import csv


def get_all_registers(f: str):
    with open(f) as csv_file:
        d = csv.reader(csv_file, delimiter=',')
        h = next(d)
        t: tuple[tuple[str, ...], ...] = tuple(map(tuple, d))

        return (h, t)


def get_only_winner_home_team(h: list[str], registers: tuple[tuple[str, ...],
                                                             ...]):
    return tuple(
        filter(lambda register: register[h.index("FTR")] == 'H', registers))


def get_all_total_goals(h: list[str], registers: tuple[tuple[str, ...], ...]):
    nombres = set(
        map(lambda register: register[h.index("HomeTeam")], registers))

    return list(
        map(
            lambda nombre: {
                'HomeTeam':
                nombre,
                'TotalFTHG':
                reduce(
                    lambda suma, register: suma + int(register[h.index("FTHG")]
                                                      ),
                    filter(
                        lambda register: register[h.index("HomeTeam")] ==
                        nombre, registers), 0),
                'TotalFTAG':
                reduce(
                    lambda suma, register: suma + int(register[h.index("FTAG")]
                                                      ),
                    filter(
                        lambda register: register[h.index("HomeTeam")] ==
                        nombre, registers), 0)
            }, nombres))


def print_goals_as_home_team(registers: list[dict]) -> None:
    equipos = list(
        map(
            lambda register: {
                'HomeTeam':
                register['HomeTeam'],
                'porcentaje':
                (register['TotalFTHG'] /
                 (register['TotalFTHG'] + register['TotalFTAG']) * 100)
            },
            filter(
                lambda register: register['TotalFTHG'] /
                (register['TotalFTHG'] + register['TotalFTAG']) > 0.85,
                registers)))

    # ordenar descendiente
    equipos = sorted(equipos,
                     key=lambda equipo: equipo['porcentaje'],
                     reverse=True)

    # imprimir HomeTeam y porcentaje de victorias como local
    for equipo in equipos:
        print(f"{equipo['HomeTeam']}: {equipo['porcentaje']:.2f}%")


def main():
    # 1. Leer el archivo soccer_df3.csv
    h, registers = get_all_registers('soccer_df3.csv')
    print("1:")
    pprint(registers[:20])
    # print("1:\n", registers[:50], end='\n\n\n')

    # 2. Obtener los equipos donde gano el equipo local
    registers = get_only_winner_home_team(h, registers)
    print("\n\n\n2:")
    pprint(registers[:20])
    # print("2:\n", registers[:50], end='\n\n\n')

    # 3. A partir del resultado anterior, obtener el resumen de los
    # goles de cada equipo como local  y los goles recibido de los equipos visitantes.
    registers = get_all_total_goals(h, registers)
    print("\n\n\n3:")
    pprint(registers[:20])
    # print("3:\n", registers[:50], end='\n\n\n')

    # 4.  A partir del resultado anterior, mostrar aquellos equipos que el 85% del total
    # de los goles hayan sido como locales, es decir, que a partir del total de los goles
    # anotado y recibos (100%), el 85% sean goles locales.
    print("\n\n\n4:")
    print_goals_as_home_team(registers)


if __name__ == "__main__":
    main()