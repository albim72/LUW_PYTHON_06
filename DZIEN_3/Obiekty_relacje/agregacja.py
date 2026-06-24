class Car:
    def __init__(self,brand):
        self.brand = brand

    def show_info(self):
        print(f"zaparkowany samochód marki {self.brand}")

class Garage:
    def __init__(self,name):
        self.name = name
        self.cars = []

    def add_car(self,car):
        self.cars.append(car)

    def show_cars(self):
        print(f"Garage {self.name}")
        print("Samochody w garażu:")

        for car in self.cars:
            car.show_info()

car1 = Car("Jeep")
car2 = Car("BMW")

garage = Garage("Garaż przy domu")
garage.add_car(car1)
garage.add_car(car2)

garage.show_cars()
