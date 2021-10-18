"""
Написать функцию email_parse(<email_address>),
 которая при помощи регулярного выражения извлекает имя пользователя
  и почтовый домен из email адреса и возвращает их в виде словаря.
  Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и
постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном случае
использовать функцию re.compile()?
"""
import re

def email_parse(email):
    RE_VALID_MAIL = re.compile(r'[a-zA-Z0-9_-]+[@][a-zA-Z0-9]+\.[a-zA-Z0-9]+')
    #assert не пойдет так как просят ValueError
    #assert RE_VALID_MAIL.match(email), f'wrong e-mail: {email}'
    if not RE_VALID_MAIL.match(email):
        raise ValueError(f'wrong e-mail: {email}')
    else:
        email_dict={}
        MAIL = re.compile(r'[a-zA-Z0-9_-]+')
        e_mail=MAIL.match(email).group()
        email_dict['username'] = e_mail
        DOMAIN = re.compile(r'[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
        domain_name = DOMAIN.search(email).group()
        email_dict['domain'] = domain_name
        return (email_dict)

print(email_parse('someone@geekbrains.ru'))


