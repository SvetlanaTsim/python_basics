# При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу,
# по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
# Примеры запуска скриптов:
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1

import sys
from itertools import islice

command_list = [*sys.argv]

if len(command_list) == 1:
    with open('bakery.csv', encoding='utf-8') as f:
        print(f.read())

# без чтения всего файла
if len(command_list) == 2:
     number = int(command_list[1])-1
     with open('bakery.csv', encoding='utf-8') as f:
         out_info = list(islice(f, number, None))
         print(''.join(out_info))

if len(command_list) == 3:
     number1 = int(command_list[1])-1
     number2 = int(command_list[2])
     with open('bakery.csv', encoding='utf-8') as f:
         out_info = list(islice(f, number1, number2))
         print(''.join(out_info))