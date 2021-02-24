"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    people_list = [
      {'name' : 'Viktor', 'age': 28, 'job' : 'specialist'}, 		
      {'name' : 'Ivan', 'age': 18, 'job' : 'unemployed'},
      {'name' : 'Olga', 'age': 23, 'job' : 'python developer'},
      {'name' : 'Nikolay', 'age': 40, 'job' : 'director'},
        ]
    with open('export.csv', 'w', encoding='utf-8') as f:
      fields = ['name', 'age', 'job']
      writer = csv.DictWriter(f, fields, delimiter=';')
      writer.writeheader()
      for person in people_list:
          writer.writerow(person)

if __name__ == "__main__":
    main()
