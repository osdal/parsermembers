import pandas as pd

# Чтение данных из файла friends.csv
data = pd.read_csv('friends.csv')

# Распарсить список значений из столбца "friends"
parsed_friends = []
for friends_list in data['friends']:
    parsed_friends.extend(eval(friends_list))

# Создать DataFrame из распарсенных значений
new_data = pd.DataFrame({'friends': parsed_friends})

# Записать данные в новый файл friends_expanded.csv
new_data.to_csv('friends_expanded.csv', index=False)

# Чтение данных из файла friends_expanded.csv
data = pd.read_csv('friends_expanded.csv')

# Удаление дубликатов и сохранение только уникальных значений
unique_data = data.drop_duplicates()

# Запись данных обратно в файл friends_expanded.csv
unique_data.to_csv('friends_expanded.csv', index=False)
