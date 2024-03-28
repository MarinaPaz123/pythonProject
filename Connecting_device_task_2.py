from pprint import pprint
from netmiko import ConnectHandler

#Создать функцию send_commands (для подключения по SSH используется netmiko).
#Параметры функции:
# device - словарь с параметрами подключения к одному устройству
# show - одна команда show (строка)
# config - список с командами, которые надо выполнить в конфигурационном режиме

R1 = {'device_type': 'cisco_ios',
'ip': '192.168.10.19',
'username': 'cisco',
'password': 'cisco',
'secret': 'cisco'}


R2 = {'device_type': 'cisco_ios',
'ip': '192.168.10.18',
'username': 'cisco',
'password': 'cisco',
'secret': 'cisco'}

commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
command = "sh ip int br"

def send_show_command(device,command):
    ssh = ConnectHandler(**device)
    ssh.enable()
    result = ssh.send_command(command)
    return result

def send_config_commands(device,config_commands):
    connection = ConnectHandler(**device)
    connection.enable()
    result = connection.send_config_set(config_commands)
    connection.disconnect()
    return result



def send_commands(device,*,show = None,config = None):
    if show and config:
        raise ValueError("Несоответствующее значение")

    if show:
        if show != None:
            result_sh = send_show_command(device,show)
            return result_sh
    if config:
        if config != None:
            result_conf = send_config_commands(device,config)
            return result_conf



final  = send_commands(R2,config = commands)
print(final)




