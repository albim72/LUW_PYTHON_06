liczby = [4,5,7,245,7,99,235,8,90,2,46,251,35,27,88,111,-53,0,-532,36,70]

lista_parzyste = list(filter(lambda x:x%2==0, liczby))
print(lista_parzyste)

cube = list(map(lambda x:x**3, liczby))
print(cube)

#lambda - funkcja anonimowa
print((lambda x,y:x+y)(2,4))
print((lambda x,y:x-y)(2,4))

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y

print(add(2,4))
print(subtract(2,4))

an = lambda u,w:u-2*w
print(an(8,2))

def multi(n):
    return lambda x:x*n

print(multi(2)(9))

def dwa(a):
    return a*2

d = lambda x,funkcja:funkcja(x)

print(d(45,dwa))
