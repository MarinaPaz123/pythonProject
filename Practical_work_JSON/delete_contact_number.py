#!/usr/bin/python3
from pprint import pprint
import json
from checking_number import checking_number


# Функция удаляет номер телефона.Если номеров несколько,удаляет указанный пользователем
# Если номер только один у данного контакта , контакт удаляется полностью!
def delete_contact_number(reference):
    while True:
        number = (input("Введите телефон без пробелов.Пример: 84955555555\n"))
        # Проверяем ,что пользователь ввёл именно цифры, и их 11
        if number.isdigit() and len(number) == 11:
            # Если формат номера ок,вызываем функцию, которая проверяет,есть ли номер в reference
            # Если номера нет, то удалять нечего.Сообщаем об этом пользователю,запрашиваем заново инфо 
            
            checking_num = checking_number(reference,number)
            if checking_num == None:
                print("Контакт с таким номером не найден!")
                continue
            else:
                for i in reference:
                    for key,val in i.items():
                        if key == "Телефоны":
                            for i2 in val:
                                if i2["Номер"]== number:
                                        i2.clear()
                                
                for i in reference:
                    for key,val in i.items():
                        if key == "Телефоны":
                            if {} in val:
                                val.remove({})
                    if i["Телефоны"] == []:
                        i.clear()
                # Перезаписываем файл. Вписываем обновленные данные        
                with open('task_1_g.json','w',encoding='utf-8') as f:
                    json.dump(reference,f,ensure_ascii=False)
                    print("Номер удалён!")
                break
    
                
                
            
    