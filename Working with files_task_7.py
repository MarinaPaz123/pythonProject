"""
Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка,
где есть MAC-адрес, должна быть обработана таким образом, чтобы
на стандартный поток вывода была выведена таблица вида:
100 01bb.c580.7000 Gi0/1
200 0a4b.c380.7c00 Gi0/2
300 a2ab.c5a0.700e Gi0/3
10 0a1b.1c80.7000 Gi0/4
"""

with open('CAM_table.txt') as f:
    lines = f.read().split("\n")

    for i in lines:
        b = i.split()
        if b == []:
            continue
        if b[0].isdigit():
            print(b[0], b[1], b[3])
