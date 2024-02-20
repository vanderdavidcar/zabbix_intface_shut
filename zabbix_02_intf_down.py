from itertools import groupby
from operator import itemgetter
from csv import DictReader
import re

with open(f'zbx_problems_export.csv') as file:
    rows = DictReader(file)


    for problem, groups in groupby(rows, key=itemgetter('Problem')):
        hosts = list(row['Host'] for row in groups)
        
        pattern = "Down.([A-z-Z-a]+\s[0-9][^\w\s]\d+|\S+.[\d]+)"
        match = re.findall(pattern, problem)
        
        #print(f"Hosts: {hosts} and Interface: {match}")
        for intf in match:
            print(f'!\ninterface {intf}')
            print('shutdown')