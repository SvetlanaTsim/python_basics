# 2.	*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы —
# результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(num):
    translate_dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if num[0].isupper():
        num = num.lower()
        answer = translate_dict.get(num, 'None')
        return answer.capitalize()
    else:
        return translate_dict.get(num, 'None')

#проверка
print(num_translate_adv('Five'))
print(num_translate_adv('five'))
print(num_translate_adv('One'))
print(num_translate_adv('one'))
print(num_translate_adv('eleven'))