import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '18fe0d281d3bbe4000564db1a31751c5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : '18fe0d281d3bbe4000564db1a31751c5'}
TRAINER_ID = '7221'

response_get = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})    
print(response_get.text)