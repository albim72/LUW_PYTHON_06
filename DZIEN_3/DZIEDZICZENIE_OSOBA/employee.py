from person import Person

class Employee(Person):
    def __init__(self, first_name, last_name, age, position:str, salary:float) -> None:
        super().__init__(first_name, last_name, age)
        self.position = position
        self.salary = salary
        
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} -> {self.age} lat/a -> {self.position} -> {self.salary}'

    def show_info(self) -> None:
        super().show_info()
        print(f"stanowisko: {self.position}")
        print(f"pensja: {self.salary} zł")
        
    def work(self) -> None:
        print(f"pracownik {self.first_name} {self.last_name} pracuje na staanowisku {self.position}")
        
    def raise_work(self,percent) -> None:
        return self.salary + percent*self.salary/100
    
