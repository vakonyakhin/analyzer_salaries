from terminaltables import SingleTable


def print_table(title, vacancies):
    final_table = [['Язык', 'Всего вакансий', 'Обработано', 'Средняя ЗП']]
    for language, summary_vacancies_value in vacancies.items():
        final_table.append([language,
                            summary_vacancies_value['vacancies_found'],
                            summary_vacancies_value['vacancies_processed'],
                            summary_vacancies_value['average_salary']
                            ])
    printed_table = SingleTable(final_table, title=title)
    print(printed_table.table)


def predict_rub_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    elif salary_from and not salary_to:
        return salary_from * 1.2
    elif salary_to and not salary_from:
        return salary_to * 0.8

