import csv

h = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']


def get_all_registers(f: str) -> tuple:
    with open(f) as csv_file:
        d = csv.reader(csv_file, delimiter=',')
        next(d)  # saltar encabezado
        t = [tuple(r) for r in d]

    return tuple(t)


def select_fieldn(field: str):

    def select_field(r: tuple):
        return r[h.index(field)]

    return select_field


def main():
    registers = get_all_registers('soccer_df3.csv')

    # 2
    select_func = select_fieldn('FTR')
    registers = tuple([r for r in registers if select_func(r) == 'H'])
    print("Home team:", registers[:10])




if __name__ == "__main__":
    main()