from person import Person
from employee import Employee
from student import Student

def main():
    person = Person("Jan","Kowalski",48)
    employee = Employee("Anna","Nowak",35,"Asystentka prezesa",8700)
    student = Student("Olaf","Jankowski",22,"SWPS","Sztuczna inteligencja")

    print("_________ OSOBA __________")
    print(person)
    person.show_info()
    person.introduce()
    print(f"wiek za 5 lat: {person.wiek_za_n_lat(5)} lat/a")

    print("_________ PRACOWNIK __________")
    employee.show_info()
    employee.introduce()
    employee.work()
    print(f"pensja po podwyżce: {employee.raise_work(15)} zł")

    print("_________ STUDENT __________")
    student.show_info()
    student.introduce()
    student.zaliczenie_semestru(78)


if __name__ == '__main__':
    main()
