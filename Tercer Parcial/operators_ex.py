from operator import add, itemgetter, methodcaller
import math

a = [20, 30, 40]
b = range(3)

m = map(add, a, b)
# print(list(m))

# -----------------------
names: tuple[str, ...] = ("Axel", "Isaac", "Carlos", "Ana", "Javier", "Maria")
last_names: tuple[str, ...] = ("Garcia", "Gonzalez", "Sanchez", "Ruiz",
                               "Santoanella", "Pinto")
ages: tuple[int, ...] = (21, 22, 19, 25, 20, 18)

people = list(zip(names, last_names, ages))
# print(people, end="\n\n")
sorted_people = sorted(people, key=itemgetter(1))
# print(sorted_people, end="\n\n")

# ---------------------------
fruits = ['Banana', 'apple', 'Apricot', 'Clementine', 'avocado']
sorted_fruits = sorted(fruits, key=methodcaller('lower'), reverse=True)
# print(sorted_fruits)

# ---------------------------
k = [1, 4, -2, 16, -3, 36, -1]
sq = map(lambda x: math.sqrt(x), filter(lambda x: x >= 0, k))

# print(list(sq))


# -------------------------------
def same(s):
    print(f'Same: {s}')
    return s


def not_empty(s):
    if s:
        print(f'\nTrue: {s}')
        return True
    else:
        print('\nFalse')
        return False


letters = ['a', '', 'b', '', '', 'f']
m = map(same, filter(not_empty, letters))

# print('Start')
# for s in m:
#     print(f'Dentro ciclo: {s}')


# -----------------------------------
def format_person(first, last, age):
    return f'{last}, {first} - age {age}'


people_to_format = [('Arturo', 'Martinez', 25), ('Veronica', 'Juarez', 19),
                    ('Maria', 'Lopez', 26)]

print(*zip(*people_to_format))

# se generan 3 iterables, sobre el que format_person recibe cada uno
m_format = map(format_person, *zip(*people_to_format))
for p in m_format:
    print(p)