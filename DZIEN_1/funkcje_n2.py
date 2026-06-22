def rank_lang(*lang,nr_rank):
    print(f"ranking nr: {nr_rank} -> 1. {lang[0]}, 2. {lang[1]}, 3. {lang[2]}")

rank_lang("Python","Java","C++",nr_rank=3)
rank_lang("Python","Java","C#",nr_rank=64)


def rank_lang_ext(*lang, nr_rank):
    if len(lang) < 3:
        print("Błąd: podaj minimum 3 języki.")
        return

    if len(lang) > 10:
        print("Błąd: podaj maksimum 10 języków.")
        return

    print(f"Ranking nr: {nr_rank}")

    for i, language in enumerate(lang, start=1):
        print(f"{i}. {language}")

rank_lang_ext("Python", "Java", "C++", nr_rank=3)

rank_lang_ext("Python", "Java", "C#", "JavaScript", "Go", nr_rank=64)


def rank_lang_input(*lang, nr_rank):
    if len(lang) < 3:
        print("Błąd: podaj minimum 3 języki.")
        return

    if len(lang) > 10:
        print("Błąd: podaj maksimum 10 języków.")
        return

    print(f"Ranking nr: {nr_rank}")

    for i, language in enumerate(lang, start=1):
        print(f"{i}. {language}")


languages = []

while len(languages) < 10:
    language = input("Podaj język programowania albo wpisz STOP: ")

    if language == "STOP":
        break

    languages.append(language)

if len(languages) >= 3:
    rank_lang(*languages, nr_rank=1)
else:
    print("Za mało języków. Musisz podać minimum 3.")

rank_lang_input(*languages, nr_rank=1)
