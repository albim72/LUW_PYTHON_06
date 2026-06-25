import json

try:
    with open('student.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(data)
    print(type(data))

    print("_"*70)

    #normalizacja
    if isinstance(data, dict):
        student = [data]
    elif isinstance(data, list):
        student = data
    else:
        raise ValueError("Niepoprawna struktura JSON - oczekiwano obiektu lub listy")

    print(student)
    print(student[0]["city"])

    print("_" * 70)


except IOError as e:
    print(e)
