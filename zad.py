while True:
    age = input("Скільки вам років? ")
    try:
        age = int(age)
        if age >= 18:
            print("Доступ дозволено")
        else:
            print("Доступ відхилено")
    except ValueError:
        print(f"{age} не є числом. Будь ласка введіть число!")
