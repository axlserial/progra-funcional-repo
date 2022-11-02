import csv


def read_csv(name_file: str) -> list:
    with open(name_file) as csvfile:
        list_students = []

        students = csv.reader(csvfile, delimiter=',')
        h = next(students)

        for student in students:
            iterator = zip(h, student)
            list_students.append({k: v for k, v in iterator})

        return list_students


if __name__ == "__main__":
    l = read_csv('./data.csv')
    print(l)