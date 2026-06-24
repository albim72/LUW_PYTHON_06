class Employee:

    count = 0

    def __init__(self,name):
        self.name = name
        Employee.count += 1


    @classmethod
    def how_many(cls):
        return cls.count

e1 = Employee("Karol")
e2 = Employee("Ewa")
e3 = Employee("Ula")
e4 = Employee("Piotr")
e5 = Employee("Maria")

print(Employee.how_many())
