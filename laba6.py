from calendar import month


def z1():
    n = int(input("введите число: "))
    if n % 3 == 0:
        print("Делится на 3!")
    else:
        print("Не делится")
z1()

def z2():
    try:
        user = input("Введите число: ")
        n = float(user)
        res = 100 / n
        print("Ответ: ", res)

    except ValueError:
        print("Некорректное значение!")
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
    except Exception as e:
        print("Ошибка: {e}")
z2()

def z3(date_str):
    try:
        day, month, year = map(int, date_str.split("."))
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1000 <= year <= 9999):
            return None

        L = year % 100
        return day * month == L
    except ValueError:
        return None

print(z3(input("введите дату: ")))


def z4(ticket):
    if not isinstance(ticket, str):
        return None
    if len(ticket) % 2 != 0:
        return None
    try:
        half_length = len(ticket) // 2
        f = ticket[:half_length]
        s = ticket[half_length:]

        sum_first_half = sum(int(digit) for digit in f)
        sum_second_half = sum(int(digit) for digit in s)

        return sum_first_half == sum_second_half

    except ValueError:
        return None
print(z4(input("введите номер билета: ")))
