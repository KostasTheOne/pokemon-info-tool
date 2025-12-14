import requests

def fetch_pokemon(pokemon_name):
    """Fetch Pokémon data from PokeAPI"""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Pokemon '{pokemon_name}' not found")
    
    return response.json()
