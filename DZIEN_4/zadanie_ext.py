import csv


students = []

try:
    number_of_students = int(input("Podaj liczbę studentów: "))

    for i in range(number_of_students):
        print(f"\nStudent #{i + 1}")

        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")
        points = int(input("Podaj liczbę punktów: "))

        student = {
            "name": name,
            "surname": surname,
            "points": points
        }

        students.append(student)

    # Zapis danych do pliku TXT
    with open("students.txt", "w", encoding="utf-8") as file:
        file.write("Lista studentów\n\n")

        for student in students:
            line = f"Student: {student['name']} {student['surname']}, punkty: {student['points']}\n"
            file.write(line)

    # Zapis danych do pliku CSV
    with open("students.csv", "w", encoding="utf-8", newline="") as csvfile:
        fieldnames = ["name", "surname", "points"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for student in students:
            writer.writerow(student)

    print("\nDane zostały zapisane do plików students.txt oraz students.csv.")

except ValueError:
    print("Błąd: liczba studentów i liczba punktów muszą być liczbami całkowitymi.")
