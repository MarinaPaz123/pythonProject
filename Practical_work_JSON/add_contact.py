#!/usr/bin/python3
from pprint import pprint
from checking_number import checking_number
from checking_name import checking_name
import json

# Функция добавляет новый контакт в список reference
# Новые данные сохраняются в файл!

def add_contact(reference):
    while True:
        request_name = (input("Введите имя:\n"))
        # Проверяем ,что переменная request_name не пустая
        if len(request_name) == 0:
            print("Значение ""Имя"" не может быть пустым!\n")
            continue
        # Вызываем функцию, которая проверяет, есть ли имя в reference
        # Если такое имя уже есть в справочнике, сообщаем об этом пользователю.Запрашиваем данные заново,так как имена не могут совпадать ( такой вот я человек) 
        checking_nam = checking_name(reference,request_name)
        if checking_nam == True:
            print("Контакт с таким именем существует!\n")
            continue
        break
    while True:
        try:
            request_volume = (int(input("Сколько телефонов Вы хотите записать?Введите число:\n")))
            if request_volume <= 0:
                print("ВВЕДИТЕ ЦЕЛОЕ ПОЛОЖИТЕЛЬНОЕ ЧИСЛО!\n")
                continue
            break
        except ValueError:
            print("ВВЕДИТЕ ЦЕЛОЕ ЧИСЛО!\n ")
            
    final_list = []
    temp_list_number = []
    temp_list_name = []
    # Проходимся циклом столкько раз,сколько телефонов необходимо записать пользователю
    for i in range(1,request_volume+1):
        while True:
            number = (input(f"Введите {i} телефон без пробелов.Пример: 84955555555\n"))
            # Проверяем ,что пользователь ввёл именно цифры, и их 11
            if number.isdigit() and len(number) == 11:
                # Если формат номера ок,вызываем функцию, которая проверяет,есть ли номер в reference.
                # Если такой номер телефона уже есть,сообщаем об этом пользователю.Запрашиваем данные заново.
                checking_num = checking_number(reference,number)
                if checking_num == True:
                    print("Такой номер  телефона уже есть!\n")
                    continue
                # Также проверяем,что пользователь не ввёл два одинаковых номера (если добавляет несколько телефонов подряд)
                if number in temp_list_number:
                    print("Такой номер телефона уже есть!\n")
                    continue
                description = (input("Введите описание:\n"))
                temp_dict = {"Описание":description,"Номер":number}
                final_list.append(temp_dict)
                break
            else:
                print("Неверный формат.Номер должен состоять только из цифр и их должно быть 11.Введите номер еще раз\n")
        temp_list_number.append(number)
    # Формируем конечный список с данными ,которые необходимо добавить в справочник
    final_dict = {"Имя":request_name}
    final_dict.setdefault("Телефоны",(final_list))
    reference.append(final_dict)
    # Перезаписываем файл с контактами (добавляем данные,которые ввёл пользователь) 
    with open('task_1_g.json','w',encoding='utf-8') as f:
        json.dump(reference,f,ensure_ascii=False)
    print("Контакт добавлен!")

