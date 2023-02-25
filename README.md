# scrapy_parser_pep

Python PEP parser
____

### Описание:

Асинхронный парсер осуществляет сбор данных о PEP с официального сайта Python, анализирует их и выдаёт в формате csv.


После парсинга будет сформировано 2 .csv документа:
- pep — список всех PEP с официального сайта, их номера, названия и статусы.
- status_summary — список возможных статусов PEP, количество PEP в этои статусе и суммарное количество PEP.

### Стек технологий 

![](https://img.shields.io/badge/Python-3.10-black?style=flat&logo=python) 
![](https://img.shields.io/badge/Scrapy-2.5.1-black?style=flat)

### Запуск проекта
- Клонировать репозиторий:
```
git clone https://github.com/Legyan/scrapy_parser_pep
```

- Cоздать и активировать виртуальное окружение:

```
windows: python -m venv env
linux: python3 -m venv env
```

```
windows: source env/Scripts/activate
linux: source env/bin/activate
```

- Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

- Запустить паук pep:

```
scrapy crawl pep
```

После завершения работы парсера в директории /results появятся файлы pep_{datetime}.csv и status_summary_{datetime}.csv.

### Примеры работы парсера:


#### pep_2024-01-01T12-00-00.csv

| number        | name                       | status   |
| ------------- |:--------------------------:| --------:|
| 1             | PEP Purpose and Guidelines |   Active |
| 219           | Stackless Python           | Deferred |
| 221           | Import As                  |    Final |
| ...           | ...                        |    ...   |


#### status_summary_2024-01-01_12-00-00.csv

| Cтатус        | Количество   |
| ------------- |:------------:|
| Accepted      | 44           |
| Active        | 31           |
| April Fool!   | 1            |
| Deferred      | 36           |
| Draft         | 29           |
| Final         | 269          |
| Rejected      | 120          |
| Superseded    | 20           |
| Withdrawn     | 55           |
| Total         | 605          |
