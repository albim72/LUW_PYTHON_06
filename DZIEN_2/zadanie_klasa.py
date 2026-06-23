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

    def refuel(self, amount):
        if amount <= 0:
            print("Ilość paliwa musi być większa od zera.")
        else:
            self.fuel += amount
            print(f"Zatankowano {amount} litrów paliwa.")

    def drive(self, distance):
        if distance <= 0:
            print("Dystans musi być większy od zera.")
            return

        needed_fuel = distance / 10

        if needed_fuel > self.fuel:
            print("Za mało paliwa na tę trasę.")
        else:
            self.fuel -= needed_fuel
            self.mileage += distance
            print(f"Przejechano {distance} km.")

    def is_old(self):
        return self.mileage > 200000


if __name__ == '__main__':

    car = Car("Toyota", "Corolla", 20, 150000)

    print("DANE POCZĄTKOWE:")
    car.show_info()

    print()
    car.refuel(10)

    print()
    car.drive(50)

    print()
    print("DANE PO TANKOWANIU I JEŹDZIE:")
    car.show_info()

    print()
    print("Czy samochód jest stary?", car.is_old())
