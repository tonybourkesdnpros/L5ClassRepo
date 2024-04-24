#!/usr/bin/python3

import json

file = open('type2.json', 'r')

routes = json.load(file)

mac_routes = set()

for item in routes['evpnRoutes']:
    mac_routes.add(routes['evpnRoutes'][item]['routeKeyDetail']['mac'])

print(mac_routes)
