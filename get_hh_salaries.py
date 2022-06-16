import requests

from general_functions import predict_rub_salary


def get_hh_vacancies(language):
    url = 'https://api.hh.ru/vacancies/'
    pages = 5
    page = 0
    vacancy_pages = []
    moscow_city_id = 1
    params = {
        'text': language,
        'area': moscow_city_id,
        'period': 30,
    }
    while page < pages:
        params['page'] = page
        response = requests.get(url, params=params)
        response.raise_for_status()
        response_json = response.json()
        page += 1
        pages = response_json['pages']
        vacancy_pages.append(response_json)

    return vacancy_pages


def get_hh_total_statistic(vacancies_pages):
    salaries = []
    vacancies_total = {}
    vacancies_list = []
    for vacancies_page in vacancies_pages:
        vacancies_list.extend(vacancies_page['items'])
        vacancies_found = vacancies_page['found']

    for vacancy in vacancies_list:
        if vacancy['salary'] is not None \
              and vacancy['salary']['currency'] == 'RUR':
            salary = predict_rub_salary(
                vacancy['salary']['from'],
                vacancy['salary']['to']
            )
            if salary:
                salaries.append(salary)
    try:
        average_salary = sum(salaries) / len(salaries)
    except ZeroDivisionError:
        average_salary = 0
    vacancies_processed = len(salaries)
    vacancies_total['vacancies_found'] = vacancies_found
    vacancies_total['vacancies_processed'] = vacancies_processed
    vacancies_total['average_salary'] = average_salary

    return vacancies_total
