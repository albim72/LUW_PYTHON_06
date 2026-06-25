class MetaKlasa(type):
    def __new__(cls, name, bases, attrs):
        print("MetaKlasa -> nazwa: ", name)
        print("MetaKlasa -> dziedziczone klasy: ", bases)
        print("MetaKlasa -> atrybuty klasy: ", attrs)
        return type.__new__(cls, name, bases, attrs)

class BaseClass(object, metaclass=MetaKlasa):
    pass

class A:
    pass

class B(BaseClass):
    pass

class C(B):
    pass

class D(A,C):
    pass





