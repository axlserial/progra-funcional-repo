import math
from operator import itemgetter, mul
from functools import reduce

# len
l = [1, 2, 3]
print(len(l))

r = range(1, 100)
print(len(r))

m = map(math.sqrt, l)

# sum
print(sum(l))
print(sum(r))
print(sum(m))

# initial value
a = [[2, 4], [0, 5], [5, 3]]
print(sum(sum(a, [])))

t1 = (1, 2, 3)
t2 = (4, 5, 6)
tr = t1 + t2
print(tr)

# min
print("\nMin:")

b = [2, 5, 7, 1, 9]
print(min(map(math.sqrt, b)))
print(min(a))
print(min(b, default=0))

print(min(a, default=0, key=itemgetter(1)))

# any
print('\nAny:')
print(any([1, 0, 2]))
print(any(['', 0, False]))
print(any([]))

# all
print('\nAll:')
print(all([1, 0, 2]))
print(all(['', 0, False]))
print(all([]))

# reduce
print('\nReduce:')
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5], 10))