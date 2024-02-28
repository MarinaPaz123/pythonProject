import re
from pprint import pprint
#Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
#из синтаксиса cisco IOS в cisco ASA.
#Функция ожидает такие аргументы:
# имя файла, в котором находится правила NAT Cisco IOS
# имя файла, в который надо записать полученные правила NAT для ASA

def convert_ios_nat_to_asa(cisco_nat_config,ASA):
    asa_template = """object network LOCAL_{}
    host {}
    nat (inside,outside) static interface service tcp {}"""
    f_dst = open(ASA,"w")
    f_src = open(cisco_nat_config)
    for i in f_src:
        match_ip = re.search(r".(\d+[.]\d+[.]\d+[.]\d+).+",i)
        if match_ip:
            match_ip = match_ip.group(1)
        match_ports = re.search(r"\D+\d+\.\d+\.\d+\.\d+\s+(\d+)\s+\w+\s+\w+\D\d+\s+(\d+)",i)
        if match_ports:
            src_port = (match_ports.group(1))
            dst_port = (match_ports.group(2))
            ports_all = src_port + " " + dst_port
            for var in asa_template.split("\n"):
                if "object" in var or "host" in var:
                    f_dst.writelines(var.format(match_ip)+"\n")
                if "nat" in var:
                    f_dst.writelines(var.format(ports_all)+"\n")
    print("Успешно")
    f_dst.close()
    f_src.close()

convert_ios_nat_to_asa("cisco_nat_config.txt","ASA.txt")


