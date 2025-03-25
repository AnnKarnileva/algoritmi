def z1():
    n = int(input("Введите количество слов: "))
    words = []

    for i in range(n):
        word = input(f"Введите слово {i+1}: ")
        words.append(word)

    result_string = " ".join(words)

    print("Результат:", result_string)
z1()

def z2():
    words = []
    while True:
        word = input("Введите слово (или 'stop' чтобы звкончить): ").lower()
        if word == "stop":
            break
        words.append(word)
    result_string = " ".join(words)

    print("Результат:", result_string)

z2()

def z3():
    word = input("Введите слово: ").lower()
    if "ф" in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
z3()
import random
def z4():
    correct_answers = 0
    incorrect_answers = 0

    while incorrect_answers < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        expression = f"{num1} + {num2} = "
        answer = input(expression)
        try:
            user_answer = int(answer)
            correct_result = num1 + num2

            if user_answer == correct_result:
                print("Правильно!")
                correct_answers += 1
            else:
                print("Ответ неверный.")
                incorrect_answers += 1
        except ValueError:
            print("Ошибка: Введите целое число.")
            incorrect_answers += 1
    print("Игра окончена.")
    print(f"Правильных ответов: {correct_answers}")
z4()