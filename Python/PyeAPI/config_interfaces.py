import yaml
import pyeapi

file = open('interfaces.yml', 'r')

print(type(file))
interface_dict = yaml.safe_load(file)

for switch in interface_dict['devices']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    int_api = connect.api('ipinterfaces')
    for interface in interface_dict['devices'][switch]['interfaces']:
        ip = interface_dict['devices'][switch]['interfaces'][interface]['ip']
        mask = interface_dict['devices'][switch]['interfaces'][interface]['mask']
        mask = str(mask)
        ip_mask = ip+"/"+mask
        int_api.create(interface)
        int_api.set_address(interface, ip_mask)
        print(interface, ip_mask)
