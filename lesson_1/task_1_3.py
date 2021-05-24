# Задание 3. Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.

#создаем список с числами 1-20 для того, чтобы тестировать склонения
procents = []
for num in range(21):
    procents.append(num)
#проверяем, что все в порядке
print(procents)
#в цикле присваиваем каждому числу нужное окончание
for procent in procents:
    if procent == 1:
        print(procent, 'процент')
    elif procent == 2 or procent == 3 or procent == 4:
        print(procent, 'процента')
    else:
        print(procent, 'процентов')

#решила, посмотреть, как будет, если до 100 сделать (факультативно для интереса)
procents_100 = []
for num in range(101):
    procents_100.append(num)

print(procents_100)

for procent in procents_100:
    if procent == 1 or procent % 10 == 1:
        print(procent, 'процент')
    elif procent == 2 or procent == 3 or procent == 4 or procent % 10 == 2 or procent % 10 == 3 or procent % 10 == 4:
        print(procent, 'процента')
    else:
        print(procent, 'процентов')



