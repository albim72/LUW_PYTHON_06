import json

try:
    with open('student.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(data)
    print(type(data))

    print("_"*70)

    #normalizacja
    if isinstance(data, dict):
        students = [data]
    elif isinstance(data, list):
        students = data
    else:
        raise ValueError("Niepoprawna struktura JSON - oczekiwano obiektu lub listy")

    print(students)
    print(students[0]["city"])

    print("_" * 70)

    print("lISTA STUDENTÓW\n")
    for i,s in enumerate(students,start=1):
        if not isinstance(s, dict):
            raise ValueError(f"Element {i} nie jest obiektem JSON")
        required_keys = ["name", "surname", "points"]
        missing = [key for key in required_keys if key not in s]
        if missing:
            raise ValueError(f"Brakuje pól {missing} w elemencie #{i}")

        name = s["name"]
        surname = s["surname"]
        points = s["points"]
        print(f"Student: {name}, {surname} -> {points}")

except IOError as e:
    print(e)
except ValueError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
except json.decoder.JSONDecodeError as e:
    print(e)
