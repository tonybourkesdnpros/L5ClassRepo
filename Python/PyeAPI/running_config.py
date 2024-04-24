import yaml
import pyeapi


config_file = []

file = open('leaf1.cfg', 'r')
config_file = file.read()

pyeapi.load_config('eapi.conf')

connect = pyeapi.connect_to('leaf1')

connect.enable(['configure replace terminal: '], config_file)
connect.enable(config_file)
# # connect.running_config = file

