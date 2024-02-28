import re

# список с названиями полей
headers = ["hostname", "ios", "platform"]

#  список кортежей со значениями
data = [
    ("R1", "12.4(24)T1", "Cisco 3825"),
    ("R2", "15.2(2)T1", "Cisco 2911"),
    ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"), ]


# Функция возвращает результат в виде списка словарей, где ключи - взяты из первого списка,
# а значения подставлены из второго

def convert_to_dict(headers, data):
    final_list = []
    for i in range(0, len(headers), 3):
        temp_host = headers[i]
        temp_ios = headers[i + 1]
        temp_platform = headers[i + 2]
        for var in data:
            match_host = re.search(r"([R|S]\w+).+", str(var))
            if match_host:
                match_host = (match_host.group(1))
                final_dict = {}
                final_dict[temp_host] = match_host
            match_ios = re.search(r"\w+\D+\s+(\D\d+[.]\d+\S+)", (str(var)))
            if match_ios:
                match_ios = match_ios.group(1)
                final_dict[temp_ios] = match_ios
            match_platform = re.search(r"\w+\D+\s+\D\d+[.]\d+\S+(.+)[']", (str(var)))
            if match_platform:
                match_platform = match_platform.group(1)
                final_dict[temp_platform] = match_platform
            final_list.append(final_dict)
    return final_list


result = convert_to_dict(headers, data)
print(result)


