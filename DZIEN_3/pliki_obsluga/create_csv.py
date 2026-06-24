import csv

students = [
    ["imię","nazwisko","punkty"],
    ["Anna","Nowak",67],
    ["Ola","Kos",33],
    ["Piotr","Kłos",78],
    ["Ula","Kot",24],
    ["Olaf","Nowik",87],
    ["Jan","Opiś",64],
    ["Leon","Kotek",56],
    ["Nadia","Modo",12],
]


try:
    with open('students.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in students:
            writer.writerow(row)

    print("plik został zapisany!")

except IOError:
    print("błąd zapisu pliku")
