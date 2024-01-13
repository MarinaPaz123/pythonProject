def config_interface(intf_name, ip_address, mask):
    interface = f'interface {intf_name}'
    no_shut = 'no shutdown'
    ip_addr = f'ip address {ip_address} {mask}'
    result = [interface, no_shut, ip_addr]
    return result

config_interface('Fa0/1', '10.0.1.1', '255.255.255.0')