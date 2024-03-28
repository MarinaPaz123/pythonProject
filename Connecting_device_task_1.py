from netmiko import ConnectHandler

#Функция подключается по SSH (с помощью netmiko) к одному устройству
# и выполняет перечень команд в конфигурационном режиме на основании переданных аргументов.

R1 = {'device_type': 'cisco_ios',
'ip': '192.168.10.19',
'username': 'cisco',
'password': 'cisco',
'secret': 'cisco'}

commands =  ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']






def send_config_commands(device,config_commands):
    connection = ConnectHandler(**device)
    connection.enable()
    result = connection.send_config_set(config_commands)
    connection.disconnect()
    return result

result = send_config_commands(R1,commands)
print(result)



