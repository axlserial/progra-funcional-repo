# Ejercicios 2.1

from statistics import mean


def run():
    students = (
        ("Jairo", [4.5, 3.2, 6.1], 21, "H"),
        ("Yaneth", [5.4, 2.3, 1.6], 19, "M"),
        ("Carlos", [8.5, 8.2, 8.1], 23, "H"),
        ("Anabel", [9.5, 9.2, 8.1], 17, "M"),
        ("Roberto", [7.5, 7.2, 1.1], 16, "H"),
        ("Pepe", [7.1, 9.2, 8.1], 18, "H"),
        ("Carolina", [4.4, 9.0, 5.6], 19, "M"),
        ("Pedro", [6.6, 1.0, 2.3], 20, "H"),
        ("Ursula", [8.8, 9.0, 6.0], 18, "M"),
        ("León", [10.0, 6.0, 7.0], 17, "H"),
    )

    # Todos los estudiantes, elemento: nombre
    s1 = {s[0] for s in students}
    print("S1: ", s1, "\n")

    # Edad >= 18, elemento: tupla(nombre, edad)
    s2 = {(s[0], s[2]) for s in students if s[2] >= 18}
    print("S2: ", s2, "\n")

    # Edad < 18 y sexo 'M', elemento: tupla(nombre, sexo)
    s3 = {(s[0], s[3]) for s in students if s[2] < 18 and s[3] == 'M'}
    print("S3: ", s3, "\n")

    # Promedio >= 6, elemento: nombre
    s4 = {s[0] for s in students if mean(s[1]) >= 6.0}
    print("S4: ", s4, "\n")

    # alumnos reprobados
    not_aproved_students = s1.difference(s4)
    print("Not aproved students: ", not_aproved_students)


if __name__ == "__main__":
    run()