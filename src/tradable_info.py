from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

STEAMID64 = os.getenv('STEAM_ID')
APPID = os.getenv('APP_ID')


f = open('json_results/inv.json')
r_json = json.load(f)

items_names = {}
for elem in r_json['descriptions']:
    if elem['tradable'] == 1:
        items_names[elem['classid']] = {
            'name': elem['name'],
            'hash_name': elem['market_hash_name']
        }

inv_dict = {}
for elem in r_json['assets']:
    elem_classid = elem['classid']
    if (elem_classid in items_names):
        if (elem_classid not in inv_dict):
            inv_dict[elem_classid] = {
                'name': items_names[elem_classid]['name'],
                'hash_name': items_names[elem_classid]['hash_name'],
                'amount': 1
            }
        else:
            inv_dict[elem_classid]['amount'] += 1


inventory_str = json.dumps(inv_dict, indent=4)
with open("json_results/tradable.json", "w") as outfile:
    outfile.write(inventory_str)