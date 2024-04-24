import pyeapi

switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4', 'spine1', 'spine2', 'spine3', 'spine4', 'borderleaf1', 'borderleaf2']

for switch in switches:
    print(f"Configuring {switch}")
    node = pyeapi.connect_to(switch)
    node.api('ipinterfaces').create('Ethernet1')

