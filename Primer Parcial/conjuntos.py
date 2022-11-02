# Construcción
fruits = {'apple', 'banana', 'cherry', 'orange', 'pear'}
numbers = {1, 5, 7, 9, 3}
things = {'abc', 34, True, 40, 'male'}

# Tamaño de un conjunto
print(f"Tamaño de fruits: {len(fruits)}\n")

# ciclos con conjuntos
for fruit in fruits:
    print(fruit)

# verificar existencia de un elemento
print('banana' in fruits)

# agregar un elemento
fruits.add("orange")

# agregar con update()
tropical = {'pineapple', 'mango', 'papaya'}
fruits.update(tropical)

# agregar iterable
list_of_fruits = ['kiwi', 'orange']
fruits.update(list_of_fruits)

# eliminar elemento con
# remove()
fruits.remove('banana')

# discard()
fruits.discard('banana')

# eliminar el ultimo elemento
fruits.pop()

# vaciar canjunto
fruits.clear()

# eliminar conjunto
del fruits
