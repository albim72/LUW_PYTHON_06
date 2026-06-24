from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, university:str, field_of_study:str) -> None:
        super().__init__(first_name, last_name, age)
        self.university = university
        self.field_of_study = field_of_study

    def show_info(self) -> None:
        super().show_info()
        print(f"uczelnia: {self.university}")
        print(f"kierunek studiów: {self.field_of_study}")  
        
    def zaliczenie_semestru(self,punkty):
        if punkty>=70:
            print(f"próg zaliczenia -> 70")
            print(f"zaliczenie semestru -> liczba punktów {punkty}")
        else:
            print(f"próg zaliczenia -> 70")
            print(f"brak zaliczenia semestru -> liczba punktów {punkty}")
    
