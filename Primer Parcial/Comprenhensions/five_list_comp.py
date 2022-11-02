import csv
from pprint import pprint


# Lista con los nombres de los juegos
def first_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        list_games = [game[h.index("Name")] for game in games]

        return list_games


# Lista de tuplas con el nombre y el año de los juegos
def second_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        list_games = [(game[h.index("Name")], game[h.index("Year")])
                      for game in games]

        return list_games


# Lista de tuplas con el nombre, el año y la plataforma de los juegos
def third_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        list_games = [(game[h.index("Name")], game[h.index("Year")],
                       game[h.index("Platform")]) for game in games]

        return list_games


def run():
    f = './vgsales.csv'

    # pprint(first_comp(f)[:10])
    # pprint(second_comp(f)[:10])
    pprint(third_comp(f)[:10])


if __name__ == "__main__":
    run()