from statistics import mean

h = ["name", "grades", "age", "sex", "grades_mean"]


def filter_closure(filter_index: int, filter_value):

    def filter(t: tuple) -> tuple:
        return tuple([e for e in t if e[filter_index] == filter_value])

    return filter


def mean_closure_all():

    def mean_calc(t: tuple) -> tuple:
        return tuple(map(lambda x: (*x, mean(x[h.index("grades")])), t))

    return mean_calc


def mean_closure_one():

    def mean_calc(t: tuple) -> tuple:
        return (*t, mean(t[h.index("grades")]))

    return mean_calc


def sort_closure(sort_index: int, asc=True):

    def sort_func(t: tuple) -> tuple:
        return tuple(sorted(t, key=lambda x: x[sort_index], reverse=not asc))

    return sort_func


def main():
    students = (
        ("Jairo", [4.5, 3.2, 6.1], 21, "H"),
        ("Yaneth", [5.4, 2.3, 1.6], 19, "M"),
        ("Carlos", [8.5, 8.2, 8.1], 23, "H"),
        ("Anabel", [9.5, 9.2, 8.1], 17, "M"),
        ("Roberto", [7.5, 7.2, 7.1], 16, "H"),
    )

    filter_func = filter_closure(h.index("sex"), "H")
    students_filtered = filter_func(students)
    print(f"\nStudents filtered: {students_filtered}\n")

    # mean_func = mean_closure_all()
    # students_mean = mean_func(students_filtered)
    # print(f"Students mean: {students_mean}\n")
    
    students_mean = tuple(map(mean_closure_one(), students_filtered))
    print(f"Students mean: {students_mean}\n")

    sort_func = sort_closure(h.index("grades_mean"))
    students_sorted = sort_func(students_mean)
    print(f"Students sorted: {students_sorted}")


if __name__ == "__main__":
    main()