from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

STEAMID64 = os.getenv('STEAM_ID')
APPID = os.getenv('APP_ID')


r = requests.get(f'http://steamcommunity.com/inventory/{ STEAMID64 }/{ APPID }/2?l=english&count=5000')
r_json = r.json()

json_object = json.dumps(r_json, indent=4)
with open("json_results/inv.json", "w") as outfile:
    outfile.write(json_object)