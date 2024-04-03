import csv

# Определение размера блока для чтения
block_size = 1024  # например, 1 КБ

# Открываем текстовый файл для чтения
with open('phone_vk_list.txt', 'r', encoding='utf-8') as txt_file:
    csv_file = open('phone_vk_list.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(csv_file)

    # Записываем заголовки столбцов
    csv_writer.writerow(['First Name', 'Last Name', 'Email', 'Phone'])

    try:
        while True:
            # Читаем блок данных из файла
            block = txt_file.read(block_size)
            if not block:
                break  # Выходим из цикла, если достигнут конец файла

            # Преобразуем данные в формат CSV и записываем в файл
            lines = block.splitlines()
            for line in lines:
                data = line.strip().strip(");").split(",")
                data = [d.strip().strip("'") for d in data]
                csv_writer.writerow(data)

    except Exception as e:
        print("Произошла ошибка:", e)
    finally:
        # Закрываем файлы
        txt_file.close()
        csv_file.close()

print("Преобразование завершено!")
