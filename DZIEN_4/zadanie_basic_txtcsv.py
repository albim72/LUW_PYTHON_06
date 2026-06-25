import csv


students = [
    {"name": "Jan", "surname": "Kowalski", "points": 80},
    {"name": "Anna", "surname": "Nowak", "points": 95},
    {"name": "Piotr", "surname": "Zieliński", "points": 67}
]


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


print("Dane zostały zapisane do plików students.txt oraz students.csv.")
