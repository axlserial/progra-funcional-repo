names = ("Axel", "Isaac", "Carlos", "Ana", "Javier", "Maria")
last_names = ("Garcia", "Gonzalez", "Sanchez", "Ruiz", "Santoanella", "Pinto")
ages = (21, 22, 19, 25, 20, 18)

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