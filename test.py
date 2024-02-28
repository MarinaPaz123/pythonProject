import re
from sys import argv
from pprint import pprint
def parse_sh_ip_int_br():
    with open("sh_ip.txt", 'r') as f:
        final_list =[]
        for i in (f.read().split("\n")):
            match_interface = re.search(r"([F|L]\w+\S+)\s+(.{10})\s+\D{4}\w+\s+(\D{21})\s(.+)", i)

            if match_interface:
                #print(match_interface.group(4))
                final_list.append(match_interface.group(1,2,3,4))
        pprint(final_list)


parse_sh_ip_int_br()








