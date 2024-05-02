#!/usr/bin/python3
from pprint import pprint

# Функция проверяет,есть ли номер в reference
def checking_number(reference,number):
    for i in reference:
        for key,val in i.items():
            if type(val) == list:
                for i2 in val:
                    if i2["Номер"] == number:
                        return True