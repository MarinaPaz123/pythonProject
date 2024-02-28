import ipaddress

def protocol_request():
    list_dst_ports = []

    while True:
        protocol = (input("Введите название протокола (tcp,udp,ip,icmp)" + "\n"))
        if protocol != "tcp" and protocol != "udp" and protocol != "ip" and protocol != "icmp":
            print("Неверное название протокола!Введите что -то из : tcp,udp,ip,icmp: ")
            continue

        print("ok")
        break
    if protocol == "udp" or protocol == "tcp":
        while True:
            dst_posts = (input(
                "Введите dst порты, например : " + "\n" + "Если порт один - 443" + "\n" + "Если портов несколько,вводите через пробел  - 443 80 8080" + "\n"))
            temp_dst_posts = dst_posts.split()
            try:
                for i in temp_dst_posts:
                    var = (int(i))
                    list_dst_ports.append(var)
                break
            except ValueError:
                print("Неверный формат! ")
        print("вот список портов",list_dst_ports)
        return list_dst_ports


list_src_subnet = []
list_dst_subnet = []

while True:
    try:
        request_src = (int(input("Сколько src сетей? Введите число: " + "\n")))
        break
    except ValueError:
        print("Введите целое число!")
        continue

for i in range(1, request_src + 1):
    while True:
        src_subnet = (input(f"Введите {i} src subnet или host, например 8.8.8.8 или 8.8.8.0/23 или any" + "\n"))
        try:
            temp_src = ipaddress.ip_network(src_subnet)
            if not temp_src.is_global or temp_src.is_multicast or temp_src.is_reserved:
                print("Введите публичную subnet! ")
                continue
            list_src_subnet.append(src_subnet)
            break
        except ValueError:
            if src_subnet == "any":
                list_src_subnet.append(src_subnet)
                break
            else:
                print("Неверное значение ip или subnet. Введите данные ещё раз! ")
###########################################
while True:
    try:
        request_dst = (int(input("Сколько dst сетей? Введите число: " + "\n")))
        break
    except ValueError:
        print("Введите целое число!")
        continue

for i in range(1, request_dst + 1):
    while True:
        dst_subnet = (input(f"Введите {i} dst subnet или host, например 8.8.8.8 или 8.8.8.0/23 или any" + "\n"))
        try:
            temp_dst = ipaddress.ip_network(dst_subnet)
            if not temp_dst.is_global or temp_dst.is_multicast or temp_dst.is_reserved:
                print("Введите публичную subnet! ")
                continue
            count = 0
            for var in list_src_subnet:
                if var == "any":
                    break
                a = ipaddress.ip_network(var)
                if a.overlaps(temp_dst):
                    count = count + 1
            if count > 0:
                print("src и dst пересекаются !!!")
                continue
            list_dst_subnet.append(dst_subnet)
            print("ок")
            list_dst_ports = protocol_request()
            fff = list_dst_ports + list_dst_subnet
            break


        except ValueError:
            if dst_subnet == "any":
                list_dst_subnet.append(dst_subnet)
                break
            else:
                print("Неверное значение ip или subnet. Введите данные ещё раз! ")


print(fff)

##############################


