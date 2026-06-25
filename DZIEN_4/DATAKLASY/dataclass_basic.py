from dataclasses import dataclass

class Student:
    def __init__(self, imie:str, wiek:int, uczelnia:str, kierunek:str)->None:
        self.imie = imie
        self.wiek = wiek
        self.uczelnia = uczelnia
        self.kierunek = kierunek

    def __repr__(self):
        return f"Student: {self.imie}, {self.wiek}, {self.uczelnia}, {self.kierunek}"

s1 = Student("Paweł",23,"UMCS","informatyka")
print(s1)


@dataclass
class StudentDT:
    imie:str
    wiek:int
    uczelnia:str
    kierunek:str = None

    # def __init__(self,imie:str,nazwisko:str,rok_st:int):
    #     self.imie = imie
    #     self.nazwisko = nazwisko
    #     self.rok_st = rok_st

s2 = StudentDT("Ewa",22,"SWPS","psychologia")

print(s2)

s3 = StudentDT("Ela",22,"SWPS","psychologia")
s4 = StudentDT("Tomek",23,"SWPS")

print(s4)
