import re

filenames = ["sw1_dhcp_snooping.txt","sw2_dhcp_snooping.txt","sw3_dhcp_snooping.txt"]
output = "result.csv"


def write_dhcp_snooping_to_csv(filenames, output):
    test = [["switch", "mac", "ip", "vlan", "interface"]]
    for i in filenames:
        data = []
        match_name_sw = re.search(r"(\w\w\d+)", i)
        if match_name_sw:
            data.append(match_name_sw.group(0))
        with open(i) as f:
            for line in f:
                print("ляля", line)
                # match = re.search(r"(\w\w\w\w\:\w\w\w\w\:\w\w\w\w).+", line)
                # if match:
                # print(match.group())


write_dhcp_snooping_to_csv(filenames, output)







