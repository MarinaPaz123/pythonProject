#Переделать скрипт из задания 1a таким образом, чтобы, при запросе
#параметра, отображался список возможных параметров. Список параметров надо
#получить из словаря, а не прописывать вручную.

london_co = {
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
d=", ".join(london_co[a].keys())
b=input(f"Введите имя параметра: {d}  ")
print(london_co[a][b])