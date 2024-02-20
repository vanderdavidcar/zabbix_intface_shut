import re

with open("zbx_problems_export.csv") as file:
    reader = file.read().splitlines()

for row in reader:
    pattern = "Down.([A-z-Z-a]+\s[0-9][^\w\s]\d+|\S+.[\d]+)"
    match = re.findall(pattern, row)

    for intf in match:
        print(f'!\ninterface {intf}')
        print('shutdown')