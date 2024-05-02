#!/usr/bin/python3
from pprint import pprint
import json
from checking_name import checking_name

# Функция удаляет контакт по имени, которое ввёл пользователь
def delete_contact_name(reference):
    while True:
        request_name = input("Введите название контакта\n")
        # Проверяем, что переменная request_name не пустая 
        if len(request_name) == 0:
            print("Значение ""Имя"" не может быть пустым!\n")
            continue
        # Вызываем функцию, которая проверяет, есть ли контакт с таким именем в reference
        # Если такого контакта нет ,то удалять нечего.Сообщаем об этом пользователю
        checking_nam = checking_name(reference,request_name)
        if checking_nam == None:
            print("Контакт с таким именем не найден!")
            break
        
        # Если контакт найден по имени,удаляем соответствующие данные из reference    
        else:
            for i in reference:
                if i["Имя"] == request_name:
                    del i["Имя"]
                    del i["Телефоны"]
                
        break
    
    if {} in reference:
        reference.remove({})
        # Перезаписываем файл
        with open('task_1_g.json','w',encoding='utf-8') as f:
            json.dump(reference,f,ensure_ascii=False)
            print("Контакт удалён!")
    
    
                
    

    
    