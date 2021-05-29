# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# А. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули,
# если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# B.Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# D. Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

price_list = [2.4, 15.42, 189.34, 4.24, 67.01, 154.18, 453.6, 231.4, 5.14, 56.87]

# А. Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули,
# если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

string_list = []
for price in price_list:
    price_s = str(price).split('.')
    if len(price_s[1]) < 2:
        price_s[1]= price_s[1] + '0'
    price_string_price = f'{int(price_s[0]):01d} руб {int(price_s[1]):02d} коп'
    string_list.append(price_string_price)

print (string_list)
price_str = ', '.join(string_list)
print (price_str)

# B.Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).

print(id(price_list))
price_list.sort()
print(price_list)

# вариант печати в виде из задания А:
string_list = []
for price in price_list:
    price_s = str(price).split('.')
    if len(price_s[1]) < 2:
        price_s[1]= price_s[1] + '0'
    price_string_price = f'{int(price_s[0]):01d} руб {int(price_s[1]):02d} коп'
    string_list.append(price_string_price)
print (string_list)
print(id(price_list)) # id тот же

# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
#вариант 1
new_list = price_list.copy()
new_list.reverse()
print(new_list)
# вариант печати в виде из задания А:
string_list = []
for price in new_list:
    price_s = str(price).split('.')
    if len(price_s[1]) < 2:
        price_s[1]= price_s[1] + '0'
    price_string_price = f'{int(price_s[0]):01d} руб {int(price_s[1]):02d} коп'
    string_list.append(price_string_price)
print (string_list)
print(id(new_list)) # id другой
print(id(price_list))
#вариант 2
new_price_list = sorted(price_list, reverse=True)
print(new_price_list)
# вариант печати в виде из задания А:
string_list = []
for price in new_price_list:
    price_s = str(price).split('.')
    if len(price_s[1]) < 2:
        price_s[1]= price_s[1] + '0'
    price_string_price = f'{int(price_s[0]):01d} руб {int(price_s[1]):02d} коп'
    string_list.append(price_string_price)
print (string_list)
print(id(new_price_list)) # id другой
print(id(price_list))

# D. Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print(string_list[:5])
