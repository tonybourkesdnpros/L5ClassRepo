import pyeapi

switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4']

# with open('vlan.txt', 'r') as f:
#     vlan_list = f.read().splitlines()

# Initialize a blank list
vlan_list = []

# Open file
vlan_file = open('vlan.txt', 'r')

# Loop through file, adding each line to the list and stripping the newline off
for line in vlan_file:
    vlan_list.append(line.rstrip())

# Loop through the list of VLANs
for vlan in vlan_list:
    print(f"VLAN: {vlan}")

