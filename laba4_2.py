seat = int(input("Место (1-54): "))
a = str
b = str
if not 1 <= seat <= 54:
    print("Некорректный номер")
if seat > 36:
    a = "Боковое"
    print(a)
else:
    a = "в купе"
    print(a)
if seat % 2 == 0:
    b = "Верхнее"
    print(b)
else:
    b = "Нижнее"
    print(b)

print("Место: ", a, b)




