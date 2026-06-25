from dataclasses import dataclass, field, asdict
from typing import ClassVar


@dataclass(order=True, frozen=True)
class RaceResult:
    """
    Wynik pojedynczego biegu.

    order=True  - obiekty można sortować
    frozen=True - obiekt jest niemodyfikowalny po utworzeniu
    """

    # To pole służy tylko do sortowania, nie podajemy go w konstruktorze
    sort_index: float = field(init=False, repr=False)

    race_name: str
    distance_km: float
    elevation_gain_m: int
    time_minutes: int

    def __post_init__(self):
        if self.distance_km <= 0:
            raise ValueError("Dystans musi być większy od zera.")

        if self.time_minutes <= 0:
            raise ValueError("Czas musi być większy od zera.")

        # Ponieważ klasa jest frozen=True, trzeba użyć object.__setattr__
        # sort_index będzie tempem w min/km
        object.__setattr__(self, "sort_index", self.time_minutes / self.distance_km)

    @property
    def pace_min_per_km(self) -> float:
        return self.time_minutes / self.distance_km

    def summary(self) -> str:
        return (
            f"{self.race_name}: {self.distance_km} km, "
            f"+{self.elevation_gain_m} m, "
            f"{self.time_minutes} min, "
            f"tempo: {self.pace_min_per_km:.2f} min/km"
        )


@dataclass
class Person:
    """
    Klasa bazowa.
    """

    name: str
    surname: str
    age: int

    def __post_init__(self):
        if self.age <= 0:
            raise ValueError("Wiek musi być większy od zera.")

    @property
    def full_name(self) -> str:
        return f"{self.name} {self.surname}"


@dataclass
class Athlete(Person):
    """
    Klasa dziedzicząca po Person.
    """

    sport: str
    country: str = "Polska"

    def introduce(self) -> str:
        return f"Nazywam się {self.full_name} i trenuję: {self.sport}."


@dataclass
class TrailRunner(Athlete):
    """
    Klasa dziedzicząca po Athlete.

    Pokazuje:
    - default_factory dla listy
    - pole niewidoczne w repr
    - pole klasowe ClassVar
    - metody pracujące na danych
    """

    MIN_ITRA_POINTS: ClassVar[int] = 0

    itra_points: int = 0
    favorite_mountains: list[str] = field(default_factory=list)
    results: list[RaceResult] = field(default_factory=list)

    # Nie będzie pokazywane przy print(obiekt)
    private_note: str = field(default="", repr=False)

    def __post_init__(self):
        super().__post_init__()

        if self.itra_points < self.MIN_ITRA_POINTS:
            raise ValueError("Punkty ITRA nie mogą być ujemne.")

    def add_result(self, result: RaceResult) -> None:
        self.results.append(result)

    @property
    def total_distance(self) -> float:
        return sum(result.distance_km for result in self.results)

    @property
    def total_elevation(self) -> int:
        return sum(result.elevation_gain_m for result in self.results)

    @property
    def best_result_by_pace(self) -> RaceResult | None:
        if not self.results:
            return None

        return min(self.results, key=lambda result: result.pace_min_per_km)

    def profile(self) -> str:
        mountains = ", ".join(self.favorite_mountains) or "brak danych"

        return (
            f"Zawodnik: {self.full_name}\n"
            f"Wiek: {self.age}\n"
            f"Sport: {self.sport}\n"
            f"Kraj: {self.country}\n"
            f"Punkty ITRA: {self.itra_points}\n"
            f"Ulubione góry: {mountains}\n"
            f"Liczba startów: {len(self.results)}\n"
            f"Łączny dystans: {self.total_distance:.1f} km\n"
            f"Łączne przewyższenie: {self.total_elevation} m"
        )


@dataclass
class UltraTrailRunner(TrailRunner):
    """
    Kolejny poziom dziedziczenia.

    Person -> Athlete -> TrailRunner -> UltraTrailRunner
    """

    longest_race_km: float = 0.0
    has_mountain_experience: bool = True

    def __post_init__(self):
        super().__post_init__()

        if self.longest_race_km < 0:
            raise ValueError("Najdłuższy bieg nie może mieć ujemnego dystansu.")

    def is_ready_for_ultra(self) -> bool:
        return (
            self.longest_race_km >= 42
            and self.has_mountain_experience
            and self.itra_points >= 300
        )


# ---------------------------------------------------------
# Przykład użycia
# ---------------------------------------------------------

runner = UltraTrailRunner(
    name="Marcin",
    surname="Albiniak",
    age=54,
    sport="biegi górskie",
    country="Polska",
    itra_points=421,
    favorite_mountains=["Tatry", "Bieszczady", "Pieniny"],
    longest_race_km=54,
    private_note="Zawodnik z dużym doświadczeniem górskim."
)

result1 = RaceResult(
    race_name="Bieszczadzki Ultramaraton",
    distance_km=54,
    elevation_gain_m=2500,
    time_minutes=620
)

result2 = RaceResult(
    race_name="Wielka Prehyba",
    distance_km=45,
    elevation_gain_m=2500,
    time_minutes=465
)

result3 = RaceResult(
    race_name="Kasprowy Vertical",
    distance_km=9,
    elevation_gain_m=1100,
    time_minutes=88
)

runner.add_result(result1)
runner.add_result(result2)
runner.add_result(result3)

print(runner)
print()
print(runner.introduce())
print()
print(runner.profile())
print()

best = runner.best_result_by_pace

if best:
    print("Najlepszy wynik tempem:")
    print(best.summary())

print()
print("Czy gotowy na ultra?")
print(runner.is_ready_for_ultra())

print()
print("Obiekt jako słownik:")
print(asdict(runner))
