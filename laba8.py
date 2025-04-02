def z1():
    country_capitals = {
        "Италия": "Рим",
        "Германия": "Берлин",
        "Франция": "Париж",
        "Испания": "Мадрид",
        "Китай": "Пекин",
        "Япония": "Токио",
        "Россия": "Москва"
    }

    print("Список стран и столиц:")
    for country, capital in country_capitals.items():
            print(f"{country}: {capital}")



    search = input("Введите название страны: ")
    if search in country_capitals:
        capital = country_capitals[search]
        print(f"Столица страны {search}: {capital}")
    else:
        print(f"Страна '{search}' не найдена в словаре.")


    sort = sorted(country_capitals.items())
    print("\nОтсортированный список стран и столиц:")
    for country, capital in sort:
            print(f"{country}: {capital}")

z1()

def z2():
    letter_scores = {
        'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1, 'о': 1, 'р': 1, 'с': 1, 'т': 1,
        'д': 2, 'к': 2, 'л': 2, 'м': 2, 'п': 2, 'у': 2,
        'б': 3, 'г': 3, 'ё': 3, 'ь': 3, 'я': 3,
        'й': 4, 'ы': 4,
        'ж': 5, 'з': 5, 'х': 5, 'ц': 5, 'ч': 5,
        'ш': 8, 'э': 8, 'ю': 8,
        'ф': 10, 'щ': 10, 'ъ': 10
    }

    word = input("Введите слово: ").lower()
    a = 0

    for letter in word:
        if letter in letter_scores:
            a += letter_scores[letter]
        else:
            print(f" Буква '{letter}' не найдена!")

    print("Стоимость слова:", a)

z2()


def z3():
    students = {
        "Петров": ["китайский", "английский", "испанский"],
        "Сидоров": ["французский", "немецкий"],
        "Кузнецова": ["китайский", "японский"],
        "Смирнова": ["английский", "французский", "испанский"],
        "Волкова": ["китайский"],
        "Зайцева": ["итальянский", "испанский"],
        "Иванов": ["английский", "немецкий"],
        "Орлова": ["китайский", "корейский"],
        "Новицкий": ["русский"]
    }


    all_languages = set()
    for student, languages in students.items():
        all_languages.update(languages)

    sorted_languages = sorted(list(all_languages))
    print("Отсортированный список: ")
    for language in sorted_languages:
        print(language)

    k = []
    for student, languages in students.items():
        if "китайский" in languages:
            k.append(student)

    print("\nСписок студентов, которые знают китайский язык:")
    if k:
        for student in k:
            print(student)
    else:
        print("Никто не знает китайский язык.")

z3()