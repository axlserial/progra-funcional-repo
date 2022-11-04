import csv
from pprint import pprint


# Lista de diccionarios con el nombre y la plataforma de los juegos
def first_comp(name_file: str):
    selected_keys = ["Name", "Platform"]

    with open(name_file) as csvfile:
        dict_games = []

        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        for game in games:
            iterator = zip(h, game)
            dict_games.append(
                {k: v
                 for k, v in iterator if k in selected_keys})

        return dict_games


# lista de diccionarios con el nombre y la plataforma de los juegos que sean del año 2009
def second_comp(name_file: str):
    selected_keys = ["Name", "Platform", "Year"]

    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        dict_games = [{k: v
                       for k, v in zip(h, game) if k in selected_keys}
                      for game in games
                      if game[h.index(selected_keys[2])] == "2009"]

        return dict_games

# Lista de diccionarios con todos los registros las columnas Name, Platform y Year donde Publisher es Sega
def third_comp(name_file: str):

    with open(name_file) as csvfile:
        columnas = ['Name','Platform','Year']
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)
        
        list_games =[{k : v for k,v in zip(h,game) if k in columnas} for game in games if game[h.index("Publisher")] == "Sega"]
        
    return list_games

# Diccionario de diccionarios donde la llave será la plataforma de los juegos cuyo Rank sea menos a 20 y el valor será un diccionario con el nombre del juego y el año
def fourth_comp(name_file: str):

    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)
        
        plataforms = [game[h.index("Platform")] for game in games if int(game[h.index("Rank")]) < 20]
        plataforms = list(set(plataforms))

        return plataforms



def run():
    f = './vgsales.csv'

    # pprint(first_comp(f)[:10])
    #pprint(second_comp(f)[:10])
    #pprint(third_comp(f)[:10])
    print(fourth_comp(f))

    


if __name__ == "__main__":
    run()