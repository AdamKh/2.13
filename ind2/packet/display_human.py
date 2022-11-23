#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def display_human(humans):
    """""
    Отобразить список людей
    """""
    # Проверить что список людей не пуст
    if humans:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Фамилия и имя",
                "Знак Зодиака",
                "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о всех.
        for idx, worker in enumerate(humans, 1):
            date = worker.get('date', '')
            print(
                '| {:^4} | {:<14} {:<15} | {:<20} | {}{} |'.format(
                    idx,
                    worker.get('surname', ''),
                    worker.get('name', ''),
                    worker.get('zodiak', ''),
                    date,
                    ' ' * 5
                )
            )

        print(line)

    else:
        print("Список работников пуст.")