#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def select_humans(humans, addedzz):
    """""
    Выбрать людей с заданным ЗЗ
    """""
    # Инициализировать счетчик.
    count = 0
    # Сформировать список людей
    result = []
    # Проверить сведения людей из списка.
    for human in humans:
        if human.get('zodiak', '') == addedzz:
            count += 1
            result.append(human)

    return result