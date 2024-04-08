import pandas as pd

# Чтение данных из файла final.csv
final_data = pd.read_csv('final.csv')

# Проверка наличия столбца 'ID_friends' в файле final.csv
if 'ID_friends' not in final_data.columns:
    print("Столбец 'ID_friends' отсутствует в файле 'final.csv'.")
    print("Пожалуйста, убедитесь, что файл содержит нужные столбцы.")
    exit()

# Итерация по каждой ячейке столбца ID_friends
for index, row in final_data.iterrows():
    id_fr_value = row['ID_friends']

    # Проверка наличия значения ID_friends
    if pd.notna(id_fr_value):
        # Итерация по всем строкам и сравнение значения ID_friends со значениями в столбце friends
        for idx, r in final_data.iterrows():
            friends_value = r['friends']
            if id_fr_value == friends_value:
                # Копирование значения friends в столбец id_fr
                final_data.at[index, 'id_fr'] = id_fr_value
                break  # Прекращаем цикл после первого совпадения

# Сохранение результата в файл final.csv
final_data.to_csv('final.csv', index=False)
