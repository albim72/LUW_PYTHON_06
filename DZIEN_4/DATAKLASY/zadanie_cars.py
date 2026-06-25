from dataclasses import dataclass


@dataclass
class Engine:
    power: int
    fuel_type: str
    capacity: float

    def description(self) -> str:
        return f"Silnik: {self.power} KM, {self.fuel_type}, pojemność {self.capacity} L"


@dataclass
class Vehicle:
    brand: str
    model: str
    year: int

    def info(self) -> str:
        return f"{self.brand} {self.model}, rok produkcji: {self.year}"


@dataclass
class Car(Vehicle):
    doors: int
    engine: Engine

    def car_info(self) -> str:
        return (
            f"{self.info()}\n"
            f"Liczba drzwi: {self.doors}\n"
            f"{self.engine.description()}"
        )


# ---------------------------------------------------------
# Przykład użycia programu
# ---------------------------------------------------------

engine = Engine(
    power=150,
    fuel_type="benzyna",
    capacity=1.6
)

car = Car(
    brand="Toyota",
    model="Corolla",
    year=2020,
    doors=5,
    engine=engine
)

print(car.car_info())
