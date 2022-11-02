from statistics import mean
import csv
import json


def part_one(name_file: str):
    with open(name_file) as csvfile:
        list_registers = []

        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        for register in registers:
            iterator = zip(h, register)
            list_registers.append({k: v for k, v in iterator})

        return list_registers


def part_two(name_file: list):
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


def part_three(name_file: list):
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


def part_four(name_file: list):
    selected_keys = ["CCA3", "World Population Percentage"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        list_registers = [(register[h.index(selected_keys[0])],
                           register[h.index(selected_keys[1])])
                          for register in registers
                          if float(register[h.index(selected_keys[1])]) >= 1.0]

        return list_registers


def part_five(name_file: list):
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


def part_six(name_file: list):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {(register[h.index(selected_keys[0])],
                          register[h.index(selected_keys[1])])
                         for register in registers}

        return set_registers


def part_seven(name_file: list):
    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {
            register[h.index("Continent")]
            for register in registers
        }

        return set_registers


def part_eight(name_file: list):
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


def part_nine(name_file: list):
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


def part_ten(name_file: list):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {(register[h.index(selected_keys[0])],
                          register[h.index(selected_keys[1])])
                         for register in registers
                         if register[h.index(selected_keys[1])] == "Oceania"}

        return set_registers


def part_eleven(name_file: list):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {(register[h.index(selected_keys[0])],
                          register[h.index(selected_keys[1])])
                         for register in registers
                         if register[h.index(selected_keys[1])] == "Europe"}

        return set_registers


def part_twelve(name_file: list):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {(register[h.index(selected_keys[0])],
                          register[h.index(selected_keys[1])])
                         for register in registers
                         if register[h.index(selected_keys[1])] == "Asia"}

        return set_registers


def part_thirteen(name_file: list):
    selected_keys = ["Country/Territory", "Continent"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        set_registers = {(register[h.index(selected_keys[0])],
                          register[h.index(selected_keys[1])])
                         for register in registers
                         if register[h.index(selected_keys[1])] == "Africa"}

        return set_registers


def part_fourteen(name_file: list):
    p11 = part_eleven(name_file)
    p12 = part_twelve(name_file)
    p13 = part_thirteen(name_file)

    return p11.union(p12, p13)


def part_fifteen(name_file: list):
    p8 = part_eight(name_file)
    p9 = part_nine(name_file)

    return p8.union(p9)


def part_sixteen(name_file: list):
    selected_keys = ["Country/Territory", "World Population Percentage"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        list_registers = {(register[h.index(selected_keys[0])],
                           register[h.index(selected_keys[1])])
                          for register in registers
                          if float(register[h.index(selected_keys[1])]) < 0.4}

        return list_registers


def part_seventeen(name_file: list):
    selected_keys = ["Country/Territory", "World Population Percentage"]

    with open(name_file) as csvfile:
        registers = csv.reader(csvfile, delimiter=',')
        h = next(registers)

        list_registers = {(register[h.index(selected_keys[0])],
                           register[h.index(selected_keys[1])])
                          for register in registers
                          if float(register[h.index(selected_keys[1])]) > 0.2}

        return list_registers


def part_eighteen(name_file: list):
    p16 = part_sixteen(name_file)
    p17 = part_seventeen(name_file)

    return p16.intersection(p17)


def part_nineteen(name_file: list):
    p16 = part_sixteen(name_file)
    p17 = part_seventeen(name_file)

    return p16.difference(p17)


def part_twenty(name_file: list):
    p16 = part_sixteen(name_file)
    p17 = part_seventeen(name_file)

    return p17.difference(p16)


if __name__ == "__main__":
    archive = './world_population.csv'

    # p1 = part_one(archive)
    # p2 = part_two(archive)
    # p3 = part_three(archive)
    # p4 = part_four(archive)
    # p5 = part_five(archive)
    # p6 = part_six(archive)
    # p7 = part_seven(archive)
    # p8 = part_eight(archive)
    # p9 = part_nine(archive)
    # p10 = part_ten(archive)
    # p11 = part_eleven(archive)
    # p12 = part_twelve(archive)
    # p13 = part_thirteen(archive)
    # p14 = part_fourteen(archive)
    # p15 = part_fifteen(archive)
    # p16 = part_sixteen(archive)
    # p17 = part_seventeen(archive)
    # p18 = part_eighteen(archive)
    # p19 = part_nineteen(archive)
    p20 = part_twenty(archive)

    print(p20)
    # print(json.dumps(p2[:10], indent=4))