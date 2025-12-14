from fetch import fetch_pokemon
from parse import parse_pokemon
import requests


all_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1000").json()
pokemon_list = [p['name'] for p in all_pokemon['results']]


def filter_pokemon_by_type(pokemon_names, type_name):
    result = []
    for name in pokemon_names:
        try:
            data = fetch_pokemon(name)
            parsed = parse_pokemon(data)
            if type_name in parsed["types"]:
                result.append(parsed["name"])
        except (requests.exceptions.RequestException, ValueError):
            continue
    return result

fire_pokemon = filter_pokemon_by_type(pokemon_list[:100], "fire")
print(fire_pokemon)
