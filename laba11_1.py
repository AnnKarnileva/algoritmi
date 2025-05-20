import os
from PIL import Image

input_folder = "pic"
output_folder = "itog"
operation = "grayscale"

def z1(input_folder, output_folder, operation='grayscale'):
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            try:
                with Image.open(input_path) as img:
                    # Применяем выбранную операцию
                    if operation == 'grayscale':
                        processed_img = img.convert('L')
                    else:
                        processed_img = img
                    processed_img.save(output_path)
                    print(f"Обработано: {filename}")
            except Exception as e:
                print(f"Ошибка при обработке {filename}: {e}")
z1(input_folder, output_folder, operation="grayscale")