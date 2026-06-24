class FuelCalculator:
    @staticmethod
    def calculate_fuel(distance,fuel_per_100km):
        return distance * fuel_per_100km/100

fuel = FuelCalculator.calculate_fuel(300,4)
print(f"zużycie paliwa: {fuel} l")

fl = FuelCalculator()
print(fl.calculate_fuel(450,7.3))
