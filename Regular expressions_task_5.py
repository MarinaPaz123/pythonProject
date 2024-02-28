import re
#Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски, которые
#настроены на интерфейсах, в виде списка кортежей:
#первый элемент кортежа - IP-адрес
#второй элемент кортежа - маска

def get_ip_from_cfg(config_r1):
    with open(config_r1, 'r') as f:
        ip_mask = []
        for i in (f.read().split("\n")):
            match = re.search(r"\s+\w+\s\w{7}\s(\d+.\d+.\d+.\d)\s(\d+.\d+.\d+.\d+)", i)
            if match:
                ip_mask.append(match.group(1, 2))

        return ip_mask


result = get_ip_from_cfg("config_r1.txt")
print(result)
