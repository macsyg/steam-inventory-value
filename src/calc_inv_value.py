from dotenv import load_dotenv
import requests
import os
import json
import time

load_dotenv()

APPID = os.getenv('APP_ID')

APPROPRIATE_CHARS='0123456789.,'
KEY_PHRASES=['case', 'capsule']

def unpack_from_currency(price_string):
    price = ""
    for char in price_string:
        if char in APPROPRIATE_CHARS:
            price += char
    final_price = price.replace(",", ".")
    return float(final_price)


def should_be_included(name):
    if not KEY_PHRASES:
        return True
    else:
        for key_phrase in KEY_PHRASES:
            if key_phrase in name:
                return True
        return False


f = open('json_results/tradable.json')
data = json.load(f)

inv_value = 0.0
for k in data:
    dict_elem = data[k]
    if should_be_included(dict_elem['name'].lower()):
        hash_name = dict_elem['hash_name']
        r = requests.get(
            f'https://steamcommunity.com/market/priceoverview/?country=PL&currency=1&appid={APPID}&market_hash_name={hash_name}'
        )
        result = r.json()
        print(hash_name, result)
        try:
            if result['success']:
                income = unpack_from_currency(result['lowest_price']) * 0.85
                inv_value += income * dict_elem['amount']
        except:
            pass
        
        time.sleep(0.5)

print(inv_value)