#!/usr/bin/python3
from pprint import pprint



# Функция ищет имя в списке reference
def find_name(reference):
    request_name = (input("Введите название контакта\n"))
    name_temp =""
    count = 0
    for i in reference:
        for key,val in i.items():
            if val == request_name:
                name_temp = request_name
                count =  1
                print("\n")
                print(request_name,"\n")
                for key2,val2 in i.items():
                    if type(val2) == list:
                        for i2 in val2:
                            print(i2["Описание"])
                            print(i2["Номер"])
    if count !=1:
        print("Контакт не найден!")

