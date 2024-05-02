#!/usr/bin/python3
from pprint import pprint
import json


# Функция сохраняет reference в отдельный файл
def save_file(reference):
    with open('reference.json','w') as file:
        json.dump(reference,file,ensure_ascii=False,indent=4)
    print("Информация сохранена в файл reference.json")
    
        
    
