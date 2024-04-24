import pyeapi
import json

# Establish eAPI connection to leaf1
connect = pyeapi.connect_to('leaf1')
# Send command 'show mac address-table' to switch
# The result is a dictionary (cmd_result) with dictionaries inside
cmd_result = connect.enable(['show mac address-table', 'show ip interface brief'])
print(cmd_result)
