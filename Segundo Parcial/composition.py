def codestr(c):
    return (hex(ord(c)))


h = codestr("a")
print(h)


# Función compuesta que recibe las dos
# funciones, f siendo la externa y
# g la interna, con x siendo a valor
# a evaular 
def compose(f, g):
    def fn(x):
        return f(g(x))

    return fn


codestr2 = compose(hex, ord)
print(codestr2('s'))