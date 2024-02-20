import re

with open("zbx_problems_export.csv") as file:
    reader = file.read().splitlines()

print(f'\nInterfaces found on zbx_problems_export.csv file\n')
for row in reader:

    pattern = "Down.([A-z-Z-a]+\s[0-9][^\w\s]\d+|\S+.[\d][(])"
    match = re.findall(pattern, row)

    for intf in match:
        print(f'!\ninterface {intf}')
        print('shutdown')