#Напишите программу, которая запрашивает у пользователя три числа в диапазоне
#1-1000. Компьютер генерирует два случайных числа в диапазоне 1-100, которые
#определяют отрезок. Определить какие числа указанные пользователям попали в
#отрезок.

import random

list1 = []
count = 1
while count != 4:
    try:
        a = int(input(f"введите {count} целое число от 1 до 1000 "))
        list1.append(a)
        print("Данные введены верно: ", a)
        count = count + 1
    except ValueError:
        print("Вы ввели неверные данные,попробуйте еще раз ")

var = random.randint(1, 100), random.randint(1, 100)
print("Вы ввели ", list1)
var2 = list(var)
var2.sort()
print(f"Сгенерированные числа {var2}")

for i in list1:
    if i > var2[0] and i < var2[1]:
        print(f"{i} входит в отрезок")
    else:
        print(f"{i} не входит в отрезок")