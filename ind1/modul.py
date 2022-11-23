#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def last_name(last_name):
    l = last_name
    def first_name(first_name):
        f = first_name
        n = 'Уважаемый {} {}! ' \
            'Вы делаете работу по замыканиям функций.'.format(l, f)
        return n
    return first_name
