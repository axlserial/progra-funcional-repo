from statistics import mean
from pprint import pprint
import csv


def part_one(name_file: str):
    with open(name_file) as csvfile:
        list_registers = []

        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        for register in registers:
            iterator = zip(h, register)
            list_registers.append({k: v for k, v in iterator})

        return list_registers


def part_two(name_file: str):
    population_keys = [
        '2022 Population', '2020 Population', '2015 Population',
        '2010 Population', '2000 Population', '1990 Population',
        '1980 Population', '1970 Population'
    ]

    with open(name_file) as csvfile:
        list_registers = []

        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        for register in registers:
            population_iterator = zip(h, register)
            population = [
                v for k, v in population_iterator if k in population_keys
            ]

            rest_iterator = zip(h, register)
            list_registers.append(
                {k: v
                 for k, v in rest_iterator if k not in population_keys})

            list_registers[-1]['Population'] = population

        return list_registers


def part_three(name_file: str):
    selected_keys = ["Country/Territory", "2022 Population"]

    with open(name_file) as csvfile:
        list_registers = []

        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        for register in registers:
            iterator = zip(h, register)
            list_registers.append(
                {k: v
                 for k, v in iterator if k in selected_keys})

        return list_registers


def part_four(name_file: str):
    selected_keys = ["CCA3", "World Population Percentage"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        list_registers = [(register[h.index(selected_keys[0])],
                           register[h.index(selected_keys[1])])
                          for register in registers
                          if float(register[h.index(selected_keys[1])]) >= 1.0]

        return list_registers


def part_five(name_file: str):
    population_keys = [
        '2022 Population', '2020 Population', '2015 Population',
        '2010 Population', '2000 Population', '1990 Population',
        '1980 Population', '1970 Population'
    ]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        list_registers = [
            (register[h.index("CCA3")],
             mean([int(register[h.index(k)]) for k in population_keys]))
            for register in registers
        ]

        return list_registers


def part_six(name_file: str):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {(register[h.index(selected_keys[0])],
                          register[h.index(selected_keys[1])])
                         for register in registers}

        return set_registers


def part_seven(name_file: str):
    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {
            register[h.index("Continent")]
            for register in registers
        }

        return set_registers


def part_eight(name_file: str):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {
            (register[h.index(selected_keys[0])],
             register[h.index(selected_keys[1])])
            for register in registers
            if register[h.index(selected_keys[1])] == "North America"
        }

        return set_registers


def part_nine(name_file: str):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {
            (register[h.index(selected_keys[0])],
             register[h.index(selected_keys[1])])
            for register in registers
            if register[h.index(selected_keys[1])] == "South America"
        }

        return set_registers


def part_ten(name_file: str):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {(register[h.index(selected_keys[0])],
                          register[h.index(selected_keys[1])])
                         for register in registers
                         if register[h.index(selected_keys[1])] == "Oceania"}

        return set_registers


def part_eleven(name_file: str):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {(register[h.index(selected_keys[0])],
                          register[h.index(selected_keys[1])])
                         for register in registers
                         if register[h.index(selected_keys[1])] == "Europe"}

        return set_registers


def part_twelve(name_file: str):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {(register[h.index(selected_keys[0])],
                          register[h.index(selected_keys[1])])
                         for register in registers
                         if register[h.index(selected_keys[1])] == "Asia"}

        return set_registers


def part_thirteen(name_file: str):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {(register[h.index(selected_keys[0])],
                          register[h.index(selected_keys[1])])
                         for register in registers
                         if register[h.index(selected_keys[1])] == "Africa"}

        return set_registers


def part_fourteen(name_file: str):
    p11 = part_eleven(name_file)
    p12 = part_twelve(name_file)
    p13 = part_thirteen(name_file)

    return p11.union(p12, p13)


def part_fifteen(name_file: str):
    p8 = part_eight(name_file)
    p9 = part_nine(name_file)

    return p8.union(p9)


def part_sixteen(name_file: str):
    selected_keys = ["Country/Territory", "World Population Percentage"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        list_registers = {(register[h.index(selected_keys[0])],
                           register[h.index(selected_keys[1])])
                          for register in registers
                          if float(register[h.index(selected_keys[1])]) < 0.4}

        return list_registers


def part_seventeen(name_file: str):
    selected_keys = ["Country/Territory", "World Population Percentage"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        list_registers = {(register[h.index(selected_keys[0])],
                           register[h.index(selected_keys[1])])
                          for register in registers
                          if float(register[h.index(selected_keys[1])]) > 0.2}

        return list_registers


def part_eighteen(name_file: str):
    p16 = part_sixteen(name_file)
    p17 = part_seventeen(name_file)

    return p16.intersection(p17)


def part_nineteen(name_file: str):
    p16 = part_sixteen(name_file)
    p17 = part_seventeen(name_file)

    return p16.difference(p17)


def part_twenty(name_file: str):
    p16 = part_sixteen(name_file)
    p17 = part_seventeen(name_file)

    return p17.difference(p16)


if __name__ == "__main__":
    archive = './world_population.csv'

    print("Impresión limitada a cierto número de elementos\n")

    print("Ejercicio 1.")
    pprint(part_one(archive)[:1])

    print("\nEjercicio 2.")
    pprint(part_two(archive)[:1])

    print("\nEjercicio 3.")
    pprint(part_three(archive)[:10])

    print("\nEjercicio 4.")
    part_four(archive)

    print("\nEjercicio 5.")
    pprint(part_five(archive)[:10])

    print("\nEjercicio 6.")
    pprint(set(list(part_six(archive))[:10]))

    print("\nEjercicio 7.")
    part_seven(archive)

    print("\nEjercicio 8.")
    pprint(set(list(part_eight(archive))[:10]))

    print("\nEjercicio 9.")
    pprint(set(list(part_nine(archive))[:10]))

    print("\nEjercicio 10.")
    pprint(set(list(part_ten(archive))[:10]))

    print("\nEjercicio 11.")
    pprint(set(list(part_eleven(archive))[:10]))

    print("\nEjercicio 12.")
    pprint(set(list(part_twelve(archive))[:10]))

    print("\nEjercicio 13.")
    pprint(set(list(part_thirteen(archive))[:10]))

    print("\nEjercicio 14.")
    pprint(set(list(part_fourteen(archive))[:10]))

    print("\nEjercicio 15.")
    pprint(set(list(part_fifteen(archive))[:10]))

    print("\nEjercicio 16.")
    pprint(set(list(part_sixteen(archive))[:10]))

    print("\nEjercicio 17.")
    pprint(set(list(part_seventeen(archive))[:10]))

    print("\nEjercicio 18.")
    part_eighteen(archive)

    print("\nEjercicio 19.")
    pprint(set(list(part_nineteen(archive))[:10]))

    print("\nEjercicio 20.")
    pprint(set(list(part_twenty(archive))[:10]))