#!/usr/bin/python3
from pprint import pprint

# Функция проверяет,есть ли имя в reference
def checking_name(reference,name):
    for i in reference:
        for key,val in i.items():
            if type(val) == str:
                if val == name:
                    return True