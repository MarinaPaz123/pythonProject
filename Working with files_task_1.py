#Создайте файл nums.txt, содержащий несколько чисел,
#записанных через пробел. Напишите программу, которая подсчитывает и
#выводит на экран общую сумму чисел, хранящихся в этом файле.

# file :
# 2 5 8 6 9

temp_list = []
f = open("nums.txt")
a = f.read().split()
for i in a:
    temp_list.append(int(i))

print(sum(temp_list))

