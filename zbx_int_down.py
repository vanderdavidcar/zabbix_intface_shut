import re

def zbx_down_intface():
    with open("zbx_problems_export.csv", "r") as f:
        reader = f.read().splitlines()

    for row in reader:
        if "sw" in row:
            pattern = re.compile(r"Down (?P<intface>\S+)[(]")
            match = pattern.search(str(row))
            ipaddr = match.group("intface")

            if "Vlan" or "Eth" in match:
                print(f'!\ninterface {ipaddr}')
                print('shutdown\n')
                ""
zbx_down_intface()

