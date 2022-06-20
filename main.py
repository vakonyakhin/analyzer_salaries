import os

from dotenv import load_dotenv

from get_hh_salaries import get_hh_vacancies, get_hh_total_statistic
from get_sj_salaries import get_sj_vacancies, get_sj_total_statistic
from general_functions import print_table


def main():
    load_dotenv()
    sj_key = os.getenv('SJ_KEY')
    programming_languages = [
        'Javascript',
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

    for language in programming_languages:
        hh_vacancies, hh_found_vacancies = get_hh_vacancies(language)
        sj_vacancies, sj_found_vacancies = get_sj_vacancies(language, sj_key)
        hh_vacancies_statistic = get_hh_total_statistic(hh_vacancies, hh_found_vacancies)
        sj_vacancies_statistic = get_sj_total_statistic(sj_vacancies, sj_found_vacancies)
        hh_languages_salary[language] = hh_vacancies_statistic
        sj_languages_salary[language] = sj_vacancies_statistic

    print_table('HeadHunter', hh_languages_salary)
    print_table('SuperJob', sj_languages_salary)


if __name__ == "__main__":
    main()
