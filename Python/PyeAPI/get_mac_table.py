import pyeapi

connect = pyeapi.connect_to('leaf1')
cmd_result = connect.enable('show mac address-table')
mac_table_dict = cmd_result[0]['result']['unicastTable']['tableEntries']
mac_table_set = set()
for mac in mac_table_dict:
    mac_table_set.add(mac['macAddress'])

for mac_address in mac_table_set:
    print(mac_address)