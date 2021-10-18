# 5.	Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

import random

def get_jokes(num):
    """Эта функция возвращает шутки из 3х случайных чисел в количестве, равном num"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []
    for time in range(num):
        joke_string = ' '.join([random.choice(nouns), random.choice(adverbs), random.choice(adjectives)])
        jokes_list.append(joke_string)
    return jokes_list

#вторая часть
#Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

def get_jokes_flag(num = 5, flag = True):
    """
    Эта функция возвращает случайные шутки в количестве num
    В случае, если flag = True, фукция возвращает шутки без повторов слов.
    В таком случае максимальное число шуток равно длине списков слов - 5.
    Если num > 5, возвращает None.
    num: int
    flag: bool
    По умолчанию:
    num = 5
    flag = True
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []
    if flag == True:
        if num > len(nouns) or num > len(adverbs) or num > len(adjectives):
            return None
        else:
            for time in range(num):
                word_1 = random.choice(nouns)
                nouns.remove(word_1)
                word_2 = random.choice(adverbs)
                adverbs.remove(word_2)
                word_3 = random.choice(adjectives)
                adjectives.remove(word_3)
                joke_string = ' '.join([word_1, word_2, word_3])
                jokes_list.append(joke_string)
            return jokes_list
    else:
        for time in range(num):
            joke_string = ' '.join([random.choice(nouns), random.choice(adverbs), random.choice(adjectives)])
            jokes_list.append(joke_string)
        return jokes_list


print(get_jokes(5))
print(get_jokes_flag(num = 5, flag = True))
#print(help(get_jokes_flag))

