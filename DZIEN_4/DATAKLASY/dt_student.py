from dataclasses import dataclass

@dataclass
class Person:
    name: str
    surname: str

    def fullname(self):
        return f"{self.name} {self.surname}"

@dataclass
class Student(Person):
    index_number:str
    points:int

    def passed(self):
        return self.points >= 50



student = Student(
    name="Jan",
    surname="Kot",
    index_number="1034531",
    points=75
)

print(student)
print(student.fullname())
print(student.passed())
