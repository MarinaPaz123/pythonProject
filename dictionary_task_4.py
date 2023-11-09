#Переделать скрипт из задания 3 таким образом, чтобы, при запросе параметра,
#которого нет в словаре устройства, отображалось сообщение 'Такого параметра нет'.
#Задание относится только к параметрам устройств, не к самим устройствам.
#london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    }
}

a=input("Введите название устройства: ")
d=", ".join(london_co[a])
b=input(f"Введите имя параметра: {d}: " )
try:
    print(london_co[a][b])
except KeyError:
    print("Нет такого параметра")