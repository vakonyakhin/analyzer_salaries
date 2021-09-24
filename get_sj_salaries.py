import os
import requests

from dotenv import load_dotenv

def get_sj_vacancies(language):
    load_dotenv()
    sj_key = os.getenv('SJ_KEY')
    vacancies_pages = []
    url = 'https://api.superjob.ru/2.0/vacancies'
    header = {
        'X-Api-App-Id': sj_key,
    }

    page = 0
    pages_number = 1

    while page < pages_number:
        params = {
            'town': 4,
            'count': 100,
            'page': 0,
            'keyword': language,
            'catalogues': 48,
        }
        response = requests.get(url, params=params, headers=header)
        response.raise_for_status()
        vacancies_pages.append(response.json())

        total = response.json()['total']

        if total <= params['count']:
            page += 1
        else:
            total -= params['count']
            pages_number += 1
            page += 1

    return vacancies_pages


#
#
def predict_rub_salary(vacancy):
    if vacancy['currency'] != 'rub':
        return None
    elif vacancy['payment_from'] and vacancy['payment_to']:
        return (vacancy['payment_from'] + vacancy['payment_to']) / 2
    elif vacancy['payment_from'] and not vacancy['payment_to']:
        return vacancy['payment_from'] * 1.2
    elif vacancy['payment_to'] and not vacancy['payment_from']:
        return vacancy['payment_to'] * 0.8


def get_sj_summary_vacancies(vacancies_pages):
    salaries = []
    vacancies_summary = {}
    vacancies_list = []
    for vacancies_page in vacancies_pages:
        vacancies_list.extend(vacancies_page['objects'])
        vacancies_found = vacancies_page['total']

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
