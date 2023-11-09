# пользователь вводит количество чисел
# number=int(input("Ввведите количество чисел"))
# компьютер генерирует случаное число 1 - 1000
# найти max среди сгенерированных чисел
# найти min среди сгенерированных чисел
# найти среднее среди сгенерированных чисел
# найти количество четных и нечетных чисел  среди сгенерированных чисел




# Вариант со списком
import random

var = int(input("Введите количество чисел "))
list = []
m = 0  # Количество четных
n = 0  # Количество нечетных

i = 0
while i != var:
    rand_num = random.randint(1, 1000)
    list.append(rand_num)

    if rand_num % 2 == 0:
        m = m + 1
    else:
        n = n + 1

    i = i + 1

print("Сгенерированные числа " + str(list))

list_sort = list.copy()
list_sort.sort()

print(list_sort)
print("Минимальное значение: " + str(list_sort[0]))
print("Максимальное значение: " + str(list_sort[-1]))
print("Среднее значение: " + str(sum(list_sort) / var))
print("Количество четных чисел: " + str(m))
print("Количество нечетных чисел: " + str(n))

# Вариант без списка
import random

var = int(input("Введите количество чисел"))

min = 1000
max = 1
sred = 0
m = 0  # Количество четных
n = 0  # Количество нечетных

i = 0
while i != var:
    rand_num = random.randint(1, 1000)
    if rand_num > max:
        max = rand_num
    if rand_num < min:
        min = rand_num
    sred = sred + rand_num

    if rand_num % 2 == 0:
        m = m + 1
    else:
        n = n + 1

    i = i + 1

print("Min: " + str(min))
print("Max: " + str(max))
print("Sred: " + str(sred / var))
print("Количество четных чисел: " + str(m))
print("Количество нечетных чисел: " + str(n))