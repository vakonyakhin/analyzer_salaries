# Developers salary analyzer 
Данный скрипт позволяет получить информацию о средней зарплате на основе данных сайтов [hh.ru](https://hh.ru) 
и [superjob](https://superjob.ru).

# Как запустить
Python 3 должен быть установлен. Используйте команду pip для установки зависимостей:

```
pip install -r requirements.txt
```
### Переменные окружения

* SJ_KEY

Пример 
```
SJ_KEY='v3.r.134950175.096fd8e380b90ba4c12093d1988f82e0db91be66.bc679cd162966a5212348787564'
```
### Как получить ключ

Для получения ключа необходимо зарегистрировать приложение на сайте [API SuperJOB](https://api.superjob.ru/register).
Полученное значение указано в поле ```Secret key```.

### Запуск

```
$ python main.py

# Результат

┌HeadHunter Moscow──────┬──────────────────┬─────────────────────┬──────────────────┐
│ Язык программирования │ Вакансий найдено │ Вакансий обработано │ Средняя зарплата │
├───────────────────────┼──────────────────┼─────────────────────┼──────────────────┤
│ Java                  │ 1745             │ 430                 │ 163728           │
│ C#                    │ 1088             │ 348                 │ 145706           │
│ Objective-C           │ 175              │ 52                  │ 179730           │
│ Python                │ 1369             │ 334                 │ 144901           │
│ C++                   │ 170              │ 84                  │ 129965           │
│ Go                    │ 366              │ 95                  │ 171563           │
│ Scala                 │ 183              │ 40                  │ 221327           │
│ PHP                   │ 1146             │ 552                 │ 118483           │
│ JavaScript            │ 2631             │ 799                 │ 136277           │
│ Typescript            │ 422              │ 153                 │ 164365           │
│ C                     │ 365              │ 199                 │ 127320           │
│ Swift                 │ 242              │ 81                  │ 175555           │
│ Ruby                  │ 205              │ 66                  │ 157121           │
└───────────────────────┴──────────────────┴─────────────────────┴──────────────────┘

┌SuperJob Moscow────────┬──────────────────┬─────────────────────┬──────────────────┐
│ Язык программирования │ Вакансий найдено │ Вакансий обработано │ Средняя зарплата │
├───────────────────────┼──────────────────┼─────────────────────┼──────────────────┤
│ JavaScript            │ 63               │ 30                  │ 120066           │
│ Java                  │ 20               │ 12                  │ 119220           │
│ Python                │ 14               │ 12                  │ 105778           │
│ Ruby                  │ 1                │ 1                   │ 175000           │
│ PHP                   │ 48               │ 17                  │ 107908           │
│ C++                   │ 26               │ 17                  │ 92056            │
│ C#                    │ 27               │ 18                  │ 119286           │
│ C                     │ 18               │ 9                   │ 94774            │
│ Go                    │ 0                │ 0                   │ 0                │
│ Objective-C           │ 2                │ 1                   │ 100000           │
│ Scala                 │ 0                │ 0                   │ 0                │
│ Swift                 │ 1                │ 0                   │ 0                │
│ Typescript            │ 5                │ 4                   │ 190000           │
└───────────────────────┴──────────────────┴─────────────────────┴──────────────────┘
```

### Цель проекта
Создан в рамках изучения API Python.


