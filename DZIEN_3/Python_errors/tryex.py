try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    result = a/b
except ZeroDivisionError:
    print("Błąd: dzielenie przez 0")
except ValueError:
    print("podałeś coś co nie jest liczbą!")
else:
    print(result)
finally:
    print("Idziemy dalej...")

print("ciąg dalszy")
