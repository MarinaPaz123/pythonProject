#!/usr/bin/python3
from pprint import pprint


# Функция ищет номер телефона в списке reference
def find_tel(reference):
    while True:
        request_tel = (input("Введите телефон без пробелов.Пример: 84955555555\n"))
        # Проверяем,что пользователь ввёл только цифры и их 11
        if request_tel.isdigit() and len(request_tel) == 11:
            break
        else:
            print("Неверный формат.Номер должен состоять только из цифр и их должно быть 11.Введите номер еще раз\n")
            
    for i in reference:
        name = ""
        count = 0
        for key,val in i.items():
            if (type(val)) != list:
                name = val
            else:
                for i2 in val:
                    if i2["Номер"] == request_tel:
                        print("\n")
                        print(i2["Описание"])
                        print(i2["Номер"])
                        count = 1
            if count == 1:
                print(name)
    
            