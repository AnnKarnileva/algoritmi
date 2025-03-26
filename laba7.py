def z1():
    my_list = [10, 25, 30, 45, 50]
    try:
        user_number = int(input("Введите число: "))
        if user_number in my_list:
            print("Поздравляю, Вы угадали число!")
        else:
            print("Нет такого числа!")
        print("Исходный список:", my_list)
        print("Число пользователя:", user_number)
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")
z1()

def z2():

    list = input("Введите список: ")
    try:
        a = list.split()
        list = [int(x) if x.isdigit() else x for x in list]
    except ValueError:
        print("Ошибка: Некорректный ввод.")
        return
    s = set()
    d = set()

    for i in list:
        if i in s:
            d.add(i)
        else:
            s.add(i)
    if d:
        print("Есть повторения")
        for duplicate in d:
            print(duplicate)
    else:
        print("Нет повторений")
z2()

def z3():
    days = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
    try:
        num = int(input("Сколько выходных на неделе вы хотите? (Введите число): "))

        if not 0 <= num <= len(days):
            print("Ошибка: Введено некорректное количество выходных. Пожалуйста, введите число от 0 до 7.")
            return

        weekend = list(days[-num:])
        working = list(days[:-num])

        print("Ваши выходные дни:", ", ".join(weekend))
        print("Ваши рабочие дни:", ", ".join(working))

    except ValueError:
        print("Ошибка")
z3()

def z4():
    group1 = ["Петров", "Васильева", "Смирнов", "Кузнецов", "Попова", "Глушко", "Федорова", "Петров", "Михайлов",
              "Иванов"]
    group2 = ["Зайцев", "Лебедев", "Орлов", "Карнильева", "Виноградов", "Морозова", "Денисова", "Волков", "Ершов", "Борисов"]

    team = tuple(group1[:5] + group2[:5])

    print("Список студентов группы 1:", group1)
    print("Список студентов группы 2:", group2)
    print("Спортивная команда:", team)

    print("Длина спортивной команды:", len(team))


    sorted_team = tuple(sorted(team))
    print("Спортивная команда (отсортированная по алфавиту):", sorted_team)

    search_name = "Иванов"
    if search_name in sorted_team:
        count = sorted_team.count(search_name)
        print(f"В команду входит студент '{search_name}'.")
        print(f"Фамилия '{search_name}' встречается в команде {count} раз(а).")
    else:
        print(f"В команду не входит студент '{search_name}'.")
z4()