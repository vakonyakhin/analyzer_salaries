import requests

from general_functions import predict_rub_salary


def get_sj_vacancies(language, api_key):
    vacancies_pages = []
    url = 'https://api.superjob.ru/2.0/vacancies'
    header = {
        'X-Api-App-Id': api_key,
    }
    moscow_city_id = 4
    it_vacancies_catalog_id = 48
    params = {
        'town': moscow_city_id,
        'count': 100,
        'page': 0,
        'keyword': language,
        'catalogues': it_vacancies_catalog_id,
    }

    while True:

        response = requests.get(url, params=params, headers=header)
        response.raise_for_status()
        vacancies_pages.append(response.json())
        more_pages = response.json()['more']

        if not more_pages:
            break

    return vacancies_pages


def get_sj_total_vacancies(vacancies_pages):
    salaries = []
    vacancies_total = {}
    vacancies_list = []
    for vacancies_page in vacancies_pages:
        vacancies_list.extend(vacancies_page['objects'])
        vacancies_found = vacancies_page['total']

    for vacancy in vacancies_list:
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
    vacancies_total['vacancies_found'] = vacancies_found
    vacancies_total['vacancies_processed'] = vacancies_processed
    vacancies_total['average_salary'] = average_salary

    return vacancies_total
