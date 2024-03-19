from time import sleep

import pytest
import configparser

from yandex_auth import yandex_auth


class TestYandexAuth:


    def setup_method(self):
        self.yandex_auth = yandex_auth

    @pytest.mark.parametrize(
        'login, password, expected',
        (

                ['bvjejvbbnjfdnbb', 'vnbjbvwbo', 'Неверный логин'],
                ['', '', 'Неверный пароль'], # Введите корректный логин и не верный пароль
                ['', '', 'Авторизация прошла успешно'] #Введён корректный логин и пароль
        )
    )
    def test_yandex_auth_login(self, login, password, expected):
        result = self.yandex_auth(login=login, password=password)
        assert result == expected




