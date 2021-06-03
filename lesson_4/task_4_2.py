# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.


from requests import get
from decimal import Decimal

def currency_rate(currency):
    currency = currency.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_str = response.text
    start = response_str.find(currency)
    value = response_str.find('Value',start)
    result = response_str[value+6:value+13]
    # у меня в случае, если .find() не находил код валюты, выдает versio
    # должен выдавать -1.
    if result == ' versio' or result == -1:
        return None
    else:
        result_decimal = Decimal(result.replace(',', '.'))
        return result_decimal

if __name__ == '__main__':
    print(currency_rate('usd'))
    print(type(currency_rate('usd')))
    print(currency_rate('DKK'))
    print(currency_rate('jpy'))
    print(currency_rate('KRW'))
    print(currency_rate('AAA'))
    print(currency_rate('tmt'))
    print(currency_rate('eur'))
    print(currency_rate('1235254365г65рпыафцп'))

