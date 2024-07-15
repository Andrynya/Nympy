import pandas as pd
import numpy as np

data = {
    'Ученик' : ['Артем', 'Александр', 'Антон', 'Алексей', 'Анна', 'Виктор', 'Анастасия', 'Петр', 'Евгений', 'Мария'],
    'История' : [3, 4, 5, 3, 2, 5, 4, 2, 5, 3],
    'Математика' : [2, 4, 5, 5, 4, 2, 3, 5, 4, 5],
    'Физика' : [5, 4, 3, 2, 5, 4, 3, 3, 5, 2],
    'Химия' : [4, 3, 5, 3, 4, 5, 5, 4, 5, 4],
    'Биология' : [5, 5, 5, 5, 5, 4, 5, 5, 5, 5]
}

df = pd.DataFrame(data)
print(df.head())

#Вычисление средней оценки
mean_ist = df['История'].mean()
print("Средняя оценка по истории: ", mean_ist)
mean_mat = df['Математика'].mean()
print("Средняя оценка по математике: ", mean_mat)
mean_fiz = df['Физика'].mean()
print("Средняя оценка по физике: ", mean_fiz)
mean_xim = df['Химия'].mean()
print("Средняя оценка по химии: ", mean_xim)
mean_bio = df['Биология'].mean()
print("Средняя оценка по биологии: ", mean_bio)

#Вычисление медианной оценки
median_ist = df['История'].median()
print("Медианная оценка по истории: ", median_ist)
median_mat = df['Математика'].median()
print("Медианная оценка по математике: ", median_mat)
median_fiz = df['Физика'].median()
print("Медианная оценка по физике: ", median_fiz)
median_xim = df['Химия'].median()
print("Медианная оценка по химии: ", median_xim)
median_bio = df['Биология'].median()
print("Медианная оценка по биологии: ", median_bio)

Q1_math = df['Математика'].quantile(0.25)
print(f"Q1_math : {Q1_math}")
Q3_math = df['Математика'].quantile(0.75)
print(f"Q3_math : {Q3_math}")
IQR = Q3_math - Q1_math
print(f"IQR : {IQR}")

#Вычисление стандартного отклонения
std_ist = df['История'].std()
print("Стандартное отклонение по истории: ", std_ist)
std_mat = df['Математика'].std()
print("Стандартное отклонение по математике: ", std_mat)
std_fiz = df['Физика'].std()
print("Стандартное отклонение по физике: ", std_fiz)
std_xim = df['Химия'].std()
print("Стандартное отклонение по химии: ", std_xim)
std_bio = df['Биология'].std()
print("Стандартное отклонение по биологии: ", std_bio)