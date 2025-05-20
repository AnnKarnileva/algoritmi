
from PIL import Image
def z1():
        try:
            img = Image.open('main-image.jpg')
            img.show()
            width, height = img.size
            format = img.format
            color_mode = img.mode
            print("Размер изображения: ", width, "x", height)
            print("Формат: ", format)
            print("Цветовая модель: ", color_mode)
        except FileNotFoundError:
            print("Ошибка!")



def z2():
        try:
            img = Image.open('main-image.jpg')
            width, height = img.size
            new_width = width // 3
            new_height = height // 3
            resized_img = img.resize((new_width, new_height))
            resized_img.save("resized_main-image.jpg")
            print("Уменьшенное изображение: resized_main-image.jpg")


            mirrored_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
            mirrored_horizontal.save("mirrored_horizontal.jpg")
            print("Горизонтальное: mirrored_horizontal.jpg")


            mirrored_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
            mirrored_vertical.save("mirrored_vertical.jpg")
            print("Вертикальное: mirrored_vertical.jpg")

        except FileNotFoundError:
            print("Файл не найден по указанному пути.")
        except Exception as e:
            print(f"Ошибка при обработке изображения: {e}")


import os
from PIL import Image, ImageFilter, ImageDraw, ImageFont

def z3():
        input_folder = "input_images"
        output_folder = "output_images"

        for filename in os.listdir(input_folder):
            if filename.endswith((".jpg")):
                try:

                    image_path = os.path.join(input_folder, filename)
                    img = Image.open(image_path)

                    filtered_img = img.filter(ImageFilter.EDGE_ENHANCE)

                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_filtered{ext}"
                    output_path = os.path.join(output_folder, new_filename)

                    filtered_img.save(output_path)
                    print(f"Файл '{filename}' обработан и сохранен как '{new_filename}'")

                except Exception as e:
                    print(f"Произошла ошибка при обработке файла '{filename}': {e}")

        print("Обработка изображений завершена.")



def z4():

    image_path = "main-image.jpg"
    watermark_text = "Sun sun sun"
    output_path = "watermarked_main-image.png"


    try:
            img = Image.open(image_path).convert("RGBA")
            draw = ImageDraw.Draw(img)

            font = ImageFont.truetype("arial.ttf", 30)

            draw.text((50, 50), watermark_text, font=font, fill=(255, 255, 255, 128))

            img.save(output_path, "PNG")
            print(f"Водяной знак добавлен и сохранен в {output_path}")

    except FileNotFoundError:
            print(f"Ошибка: Файл '{image_path}' не найден.")
    except Exception as e:
            print(f"Произошла ошибка: {e}")


z4()
