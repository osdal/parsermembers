import pandas as pd

# Чтение данных из файла final.csv
final_data = pd.read_csv('final.csv')

# Проверка наличия столбцов 'name_friend' и 'phone' в файле final.csv
if 'name_friend' not in final_data.columns or 'phone' not in final_data.columns:
    print("Столбцы 'name_friend' или 'phone' отсутствуют в файле 'final.csv'.")
    print("Пожалуйста, убедитесь, что файл содержит нужные столбцы.")
    exit()

# Итерация по каждой ячейке столбца name_friend
for index, row in final_data.iterrows():
    name_fr_value = row['name_friend']

    # Проверка наличия значения name_friend
    if pd.notna(name_fr_value):
        # Поиск индекса строки, в которой содержится значение name_friend в столбце friends
        friends_index = final_data[final_data['friends'] == name_fr_value].index
        if len(friends_index) > 0:
            # Копирование значения name_friend в столбец name_fr в найденной строке
            final_data.at[friends_index[0], 'name_fr'] = name_fr_value

# Итерация по каждой ячейке столбца phone
for index, row in final_data.iterrows():
    phone_fr_value = row['phone']

    # Проверка наличия значения phone
    if pd.notna(phone_fr_value):
        # Поиск индекса строки, в которой содержится значение phone в столбце friends
        friends_index = final_data[final_data['friends'] == phone_fr_value].index
        if len(friends_index) > 0:
            # Копирование значения phone в столбец phone_fr в найденной строке
            final_data.at[friends_index[0], 'phone_fr'] = phone_fr_value

# Сохранение результата в файл final.csv
final_data.to_csv('final.csv', index=False)
