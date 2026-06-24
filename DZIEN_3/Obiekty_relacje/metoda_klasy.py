class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    @classmethod
    def from_text(cls,text):
        data = text.split(";")
        brand = data[0]
        model = data[1]
        year = data[2]
        return cls(brand,model,year)

    def show_info(self):
        print(self.brand)
        print(self.model)
        print(self.year)

car = Car("Jeep","Compass","2020")
car.show_info()
print(car)

car2 = Car.from_text("Toyota;Corolla;2023")
car2.show_info()
print(car2)
