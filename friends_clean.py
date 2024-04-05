import pandas as pd

# Чтение данных из файла friends.csv
data = pd.read_csv('friends.csv')

# Удаление строк, в которых столбец 'friends' содержит пустые списки
data = data[data['friends'].apply(lambda x: x != '[]')]

# Запись данных в файл без строк, содержащих пустые списки
data.to_csv('friends_cleaned.csv', index=False)
