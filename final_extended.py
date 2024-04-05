import pandas as pd

# Чтение данных из файла final.xlsx с использованием openpyxl
final_data = pd.read_excel('final.xlsx', engine='openpyxl')

# Вывод первых нескольких строк для проверки
print(final_data.head())
