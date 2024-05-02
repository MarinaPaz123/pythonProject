#!/usr/bin/python3
from pprint import pprint
import json
from loading import loading
from find_tel import find_tel
from find_name import find_name
from add_contact import add_contact
from delete_contact_name import delete_contact_name
from delete_contact_number import delete_contact_number
from save_file import save_file




def main():
    with open('task_1_g.json') as f:
        reference = json.load(f)
    f.close()
    # Спрашиваем у пользователя, что требуется сделать
    while True:
        request = (input("1- Загрузить инфо\n2- Поиск по телефону\n3- Поиск по имени\n4- Добавить контакт\n5- Удалить контакт по имени\n6- Удалить телефон\n7- Сохранить справочник в файл\n"))
        # Проверяем,что пользователь ввёл именно число!
        if request.isdigit():
            request = int(request)
            break
        else:
            print("Неверное значение! Введите число\n")
        break
    # В зависимости от того,какое число ввёл пользователь, вызываем соответствующую функцию
    if request == 1:
        loading(reference)
    elif request == 2:
        find_tel(reference)
    elif request == 3:
        find_name(reference)
    elif request == 4:
        add_contact(reference)
    elif request == 5:
        delete_contact_name(reference)
    elif request == 6:
        delete_contact_number(reference)
    elif request == 7:
        save_file(reference)
    else:
        print("Введите число от 1 до 7")
    




if __name__ == "__main__":
    main()