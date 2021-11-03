"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярногоLesson 4 http://www.cbr.ru/
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает
их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
"""


import re
def email_parse(email_adress):
    RE_email = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)'), re.IGNORECASE)
    if not RE_email.match(email_adress):
        raise ValueError(f'wrong email:{email_adress}')
    print(RE_email.match(email_adress).groupdict())

try:
    (email_parse('someone@geekbrains.ru')
    (email_parse('someone@geekbrainsru')
except ValueError as err:
    print(err)