# Напишите программу, которая у пользователя запрашивает одно число. Находит
# делители данного числа от 2 до 10 и выводит на экран найденные делители

a = int(input("Введите целое число "))
print(f"Вы ввели {a}")
count = 0
list = []
for i in range(1, a + 1):
    if a % i == 0:
        print(f"Делитель числа  {a} ", ":", i)
        count = count + 1

        if i >= 2 and i <= 10:
            list.append(i)

print(f"Всего делителей {count}")
print(f"Делители числа {a} от 2 до 10 :  {list}")