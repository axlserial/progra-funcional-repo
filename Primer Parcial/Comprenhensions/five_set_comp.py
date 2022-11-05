import csv
from pprint import pprint


# Conjunto de los nombres de las plataformas
def first_set_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {game[h.index("Platform")] for game in games}

        return set_games


# Conjunto de todos los registros que sus elementos
# sean la tupla "Name" y "Global_Sales" de los juegos
def second_set_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {(game[h.index("Name")], game[h.index("Global_Sales")])
                     for game in games}

        return set_games


# Conjunto de todos los registros que sus elementos
# sean la tupla "Name" y "NA_Sales" de los juegos
# que hayan vendido más de 5.0 millones en NA
def third_set_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {(game[h.index("Name")], game[h.index("NA_Sales")])
                     for game in games
                     if float(game[h.index("NA_Sales")]) > 5.0}

        return set_games

# Conjunto de tuplas con las columnas: Name y Global_Sales
# de juegos que su plublisher sea Sega, su plataforma 3DS
# y que sean de Sonic.

def fourth_set_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h =  next(games)

        set_games = {(game[h.index("Name")], game[h.index("Global_Sales")]) 
                     for game in games if game[h.index("Publisher")] == "Sega" and 
                     game[h.index("Platform")] == "3DS" and game[h.index("Name")].find("Sonic") != -1}

        return set_games

# Conjunto de los nombres de los Publisher's que poseen juegos
# del genero de Platform cuyo lanzamiento esta entre los años 2013 y 2016.
def five_set_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {game[h.index("Publisher")] for game in games 
                     if game[h.index("Year")] >= '2013' and game[h.index("Year")] <= '2016' 
                     and game[h.index("Genre")] == "Platform"}

        return set_games


# Conjunto de tuplas con las columnas: Name y Global_Sales
# de juegos que su plublisher sea Sega, su plataforma 3DS.
def conjunto_p(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h =  next(games)

        set_games = {(game[h.index("Name")], game[h.index("Global_Sales")]) 
                     for game in games if game[h.index("Publisher")] == "Sega" and 
                     game[h.index("Platform")] == "3DS"}

        return set_games

# Conjunto de los nombres de las plataformas que tengan juegos del genero Action
def conjunto_q(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {game[h.index("Platform")] for game in games if game[h.index("Genre")] == "Action"}

        return set_games

# Conjunto de todos los registros que sus elementos
# sean la tupla "Name" y "NA_Sales" de los juegos
# que hayan vendido menos de 2.0 millones en NA
def conjunto_u(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {(game[h.index("Name")], game[h.index("NA_Sales")])
                     for game in games
                     if float(game[h.index("NA_Sales")]) > 4.0}

        return set_games

def run():
    f = './vgsales.csv'

    # pprint(first_comp(f))
    # pprint(second_comp(f))
    # pprint(third_comp(f))
    # pprint(five_comp(f))

    #Operaciones con conjuntos

    # Obtener el conjuntos de las tuplas donde los juegos sean de la Plataforma 3DS, su Publisher sea Sega
    # y que su nombre no contenga la palabra Sonic. 
    A = conjunto_p(f) - fourth_set_comp(f)
    #pprint(A)

    # Obtener el conjunto de los Publisher's que poseen juegos del genero de Platform cuyo 
    # lanzamiento esta entre los años 2013 y 2016 y los las plataformas.

    B = five_set_comp(f).union(first_set_comp(f))
    #print(B)

    # Obtener el conjunto de tuplas que pertenezcan tanto en el conjunto A y el resultado de la llamada
    # a la función second_set_comp(f) 
    C = A.intersection(second_set_comp(f))
    #print(C)

    # Obtener el conjunto complemento de las plataformas que pertenecen a las llamadas de las funciones
    # first_set_comp(f) y conjunto_q(f)
    D = conjunto_q(f).symmetric_difference(first_set_comp(f))
    #print(D)

    # Obtener el conjunto de tuplas donde las ventas de los juegos que se encuentren en el conjunto 
    # de la llamada a la función third_set_comp(f) y en el conjunto de la llamda a la función
    # conjunto_u(f)

    E = third_set_comp(f) & conjunto_u(f)
    #print(E)

    
    
    

if __name__ == "__main__":
    run()