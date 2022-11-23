#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
from packet.display_human import display_human
from packet.get_human import get_human
from packet.help import help
from packet.select_humans import select_humans


def main():
    # Вывод сообщения о команде help
    print("help - список всех команд")
    # Список людей.
    humans = []

    # Организовать бесконечный цикл запроса команд
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            human = get_human()
            # Добавить словарь в список.
            humans.append(human)
            # Отсортировать список в случае необходимости.
            if len(humans) > 1:
                humans.sort(key=lambda item: item.get('date', ''))

        elif command == 'list':
            display_human(humans)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            addedzz = parts[1]
            selected = select_humans(humans, addedzz)
            display_human(selected)

        elif command == 'help':
            help()

        else:
            print(f"Неизвестная комманда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()