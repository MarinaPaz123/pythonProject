import re
from pprint import pprint
#Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент имя файла,
#в котором находится вывод команды show ip int br
#Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
# Interface
# IP-Address
# Status
# Protocol
# Информация должна возвращаться в виде списка кортежей

def parse_sh_ip_int_br(file):
    with open(file, 'r') as f:
        final_list =[]
        for i in (f.read().split("\n")):
            match_interface = re.search(r"([F|L]\w+\S+)\s+(.{10})\s+\D{4}\w+\s+(\D{21})\s(.+)", i)

            if match_interface:
                #print(match_interface.group(4))
                final_list.append(match_interface.group(1,2,3,4))
        return(final_list)
result = parse_sh_ip_int_br("sh_ip_int_br.txt")
pprint(result)
