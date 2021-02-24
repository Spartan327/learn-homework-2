"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    now = datetime.now()
    yerstaday = now - timedelta(days=1)
    thirty_days_ago = now - timedelta(days=30)
    print (yerstaday.strftime('%Y-%m-%d'))
    print (now.strftime('%Y-%m-%d'))
    print (thirty_days_ago.strftime('%Y-%m-%d'))

def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
