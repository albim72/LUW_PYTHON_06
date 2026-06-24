class Person:
    def __init__(self, first_name:str, last_name:str, age:int)->None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self)->str:
        return f'{self.first_name} {self.last_name} -> {self.age} lat/a'
    
    def show_info(self)->None:
        print(f"imię: {self.first_name}")
        print(f"nazwisko: {self.last_name}")
        print(f"wiek: {self.age}")
        
    def introduce(self)->None:
        print(f"Nazywam się: {self.first_name} {self.last_name}")
        
    def wiek_za_n_lat(self,n:int)->int:
        return self.age + n
