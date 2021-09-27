from terminaltables import SingleTable


def print_table(title, vacancies):
    final_table = [['Язык', 'Всего вакансий', 'Обработано', 'Средняя ЗП']]
    for language in vacancies:
        final_table.append([language,
                            vacancies[language]['vacancies_found'],
                            vacancies[language]['vacancies_processed'],
                            vacancies[language]['average_salary']
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

