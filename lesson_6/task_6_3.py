# #Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи

import sys
from itertools import zip_longest
import json
import pickle

# создаем файлы
users = ['Иван, Иванович, Иванов', 'Петр, Петрович, Петров', 'Сидор, Сидорович, Сидоров', 'Степан, Степанович, Степанов',
         'Сергей, Сергеевич, Сергеев', 'Александра, Александровна, Александрова', 'Евгения, Евгеньевна, Евгеньева']
with open('users.csv', 'w', encoding='utf-8') as f:
    f.write('\n'.join(users))

hobby = ['скалозазание, охота\n', 'чтение, рыбалка\n', 'вышивание крестиком\n', 'бальные танцы\n', 'дзюдо, айкидо\n',
         'плавание, прыжки в длину\n', 'туризм, активный отдых\n']
with open('hobby.csv', 'w', encoding = 'utf-8') as f:
    f.writelines(hobby)

# теперь читаем
with open('users.csv', encoding='utf-8') as f:
    users_read = f.readlines()
users_read_final = [users.strip() for users in users_read]
print(users_read_final)

with open('hobby.csv', encoding='utf-8') as f:
    hobby_read = f.readlines()
hobby_read_final = [hobby.strip() for hobby in hobby_read]
print(hobby_read_final)

if len(hobby_read) > len(users_read):
    sys.exit(1)
else:
    out_dict = {user:hobby for user, hobby in zip_longest(users_read_final,hobby_read_final)}

print(out_dict)

#сохраняем в файл и пробуем достать
with open('user_hobby.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f)

with open('user_hobby.json', encoding='utf-8') as f:
    our_dict = json.load(f)
print(our_dict)

with open('user_hobby_1.pickle', 'wb') as f:
    pickle.dump(out_dict, f)

with open('user_hobby_1.pickle', 'rb') as f:
    our_dict_pickle = pickle.load(f)
print(our_dict_pickle)
