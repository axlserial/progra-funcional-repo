import csv
from pprint import pprint


# Conjunto de los nombres de las plataformas
def first_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {game[h.index("Platform")] for game in games}

        return set_games


# Conjunto de todos los registros que sus elementos
# sean la tupla "Name" y "Global_Sales" de los juegos
def second_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {(game[h.index("Name")], game[h.index("Global_Sales")])
                     for game in games}

        return set_games


# Conjunto de todos los registros que sus elementos
# sean la tupla "Name" y "NA_Sales" de los juegos
# que hayan vendido más de 5.0 millones en NA
def third_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {(game[h.index("Name")], game[h.index("NA_Sales")])
                     for game in games
                     if float(game[h.index("NA_Sales")]) > 5.0}

        return set_games


def run():
    f = './vgsales.csv'

    # pprint(first_comp(f))
    pprint(second_comp(f))
    # pprint(third_comp(f))


if __name__ == "__main__":
    run()