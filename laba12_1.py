import json
data = {
        "products": [
            {"name": "Шоколад", "price": 50, "available": True, "weight": 100},
            {"name": "Кофе", "price": 100, "available": False, "weight": 250},
            {"name": "Чай", "price": 70, "available": True, "weight": 50}
        ]
}
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)



def display_product_info(filename="products.json"):

    try:
        with open(filename, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)

        products = data["products"]  # Получаем список продуктов из JSON

        for product in products:
            name = product["name"]
            price = product["price"]
            weight = product["weight"]
            available = product["available"]

            print("Название:", name)
            print("Цена:", price)
            print("Вес:", weight)
            if available:
                print("В наличии")
            else:
                print("Нет в наличии!")
            print()

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный формат JSON в файле '{filename}'.")
    except KeyError as e:
        print(f"Ошибка: Отсутствует ключ '{e}' в JSON-данных.")
    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")

def add_product_to_json(filename="products.json"):

    try:
        with open(filename, 'r+', encoding='utf-8') as jsonfile:  # Открываем для чтения и записи
            data = json.load(jsonfile)

            # Запрашиваем информацию о новом продукте
            name = input("Введите название продукта: ")
            price = int(input("Введите цену продукта: "))
            weight = int(input("Введите вес продукта: "))
            available = input("Есть в наличии? (да/нет): ").lower() == "да"

            # Создаем словарь для нового продукта
            new_product = {
                "name": name,
                "price": price,
                "available": available,
                "weight": weight
            }

            # Добавляем новый продукт в список
            data["products"].append(new_product)

            # Перемещаемся в начало файла и записываем обновленные данные
            jsonfile.seek(0)
            json.dump(data, jsonfile, ensure_ascii=False, indent=2)
            jsonfile.truncate() # Обрезаем остаток старых данных

            print("Продукт успешно добавлен в файл.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный формат JSON в файле '{filename}'.")
    except ValueError:
        print("Ошибка: Некорректный ввод цены или веса. Введите целые числа.")
    except KeyError as e:
        print(f"Ошибка: Отсутствует ключ '{e}' в JSON-данных.")
    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")
add_product_to_json()
display_product_info()

