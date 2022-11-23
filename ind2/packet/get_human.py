#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import datetime


def get_human():
    """""
    Запросить данные о человеке.
    """""
    # Запросить данные о человеке.
    surname = input("Фамилия: ")
    name = input("Имя: ")
    zodiak = input("Знак Зодиака: ")
    date_str = input("Введите дату выпуска (dd/mm/yyyy)\n")
    date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()

    # Вернуть словарь.
    return {
        'surname': surname,
        'name': name,
        'zodiak': zodiak,
        'date': date
    }