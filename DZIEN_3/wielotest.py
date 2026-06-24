class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a + self.b

class B:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def oblicz(self):
        return self.a + self.b * self.c

class Kalk(A,B):
    def __init__(self,a,b,c,d,f):
        A.__init__(self,a,b)
        B.__init__(self,c,0,0)
        self.d = d
        self.f = f

    def sum(self):
        return super().sum() + self.f

    def funkcja(self):
        return self.a*(self.d+self.f)


k=Kalk(1,2,3,4,5)
print(k.oblicz())
print(k.funkcja())
print(k.sum())


