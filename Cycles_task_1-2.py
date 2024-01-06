#Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.
#Ограничение: Все задания надо выполнять используя только пройденные темы.
# Эти задания из книги делала еще до Нового Года, поэтому высылаю готовый скрипт с дополнением.

while True:
    error = 0

    ip = (input("Введите ip-адрес: "))
    var = (ip.split("."))
    b = []
    for i in var:
        if i.isdigit() and len(var) == 4:
            b.append(int(i))

        else:

            print("Неправильный ip")
            error = 1
            break

    if error == 1:
        continue

    for i in b:
        if i > 255:
            print("Неправильный ip")
            error = 1
            break
    if error == 1:
        continue
    else:
        break

if b[0] >= 1 and b[0] <= 223:
    print("«unicast»")
elif b[0] >= 224 and b[0] <= 239:
    print("«multicast»")
elif b[0] == 255 and b[1] == 255 and b[2] == 255 and b[3] == 255:
    print("«local broadcast»")
elif b[0] == 0 and b[1] == 0 and b[2] == 0 and b[3] == 0:
    print("«unassigned»")
else:
    print("«unused»")