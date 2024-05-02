#!/usr/bin/python3
from pprint import pprint
import json


# Функция выводит информацию из списка reference
def loading(reference):
    for i in reference:
        for key,val in i.items():
            print("-"*15)
            print(key)
            print(val)
            print("-"*15)
    
            
                