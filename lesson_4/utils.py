# *(вместо 2) Доработать функцию currency_rates():
# теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?

from requests import get
from decimal import Decimal
from datetime import date

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
        print(None)
    else:
        date_index = response_str.find('Date')
        result_date = response_str[date_index + 6:date_index + 16]
        day, month, year = result_date.split('.')
        date_cur = date(year=int(year), month=int(month), day=int(day))
        result_decimal = Decimal(result.replace(',', '.'))
        print(result_decimal, date_cur)


if __name__ == '__main__':
    currency_rate('usd')
    currency_rate('EUR')
    currency_rate('FFF')
    currency_rate('sfdhsghndgmdyghardfgvs')
    currency_rate('usd')
    currency_rate('KRW')
    currency_rate('DKK')
