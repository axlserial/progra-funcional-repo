names: tuple[str, ...] = ("Axel", "Isaac", "Carlos", "Ana", "Javier", "Maria")
last_names: tuple[str, ...] = ("Garcia", "Gonzalez", "Sanchez", "Ruiz",
                               "Santoanella", "Pinto")
ages: tuple[int, ...] = (21, 22, 19, 25, 20, 18)

# asignar un indice a cada elemento
for i, name in enumerate(names, start=1):
    print(f'{i}. {name}')

# Empaqueta para iterar
for name, last_name, age in zip(names, last_names, ages):
    print(f'{name} {last_name} - {age} years old')

# Como regresar a su valor orginal un paquete (desempaquetado)
a = (10, 11, 12, 13, 14, 15)
b = (20, 21, 22, 23, 24, 25)
c = (30, 31, 32, 33, 34, 35)

z = zip(a, b, c)
restored = zip(*z)
print(list(restored))

# filter
a = [3, 2, 7, 6, 9, 9, 8]
f = filter(lambda x: x > 7, a)
# print(list(f))
for i in f:
    print(i)

# other filter example, colores
colors = ['red', '', 'green', '', 'blue']
for color in filter(len, colors):
    print(color)


# map
def square(x):
    print(f'Num: {x}')
    return x * x


numbers = [2, 5, 6]
m = map(square, numbers)

for number in m:
    print(number)

# reversed
nums_rev = reversed(numbers[:])
print(list(nums_rev))

for i in reversed(range(10)):
    print(i)

dates = [
    '2019/09/09', '2009/01/09', '2010/03/29', '2000/07/01', '2022/12/12',
    '2018/09/09', '2015/09/09', '2010/09/09', '2000/06/02', '2022/04/22',
    '2017/09/09', '2022/11/25', '2010/07/07', '2000/05/03', '2022/05/15',
    '2016/09/30'
]

# sorted_dates = sorted(sorted(dates, key=lambda x: x[5:7]),
#                       key=lambda x: x[0:4])

sorted_dates = [
    sorted(tuple(filter(lambda x: x[0:4] == filtro, dates)),
           key=lambda x: x[5:7])
    for filtro in set(map(lambda x: x[0:4], dates))
]

print(sorted_dates)
