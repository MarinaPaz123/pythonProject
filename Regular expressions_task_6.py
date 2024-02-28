import re

#Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким
#образом, чтобы она возвращала словарь:
#ключ: имя интерфейса
#значение: кортеж с двумя строками: IP-адрес,маска
#В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

def get_ip_from_cfg(config_r1):
    with open(config_r1, 'r') as f:
        result = {}
        for i in (f.read().split("\n")):
            match_intf = re.search(r"interface\s([A-Z]\w+\S+)", i)
            match_address = re.search(r"\s+\w+\s\w{7}\s(\d+.\d+.\d+.\d)\s(\d+.\d+.\d+.\d+)", i)
            if match_intf:
                interface = match_intf.group(1)
            if match_address:
                address = match_address.group(1,2)
                result[interface]= address
        return result

result = get_ip_from_cfg("config_r1.txt")
print(result)
