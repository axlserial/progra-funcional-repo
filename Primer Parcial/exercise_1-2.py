# Ejercicios 1.2

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

    # Todos los estudiantes
    d1 = {
        s[0]: {
            "calificaciones": s[1],
            "edad": s[2],
            "sexo": s[3]
        }
        for s in students
    }
    solution.append(d1)

    # Todos los estudiantes con una edad mayor o igual a 18
    d2 = {
        s[0]: {
            "calificaciones": s[1],
            "edad": s[2],
            "sexo": s[3]
        }
        for s in students if s[2] >= 18
    }
    solution.append(d2)

    # Todos las estudiantes con una edad menor a 18 y sexo 'M'
    d3 = {
        s[0]: {
            "calificaciones": s[1],
            "edad": s[2],
            "sexo": s[3]
        }
        for s in students if s[2] < 18 and s[3] == "M"
    }
    solution.append(d3)

    # Todos los estudiantes con un promedio mayor o igual a 6.0
    d4 = {
        s[0]: {
            "calificaciones": s[1],
            "edad": s[2],
            "sexo": s[3]
        }
        for s in students if mean(s[1]) >= 6
    }
    solution.append(d4)

    for s in solution:
        print(s, "\n")


if __name__ == "__main__":
    run()
