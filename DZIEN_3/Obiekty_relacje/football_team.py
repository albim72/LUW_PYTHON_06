class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_info(self):
        print(f"Zawodnik: {self.name}, pozycja: {self.position}")


class Coach:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def show_info(self):
        print(f"Trener: {self.name}, rola: {self.role}")


class Physiotherapist:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Fizjoterapeuta: {self.name}")


class Worker:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def show_info(self):
        print(f"Pracownik: {self.name}, zadanie: {self.job}")


class TeamEquipment:
    """
    Ta klasa pokazuje kompozycję.

    Sprzęt drużyny powstaje wewnątrz obiektu FootballTeam.
    Jest częścią drużyny.
    """

    def __init__(self):
        self.balls = 20
        self.training_cones = 40
        self.medical_kits = 3

    def show_info(self):
        print("Sprzęt drużyny:")
        print(f"Piłki: {self.balls}")
        print(f"Pachołki treningowe: {self.training_cones}")
        print(f"Apteczki: {self.medical_kits}")


class FootballTeam:
    def __init__(self, name):
        self.name = name

        # Kompozycja:
        # Obiekt TeamEquipment powstaje wewnątrz drużyny.
        # Jest jej częścią.
        self.equipment = TeamEquipment()

        # Agregacja:
        # Ludzie będą utworzeni poza drużyną
        # i dopiero potem dodani do drużyny.
        self.players = []
        self.coaches = []
        self.physiotherapists = []
        self.workers = []

    def add_player(self, player):
        if len(self.players) < 11:
            self.players.append(player)
        else:
            print("Drużyna ma już 11 zawodników.")

    def add_coach(self, coach):
        if len(self.coaches) < 3:
            self.coaches.append(coach)
        else:
            print("Drużyna ma już 3 trenerów.")

    def add_physiotherapist(self, physiotherapist):
        if len(self.physiotherapists) < 1:
            self.physiotherapists.append(physiotherapist)
        else:
            print("Drużyna ma już fizjoterapeutę.")

    def add_worker(self, worker):
        if len(self.workers) < 3:
            self.workers.append(worker)
        else:
            print("Drużyna ma już 3 dodatkowych pracowników.")

    def show_team(self):
        print(f"Drużyna: {self.name}")
        print()

        print("=== ZAWODNICY ===")
        for player in self.players:
            player.show_info()

        print()
        print("=== TRENERZY ===")
        for coach in self.coaches:
            coach.show_info()

        print()
        print("=== FIZJOTERAPEUCI ===")
        for physiotherapist in self.physiotherapists:
            physiotherapist.show_info()

        print()
        print("=== DODATKOWI PRACOWNICY ===")
        for worker in self.workers:
            worker.show_info()

        print()
        print("=== KOMPOZYCJA: SPRZĘT DRUŻYNY ===")
        self.equipment.show_info()


# Tworzymy ludzi poza drużyną.
# To będzie agregacja, ponieważ te obiekty istnieją niezależnie.

players = [
    Player("Jan Kowalski", "bramkarz"),
    Player("Adam Nowak", "obrońca"),
    Player("Piotr Zieliński", "obrońca"),
    Player("Marek Wiśniewski", "obrońca"),
    Player("Tomasz Wójcik", "obrońca"),
    Player("Karol Kamiński", "pomocnik"),
    Player("Paweł Lewandowski", "pomocnik"),
    Player("Robert Dąbrowski", "pomocnik"),
    Player("Michał Kaczmarek", "napastnik"),
    Player("Łukasz Mazur", "napastnik"),
    Player("Grzegorz Król", "napastnik")
]

coaches = [
    Coach("Andrzej Trener", "pierwszy trener"),
    Coach("Marcin Asystent", "asystent trenera"),
    Coach("Kamil Bramkarz", "trener bramkarzy")
]

physio = Physiotherapist("Ewa Fizjo")

workers = [
    Worker("Anna Organizator", "organizacja meczów"),
    Worker("Krzysztof Kierownik", "kierownik drużyny"),
    Worker("Barbara Media", "kontakt z mediami")
]


# Tworzymy drużynę.
team = FootballTeam("Python FC")

# Dodajemy zawodników do drużyny.
# To jest agregacja.
for player in players:
    team.add_player(player)

# Dodajemy trenerów.
for coach in coaches:
    team.add_coach(coach)

# Dodajemy fizjoterapeutę.
team.add_physiotherapist(physio)

# Dodajemy dodatkowych pracowników.
for worker in workers:
    team.add_worker(worker)

# Wypisujemy całą drużynę.
team.show_team()
