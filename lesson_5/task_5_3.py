# Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
#
#
# Необходимо реализовать генератор,
# возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
#
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# Доказать, что вы создали именно генератор.
# Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект.

from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', '11Б', '11А'
]

#Вариант 1, через zip_longest

# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Убираем лишние классы:
if len(tutors) < len(klasses):
    klass_dif = len(klasses) - len(tutors)
    for klass in range(klass_dif):
        klasses.pop()

# print(tutors)
# print(klasses)

tutors_klass_gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
print(type(tutors_klass_gen)) #доказываем, что это генератор
print(next(tutors_klass_gen))
print(next(tutors_klass_gen))
print(next(tutors_klass_gen))
print(next(tutors_klass_gen))
print(next(tutors_klass_gen))
print(next(tutors_klass_gen))
print(next(tutors_klass_gen))
#print(next(tutors_klass_gen)) StopIteration

#Вариант 2, через zip

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Степан', 'Афанасий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]
#Eсли в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None)
# добавляем нужное количество None:
if len(tutors) > len(klasses):
    tutor_dif = len(tutors) - len(klasses)
    for klass in range(tutor_dif):
        klasses.append(None)

tutors_klass_gen_zip = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(type(tutors_klass_gen_zip)) #доказываем, что это генератор
print(next(tutors_klass_gen_zip))
print(next(tutors_klass_gen_zip))
print(next(tutors_klass_gen_zip))
print(next(tutors_klass_gen_zip))
print(next(tutors_klass_gen_zip))
print(next(tutors_klass_gen_zip))
print(next(tutors_klass_gen_zip))
print(next(tutors_klass_gen_zip))
print(next(tutors_klass_gen_zip))
#print(next(tutors_klass_gen_zip)) #StopIteration
