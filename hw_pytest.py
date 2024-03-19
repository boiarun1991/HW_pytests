import requests
import configparser
import json


class Info_def_lists:
    def __init__(self):
        self.courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
                        "Frontend-разработчик с нуля"]

        self.mentors = [
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
             "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
             "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков",
             "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
             "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
             "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
             "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
             "Азамат Искаков", "Роман Гордиенко"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин",
             "Михаил Ларченко"]
        ]


courses_and_mentors = Info_def_lists()


def sort_list_to_asc(courses, mentors):
    courses = courses
    mentors = mentors
    durations = [14, 20, 12, 20]

    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    durations_dict = {}

    for _id, months in enumerate(courses_list):
        key = months['duration']
        durations_dict.update({_id: (key, _id)})

    durations_dict = tuple(sorted(durations_dict.values()))
    result = []
    for value, index in durations_dict:

        result.append(f'{courses[index]} - {value} месяцев')

    return result


def find_equal_name(flag, courses, mentors):
    result = []
    courses = courses

    mentors = mentors
    durations = [14, 20, 12, 20]

    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    if flag is True:
        for _id, course in enumerate(courses):
            all_names = [i.split()[0] for i in mentors[_id]]
            unique_names = set(all_names)
            unique_names = list(unique_names)
            unique_names.sort()

            same_name_list = []
            for name in unique_names:
                if all_names.count(name) > 1:
                    for full_name in mentors[_id]:
                        if name in full_name:
                            same_name_list.append(full_name)

            if same_name_list:
                result.append(f'На курсе {course} есть тёзки: {", ".join(sorted(same_name_list))}')
        return result
    else:
        return [None]


def find_longest_and_shortest_course(courses, mentors):
    courses = courses
    mentors = mentors
    durations = [14, 20, 12, 20]

    courses_list = []

    for i in zip(['title', 'mentors', 'duration'], [courses, mentors, durations]):
        course_dict = {i[0]: i[1]}
        courses_list.append(course_dict)

    min_ = min(courses_list[2]['duration'])
    max_ = max(courses_list[2]['duration'])

    maxes = []
    minis = []
    for i, duration in enumerate(durations):
        if duration == max_:
            maxes.append(i)
        elif duration == min_:
            minis.append(i)

    courses_min = []
    courses_max = []
    for _id in minis:
        courses_min.append(courses_list[0]['title'][_id])
    for _id in maxes:
        courses_max.append(
            courses_list[0]['title'][_id])

    return ', '.join(courses_min)


#Yandex API


class HttpException(Exception):
    def __init__(self, status, message=''):
        self.status = status
        self.message = message

    def __str__(self):
        return f'http error: {self.status}\n{self.message}'


def yandex_api(ya_token):
    base_url = 'https://cloud-api.yandex.net/v1/disk'
    params = {
        'path': 'test'
    }
    headers = {
        'Authorization': f'OAuth {ya_token}'
    }
    response = requests.request('PUT', f'{base_url}/resources', params=params, headers=headers, json=None)
    print(response.status_code)
    if response.status_code >= 400 and response.status_code != 409:
        raise HttpException(response.status_code, response.text)
    return response


config = configparser.ConfigParser()
config.read('config.ini')
ya_token = config['yandex']['token']

if __name__ == '__main__':
    print(sort_list_to_asc(courses_and_mentors.courses, courses_and_mentors.mentors))
    print(find_equal_name(True, courses_and_mentors.courses, courses_and_mentors.mentors))
    print(find_longest_and_shortest_course(courses_and_mentors.courses, courses_and_mentors.mentors))
    print(find_equal_name(False, courses_and_mentors.courses, courses_and_mentors.mentors))
    print(yandex_api(ya_token))