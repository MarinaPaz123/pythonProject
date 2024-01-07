trunk_template = [
"switchport trunk encapsulation dot1q",
"switchport mode trunk",
"switchport trunk allowed vlan",
]

trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for key, val in trunk.items():
    vlan_str = ''
    print(f"interface FastEthernet{key}")
    print(trunk_template[0])
    print(trunk_template[1])

    for i in range(1,len(val)):
        vlan_str = vlan_str + "," + val[i]

    if val[0] == 'add':
        print(trunk_template[2] + " add " + vlan_str[1:])
    if val[0] == 'only':
        print(trunk_template[2] + " " + vlan_str[1:])
    if val[0] == 'del':
        print(trunk_template[2] + " remove " + vlan_str[1:])
