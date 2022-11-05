import csv
from pprint import pprint
from statistics import mean


# Diccionario con el 'Name' del juego como clave y la 'Platform'
# del juego como valor.
def first_dict_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        dict_games = {
            game[h.index("Name")]: game[h.index("Platform")]
            for game in games
        }

        return dict_games


# Diccionario con el 'Name' del juego como clave y la 'Platform'
# del juego como valor que sean del año 2009.
def second_dict_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        dict_games = {
            game[h.index("Name")]: game[h.index("Platform")]
            for game in games if game[h.index("Year")] == "2009"
        }

        return dict_games


# Diccionario con todos los registros que su 'Publisher' sea Sega
def third_dict_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        dict_games = {
            game[h.index("Name")]: {
                "Platform": game[h.index("Platform")],
                "Year": game[h.index("Year")],
                "Genre": game[h.index("Genre")],
                "Publisher": game[h.index("Publisher")]
            }
            for game in games if game[h.index("Publisher")] == "Sega"
        }

        return dict_games


# Diccionario que tiene el 'Name' del juego como clave
# y sus datos como valor y que 'Rank' sea mayor a 10 y menor a 20
def fourth_dict_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        dict_games = {
            game[h.index("Name")]: {
                "Rank": game[h.index("Rank")],
                "Platform": game[h.index("Platform")],
                "Year": game[h.index("Year")],
                "Genre": game[h.index("Genre")],
                "Publisher": game[h.index("Publisher")]
            }
            for game in games if int(game[h.index("Rank")]) > 10
            and int(game[h.index("Rank")]) < 20
        }

        return dict_games


# Diccioanrio con el 'Name' del juego como clave 
# y un promedio de sus Sales como valor
def fifth_dict_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        dict_games = {
            game[h.index("Name")]: mean(
                [float(game[h.index("NA_Sales")]),
                 float(game[h.index("EU_Sales")]),
                 float(game[h.index("JP_Sales")]),
                 float(game[h.index("Other_Sales")])])
            for game in games
        }

        return dict_games

def run():
    f = './vgsales.csv'

    # pprint(first_comp(f))
    # pprint(second_dict_comp(f))
    # pprint(third_dict_comp(f))
    # pprint(fourth_dict_comp(f))
    pprint(fifth_dict_comp(f))
    #pprint(third_comp(f)[:10])
    # print(fourth_comp(f))


if __name__ == "__main__":
    run()