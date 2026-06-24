class Engine:
    def __init__(self,power):
        self.power = power

    def start(self):
        print(f"Silnik o mocy {self.power} kM został uruchomiony!")

class Car:
    def __init__(self,brand, power):
        self.brand = brand
        self.engine = Engine(power)

    def start_car(self):
        print(f"uruchamiam samochód marki {self.brand}")
        self.engine.start()

car = Car(brand="Toyota", power=255)
car.start_car()
