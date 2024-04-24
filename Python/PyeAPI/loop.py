import yaml

file = open('interfaces.yml', 'r')

interfaces = yaml.safe_load(file)

for interface in interfaces['devices']['leaf1']['interfaces']:
            print(f"Interface: {interface}")
            print(f"IP: {interfaces['devices']['leaf1']['interfaces'][interface][0]['ip']}/{interfaces['devices']['leaf1']['interfaces'][interface][0]['mask']}")