#Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно
#присутствует, замените его на 200 Обновите список только при первом вхождении числа 20

import random

list=[]
count=0
while count < 10:
    a=random.randint(10,20)
    list.append(a)
    count=count+1
print("Сгенерированный список:", list)


c=(list.count(20)) #Проверяем количество вхождений в список числа 20
if c !=0 :
    print("Количество вхождений числа 20 в список: ",c)
    d=list.index(20)  #Задаем переменную со значением индекса числа 20
    list[d]=200 #Заменяем число 20 на 200
    print(list)
else:
    print("В списке нет числа 20! Попробуйте запустить программу еще раз")


#Еще одно решение :
import random

var=0
list=[]

while var < 10:
    a=random.randint(1,10)
    list.append(a)
    var=var+1
print("Сгенерированные числа ", list)

for i in list:
    print("Число", i,"повторяется", list.count(i),"раз(а)")