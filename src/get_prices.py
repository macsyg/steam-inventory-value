from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

APPID = os.getenv('APP_ID')

appropriate_chars='0123456789.,'

def unpack_from_currency(price_string):
    price = ""
    for char in price_string:
        if char in appropriate_chars:
            price += char
    final_price = price.replace(",", ".")
    try:
        float_price = float(final_price)
        return float_price
    except:
        raise (f"{price_string}")

price_dict = {}

are_items = True
start_index = 0
while are_items:
    print(start_index)
    url = f"https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=name&sort_dir=desc&appid={APPID}&norender=1&count=100&start={start_index}"
    r = requests.get(url)
    resp_json = r.json()

    results = resp_json['results']

    if len(results) != 100:
        are_items = False
        print(results[0]['sale_price_text'])

    for result in results:
        asset_desc = result['asset_description']
        price_dict[asset_desc['classid']] = {
            'name': result['name'],
            'hash_name': result['hash_name'],
            'price': unpack_from_currency(result['sale_price_text'])
        }

    start_index += 100

price_str= json.dumps(price_dict, indent=4)
with open("json_results/price_info.json", "w") as outfile:
    outfile.write(price_str)

print(start_index)