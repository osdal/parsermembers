import pandas as pd

# Чтение данных из файла final_phone.csv
final_phone_data = pd.read_csv('final_phone.csv')

# Чтение данных из файла friends_phone_barkov_comma.csv
friends_data = pd.read_csv('friends_phone_barkov_comma.csv')

# Выполнение объединения по столбцам friends и ID
final_phone_data = final_phone_data.merge(friends_data[['ID', 'name', 'phone']], left_on='friends', right_on='ID', how='left')

# Удаление лишнего столбца 'ID'
final_phone_data.drop(columns=['ID'], inplace=True)

# Сохранение результата в файл final_phone.csv
final_phone_data.to_csv('final_phone.csv', index=False)
