import pandas as pd

# Чтение данных из файла friends.csv
data = pd.read_csv('friends.csv')

# Копирование столбцов ID, name, surname без изменений в новый DataFrame
final_data = data[['ID', 'name', 'surname']].copy()

# Распарсить список значений из столбца "friends"
parsed_friends = []
for friends_list in data['friends']:
    parsed_friends.append(eval(friends_list))

# Добавить столбец "friends" с распарсенными значениями в final_data
final_data['friends'] = parsed_friends

# Расширить DataFrame, чтобы каждый айди был в отдельной ячейке
final_data = final_data.explode('friends')

# Запись данных в новый файл final.csv
final_data.to_csv('final.csv', index=False)

# Конвертация в формат xls
final_data.to_excel('final.xls', index=False)
