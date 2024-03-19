import configparser

import pytest
import requests

from hw_pytest import sort_list_to_asc, find_equal_name, Info_def_lists, find_longest_and_shortest_course


class TestFuncs:
    def setup_method(self):
        self.course_and_mentors = Info_def_lists()

    def test_sort_asc(self):
        expected = ['Python-разработчик с нуля - 12 месяцев',
                    'Java-разработчик с нуля - 14 месяцев',
                    'Fullstack-разработчик на Python - 20 месяцев',
                    'Frontend-разработчик с нуля - 20 месяцев']

        assert expected == sort_list_to_asc(self.course_and_mentors.courses, self.course_and_mentors.mentors)

    @pytest.mark.parametrize(
        'flag, expected',
        (
            [True, 'На курсе Java-разработчик с нуля есть тёзки: Иван Бочаров, Иван Маркитан,'
                   ' Максим Батырев, Максим Воронцов, Сергей Индюков, Сергей Сердюк'],
            [False, None]
        )
    )
    def test_find_equal_name(self, flag, expected):
        assert expected == (find_equal_name(flag, self.course_and_mentors.courses, self.course_and_mentors.mentors)[0])

    def test_find_longest_and_shortest(self):
        expected = 'Python-разработчик с нуля'
        assert expected == find_longest_and_shortest_course(self.course_and_mentors.courses,
                                                            self.course_and_mentors.mentors)


class TestYandexApi:
    def setup_class(self):
        self.headers = {
            'Authorization': f'OAuth {ya_token}'
        }
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/resorces'
        self.params = {
            'path': 'test'
        }

    def teardown_class(self):
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                params=self.params,
                                headers=self.headers)
        assert response.status_code == 204

    def test_create_folder(self):

        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=self.params,
                                headers=self.headers)
        assert response.status_code == 201

    def test_create_folder_2(self):
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=self.params,
                                headers=self.headers)
        assert response.status_code == 409

    def test_wrong_path(self):
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resource',
                                params=self.params,
                                headers=self.headers)
        assert response.status_code == 404


config = configparser.ConfigParser()
config.read('config.ini')
ya_token = config['yandex']['token']