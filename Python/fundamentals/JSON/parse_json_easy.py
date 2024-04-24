import json

cmd_output = """
{
    "unicastTable": {
        "tableEntries": [
            {
                "vlanId": 10,
                "macAddress": "00:1c:73:f1:c6:01",
                "entryType": "dynamic",
                "interface": "Port-Channel7",
                "moves": 3,
                "lastMove": 1712125688.9123
            }
        ]
    }
}
"""

json_output_dict = json.loads(cmd_output)
print(json_output_dict['unicastTable']['tableEntries'][0]['macAddress'])
