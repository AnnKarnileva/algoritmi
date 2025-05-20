import csv

def create_csv_file(filename):
    data = [
        ["Продукт", "Количество", "Цена"],
        ["Молоко", 2, 80],
        ["Сыр", 1, 500],
        ["Хлеб", 2, 80]
    ]

    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Файл {filename} успешно создан")


def calculate_expenses(filename):
    total = 0
    print("Нужно купить:")

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) == 3:
                product, quantity, price = row
                quantity = int(quantity)
                price = int(price)
                total += quantity * price
                print(f"{product} - {quantity} шт. за {price} руб.")
    print(f"\nИтоговая сумма: {total} руб.")
csv_file = "products.csv"
try:
    with open(csv_file, mode='r', encoding='utf-8'):
        pass
except FileNotFoundError:
    create_csv_file(csv_file)

calculate_expenses(csv_file)