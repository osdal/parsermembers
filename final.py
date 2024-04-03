import pandas as pd

# Чтение данных из файла friends.csv и выбор нужных столбцов
friends_data = pd.read_csv('friends.csv', usecols=['ID', 'name', 'surname'])

# Распарсивание списка значений в столбце friends_expanded.csv и запись каждого значения в отдельную ячейку
expanded_data = pd.read_csv('friends_expanded.csv', header=None)
expanded_data = expanded_data[0].astype(str).str.split(',', expand=True)

# Объединение данных из friends.csv и распарсенного списка в один файл
final_data = pd.concat([friends_data, expanded_data], axis=1)

# Запись данных в файл final.csv
final_data.to_csv('final.csv', index=False)

# Преобразование файла в формат xlsx
final_data.to_excel('final.xlsx', index=False, engine='openpyxl')
