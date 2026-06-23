class Car:
    def __init__(self, brand, model, fuel, mileage):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.mileage = mileage

    def show_info(self):
        print(f"Marka: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Paliwo: {self.fuel} litrów")
        print(f"Przebieg: {self.mileage} km")

if __name__ == '__main__':

    car = Car("Toyota", "Corolla", 20, 150000)

    car.show_info()
