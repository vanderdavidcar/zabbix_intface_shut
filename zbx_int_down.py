import re

def zbx_down_intface():
    with open("zbx_problems_export.csv", "r") as f:
        reader = f.read().splitlines()

    print(f'\nInterfaces found on zbx_problems_export.csv file\n')
    for row in reader:
        # Condition to find specific device hostname "zbx_problems_export.csv" file
        if "sw" in row:
            # Regex to find only the interfaces
            pattern = re.compile(r"Down (?P<intface>\S+)[(]")
            match = pattern.search(str(row))
            ipaddr = match.group("intface")

            # Condition to find Vlan ou Eth interfaces into variable
            if "Vlan" or "Eth" in match:
                print(f'interface {ipaddr}')
                print('shutdown\n!')
                ""
zbx_down_intface()

