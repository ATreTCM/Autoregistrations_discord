'''Завдання:
написати пітон скрипт, який автоматично створює discord аккаунт і логіниться в нього отримуючи token авторизації з headers “authorization”
Умови:
- cкрипт повинен приймати емейл та нікнейм у командному рядку
- пароль генерується автоматично
- підтверджувати пошту не треба
Очікується
- повинен створюватися обліковий запис і повертати в командний рядок token після логіну'''

import json
import requests
import random
import time

answer_from_login = []


def auto_password():
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    symbol = ':~!?@#$%^&*_-+()[]{}></\|".,:;'
    len_password = 15
    main_value = lower_letters + lower_letters.upper() + symbol + numbers
    password = ''.join(random.sample(main_value, len_password))
    return password


def diskord_auto_registration():
    registation_data = {
        'captcha_key': None,
        'consent': True,
        'date_of_birth': "1988-05-28",
        'email': input('Enter email: '),
        'fingerprint': None,
        'gift_code_sku_id': None,
        'invite': None,
        'password': auto_password(),
        'promotional_email_opt_in': False,
        'username': input('Enter nickname: '),
    }
    response_register = requests.post('https://discord.com/api/v9/auth/register', json=registation_data)
    answer_from_login.append(registation_data['email'])
    answer_from_login.append(registation_data['password'])
    return answer_from_login


def diskord_auto_auntification():
    login_data = {
        'login': answer_from_login[0],
        'password': answer_from_login[1],
        'undelete': False,
        'captcha_key': None,
        'login_source': None,
        'gift_code_sku_id': None,
    }
    response_login = requests.post('https://discord.com/api/v9/auth/login', json=login_data)
    if response_login.status_code == '429':
        time.sleep(60)
        diskord_auto_auntification()
    else:
        print(json.loads(response_login.headers['authorization']))


if __name__ == '__main__':
    diskord_auto_registration()
    diskord_auto_auntification()
