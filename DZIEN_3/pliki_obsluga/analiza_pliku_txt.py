from turtledemo.chaos import line

try:
    with open("shopping_list.txt","r",encoding="utf-8") as file:
        text = file.read()

        #liczba znaków
        char_count = len(text)

        #liczba słów
        words = text.split()
        word_count = len(words)

        #liczba linii
        lines = text.split("\n")
        line_count = len(lines)

    print("ANALIZA PLIKU TEKSTOWEGO....")
    print("_"*80)
    print(f"liczba linii: {line_count}")
    print(f"liczba słów: {word_count}")
    print(f"liczba znaków: {char_count}")
except FileNotFoundError:
    print("nie nzalezono pliku.... ")
except IOError:
    print("błąd odczytu pliku.... ")
