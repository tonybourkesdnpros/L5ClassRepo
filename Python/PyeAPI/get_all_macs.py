import pyeapi

switches = ['leaf1', 'leaf2', 'leaf3', 'leaf3', 'borderleaf1', 'borderleaf2']
mac_table_set = set()

for switch in switches:
    connect = pyeapi.connect_to(switch)
    cmd_result = connect.enable('show mac address-table')
    mac_table_dict = cmd_result[0]['result']['unicastTable']['tableEntries']
    for mac in mac_table_dict:
        mac_table_set.add(mac['macAddress'])

print("The following are unique MAC addresses in the fabric")
for mac_address in mac_table_set:
    print(mac_address)
