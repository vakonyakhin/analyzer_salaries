import requests


def get_hh_vacancies(language):
    url = 'https://api.hh.ru/vacancies/'
    pages = 5
    page = 0
    vacancies_pages = []

    while page < pages:
        params = {
            'text': language,
            'page': page,
            'area': 1,
            'period': 30,
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        page += 1
        pages = response.json()['pages']
        vacancies_pages.append(response.json())

    return vacancies_pages


def get_hh_summary_vacancies(vacancies_pages):
    salaries = []
    vacancies_summary = {}
    vacancies_list = []
    for vacancies_page in vacancies_pages:
        vacancies_list.extend(vacancies_page['items'])
        vacancies_found = vacancies_page['found']

    for vacancy in vacancies_list:
        salary = predict_rub_salary(vacancy)
        if salary:
            salaries.append(salary)
    try:
        average_salary = int((sum(salaries) / len(salaries)))
    except ZeroDivisionError:
        average_salary = 0
    vacancies_processed = len(salaries)
    vacancies_summary['vacancies_found'] = vacancies_found
    vacancies_summary['vacancies_processed'] = vacancies_processed
    vacancies_summary['average_salary'] = int(average_salary)

    return vacancies_summary


def predict_rub_salary(vacancy):
    if vacancy['salary'] is None:
        return None
    elif vacancy['salary']['currency'] != 'RUR':
        return None
    elif vacancy['salary']['from'] and vacancy['salary']['to']:
        return (vacancy['salary']['from'] + vacancy['salary']['to']) / 2
    elif vacancy['salary']['from'] and not vacancy['salary']['to']:
        return vacancy['salary']['from'] * 1.2
    elif vacancy['salary']['to'] and not vacancy['salary']['from']:
        return vacancy['salary']['to'] * 0.8