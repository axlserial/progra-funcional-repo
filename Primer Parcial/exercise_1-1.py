# Ejercicios 1.1

from statistics import mean


def run():
    students = (
        ("Jairo", [4.5, 3.2, 6.1], 21, "H"),
        ("Yaneth", [5.4, 2.3, 1.6], 19, "M"),
        ("Carlos", [8.5, 8.2, 8.1], 23, "H"),
        ("Anabel", [9.5, 9.2, 8.1], 17, "M"),
        ("Roberto", [7.5, 7.2, 71.1], 16, "H"),
    )

    solution = []

    # Todos los estudiantes con una edad mayor o igual a 18
    l1 = [s for s in students if s[2] >= 18]
    solution.append(l1)

    # Todos las estudiantes con una edad menor a 18 y sexo 'M'
    l2 = [s for s in students if s[2] < 18 and s[3] == "M"]
    solution.append(l2)

    # Todos los estudiantes con un promedio mayor o igual a 6.0
    l3 = [s for s in students if mean(s[1]) >= 6]
    solution.append(l3)

    for s in solution:
        print(s, "\n")


if __name__ == "__main__":
    run()
