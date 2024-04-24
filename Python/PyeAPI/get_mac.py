import pyeapi
leafs = ['leaf1', 'leaf2', 'leaf3', 'leaf4']
mac_table_set = set()
for leaf in leafs:
    connect = pyeapi.connect_to(leaf)
    cmd_result = connect.enable('show mac address-table')
    unicast_table = cmd_result[0]['result']
    mac_table_dict = cmd_result[0]['result']['unicastTable']['tableEntries']
    for mac in mac_table_dict:
        mac_table_set.add(mac['macAddress'])
for mac_entry in mac_table_set:
    print(mac_entry)
