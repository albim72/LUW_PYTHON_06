class AddHelloMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs["hello"] = lambda self:print("Hello,Python!")
        return type.__new__(cls, name, bases, attrs)

class A(metaclass=AddHelloMeta):
    pass

a = A()
a.hello()
print(type(a))

def helloB(self):
    print("Hello,nowa klasa B!")

class B(A):
    pass

#monkey patching
b = B()
b.hello()

B.hello = helloB
b.hello()

class C(B):
    pass

c = C()
c.hello()
