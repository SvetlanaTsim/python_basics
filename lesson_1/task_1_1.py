# Задание 1. Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#     Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

# чтобы тестировать с разными числами решила создать список
# результаты через www.epochconverter.com проверила
time_duration = [53, 153, 4153, 400153, 50432, 5437932854, 7865443, 555469, 5469]

for duration in time_duration:
    # проверяем, можно ли выделить минуты, часы и дни
    is_second = duration // 60 < 1
    is_minute = 1 <= duration // 60 < 60
    is_hour = 60 <= duration // 60 < 3600
    if is_second:
        print(duration % 60, 'сек')
    elif is_minute:
        print(duration // 60, 'мин', duration % 60, 'сек')
    elif is_hour:
        print(duration // 3600, 'час', duration % 3600 // 60, 'мин', duration % 3600 % 60, 'сек')
    else:
        print(duration // 86400, 'дн', duration % 86400 // 3600, 'час', duration % 86400 % 3600 // 60, 'мин',
              duration % 86400 % 3600 % 60 % 60, 'сек')

