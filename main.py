import os

from dotenv import load_dotenv

from get_hh_salaries import get_hh_vacancies, get_hh_summary_vacancies
from get_sj_salaries import get_sj_vacancies, get_sj_summary_vacancies
from general_functions import print_table


def main():
    load_dotenv()
    sj_key = os.getenv('SJ_KEY')
    prog_languages = [
        'JavaScript',
        'Java',
        'Python',
        'Ruby',
        'C++',
        'C#',
        'C',
        'Swift',
        'Go',
        'PHP'
    ]

    hh_languages_salary = {}
    sj_languages_salary = {}

    for language in prog_languages:
        hh_vacancies_list = get_hh_vacancies(language)
        sj_vacancies_list = get_sj_vacancies(language, sj_key)
        hh_vacancies_summary = get_hh_summary_vacancies(hh_vacancies_list)
        sj_vacansies_summary = get_sj_summary_vacancies(sj_vacancies_list)
        hh_languages_salary[language] = hh_vacancies_summary
        sj_languages_salary[language] = sj_vacansies_summary

    print_table('HeadHunter', hh_languages_salary)
    print_table('SuperJob', sj_languages_salary)


if __name__ == "__main__":
    main()
