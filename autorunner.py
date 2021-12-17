import yaml
import sys
import os

with open(r'creds.yaml') as file:
   creds = yaml.load(file, Loader=yaml.FullLoader)

for i in range(0,len(creds['usernames'])):
    os.system(f"python main.py {creds['usernames'][i]} {creds['passwords'][i]} ")