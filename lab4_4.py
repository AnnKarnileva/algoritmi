a = str(input("введите цвет: "))
b = str(input("введите второй цвет: "))

if a != "красный" and a != "синий" and a != "желтый" and b != "красный" and b != "синий" and b != "желтый":
    print("Ошибка")
else:
    if (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
        print("фиолетовый")
    elif (a ==  "красный" and b == "желтый") or (a == "желтый" and b == "красный"):
        print("оранжевый")
    elif (a == "синий" and b == "желтый") or (a =="желтый"  or b == "синий"):
       print("зеленый")
    else:
        print("Ошибка")
