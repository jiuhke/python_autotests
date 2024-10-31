import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '18fe0d281d3bbe4000564db1a31751c5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : '18fe0d281d3bbe4000564db1a31751c5'}
BODYCREATE = {
    'name': 'Бульбазавр',
      'photo_id': 1
}

BODYCHANGE = {
    'pokemon_id': '119520',
    'name': 'буль',
    'photo_id': 2
}

BODYCATCH = {
    "pokemon_id": "119520"
}

create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODYCREATE)

print(create.json)

change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODYCHANGE)

print(change.json)

catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODYCATCH)

print(catch.json)


