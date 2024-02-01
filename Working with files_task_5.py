"""
Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:
Prefix 10.0.24.0/24
AD/Metric 110/41
Next-Hop 10.0.13.3
Last update 3d18h
Outbound Interface FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

with open('ospf.txt') as f:
    a = f.readlines()
    for i in a:
        b = i.split()
        print("Prefix ", b[1])
        print("AD/Metric ", b[2][1:-1])
        print("Next-Hop ", b[4].replace(',', ''))
        print("Last update ", b[-2].replace(',', ''))
        print("Outbound Interface ", b[-1])
        print("-" * 10)
