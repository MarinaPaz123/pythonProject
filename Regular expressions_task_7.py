import re
#Скопировать функцию get_ip_from_cfg и переделать ее таким образом,
#чтобы она возвращала список кортежей для каждого интерфейса. Если на интерфейсе
#назначен только один адрес, в списке будет один кортеж. Если же на интерфейсе
#настроены несколько IP-адресов, то в списке будет несколько кортежей.


def get_ip_from_cfg(config_r2):
    with open(config_r2, 'r') as f:
        result = {}
        for i in (f.read().split("\n")):
            match_intf = re.search(r"interface\s([A-Z]\w+\S+)", i)
            match_address = re.search(r"\s+\w+\s\w{7}\s(\d+.\d+.\d+.\d)\s(\d+.\d+.\d+.\d+)", i)
            if match_intf:
                interface = match_intf.group(1)
            if match_address:
                address = match_address.group(1, 2)
                if interface not in result:
                    result[interface] = []
                result[interface].append(address)

        return result


result = get_ip_from_cfg("config_r2.txt")
print(result)

