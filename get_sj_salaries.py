import requests

from general_functions import predict_rub_salary


def get_sj_vacancies(language, api_key):
    vacancy_pages = []
    url = 'https://api.superjob.ru/2.0/vacancies'
    header = {
        'X-Api-App-Id': api_key,
    }
    moscow_city_id = 4
    page = 0
    pages_number = 5
    it_vacancies_catalog_id = 48
    params = {
        'town': moscow_city_id,
        'count': 100,
        'keyword': language,
        'catalogues': it_vacancies_catalog_id,
    }

    while page < pages_number:
        params['page'] = page
        response = requests.get(url, params=params, headers=header)
        response.raise_for_status()
        raw_response = response.json()
        vacancy_pages.append(raw_response)

        if raw_response['more']:
            page += 1
            pages_number += 1
        else:
            break
    vacancies_quantity = raw_response['total']
    return vacancy_pages, vacancies_quantity


def get_sj_total_statistic(vacancies_pages, vacancies_quantity):
    salaries = []
    vacancies_statistic = {}
    vacancies = []
    for vacancies_page in vacancies_pages:
        vacancies.extend(vacancies_page['objects'])

    for vacancy in vacancies:
        if vacancy['currency'] == 'rub':
            salary = predict_rub_salary(
                vacancy['payment_from'],
                vacancy['payment_to']
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
