import pyeapi

pyeapi.load_config('eapi.conf')

connect = pyeapi.connect_to('leaf1')

running_config_raw = connect.get_config()
running_config = []
for line in running_config_raw:
    print(line)

# print(running_config)