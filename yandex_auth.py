import json
from pprint import pprint
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


chrome_path = ChromeDriverManager().install()
browser_service = Service(executable_path=chrome_path)
browser = Chrome(service=browser_service)

def yandex_auth(login, password):
    browser.get('https://passport.yandex.ru/auth/')
    login_input = browser.find_element(By.CLASS_NAME, value='Textinput').find_element(By.ID, value='passp-field-login')
    login_input.click()
    login_input.send_keys(f'{login}')
    login_input.send_keys('\n')
    sleep(2)
    try:
        wrong_login = browser.find_element(By.ID, value='field:input-login:hint')
        if wrong_login:
            print('Неверный логин')
            return 'Неверный логин'
    except:

        sleep(2)
        password_input = browser.find_element(By.CLASS_NAME, value='Textinput').find_element(By.ID, value='passp-field-passwd')
        password_input.click()
        password_input.send_keys(f'{password}')
        password_input.send_keys('\n')
        sleep(2)
    try:
        wrong_pass = browser.find_element(By.ID, value='field:input-passwd:hint')
        if wrong_pass:
            print('Неверный пароль')
            return 'Неверный пароль'
    except:
        return 'Авторизация прошла успешно'



if __name__ == '__main__':

    login = input('Please enter your login: ')
    password = input('Please enter your password: ')
    yandex_auth(login=login, password=password)

