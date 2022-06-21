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
        raw_response = response.json()
        page += 1
        pages = raw_response['pages']
        vacancy_pages.append(raw_response)
    vacancies_quantity = raw_response['found']

    return vacancy_pages, vacancies_quantity


def get_hh_total_statistic(vacancies_pages, vacancies_quantity):
    salaries = []
    vacancies_statistic = {}
    vacancies = []
    for vacancies_page in vacancies_pages:
        vacancies.extend(vacancies_page['items'])

    for vacancy in vacancies:
        if vacancy['salary'] \
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
    vacancies_statistic['vacancies_found'] = vacancies_quantity
    vacancies_statistic['vacancies_processed'] = vacancies_processed
    vacancies_statistic['average_salary'] = average_salary

    return vacancies_statistic
