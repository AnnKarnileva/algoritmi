import os
from PIL import Image

def display_image_info(image_path):
                try:
                    allowed_extensions = (".png")
                    filename, file_extension = os.path.splitext(image_path)
                    if file_extension.lower() not in allowed_extensions:
                        print(
                            f"Файл '{image_path}' имеет формат: {file_extension}.  Пропускаем.")
                        return
                    img = Image.open(image_path)
                    img.show()
                    width, height = img.size
                    format = img.format
                    mode = img.mode

                    print("Информация об изображении:")
                    print(f"  Размер: {width} x {height}")
                    print(f"  Формат: {format}")
                    print(f"  Цветовая модель: {mode}")

                except FileNotFoundError:
                    print(f"Ошибка: Файл '{image_path}' не найден.")
                except Exception as e:
                    print(f"Произошла ошибка при обработке изображения: {e}")
folder_path = "pic"
for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            display_image_info(file_path)
