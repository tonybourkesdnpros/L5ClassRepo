import re

output = """
     Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports      Moves   Last Move
----    -----------       ----        -----      -----   ---------
  10    001c.7300.0099    STATIC      Cpu
  10    001c.73c2.c601    STATIC      Po1
  10    001c.73f1.c601    DYNAMIC     Po7        2       0:00:05 ago
Total Mac Addresses for this criterion: 3
"""

# Define the regular expression pattern
pattern = r"\s*(\d+)\s+([0-9a-fA-F.]+)\s+(\w+)\s+(\S+)\s+(\d+)\s+([\d:]+(?: ago)?)"

# Find all matches in the output
matches = re.findall(pattern, output)

# Extract variables from matches
for match in matches:
    vlan = match[0]
    mac_address = match[1]
    entry_type = match[2]
    ports = match[3]
    moves = match[4]
    last_move = match[5]

    # Print variables
    print("VLAN:", vlan)
    print("MAC Address:", mac_address)
    print("Entry Type:", entry_type)
    print("Ports:", ports)
    print("Moves:", moves)
    print("Last Move:", last_move)
    print()  # Add an empty line for better readability