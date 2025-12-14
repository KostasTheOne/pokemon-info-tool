def parse_pokemon(data):
    """Parse API data into structured dictionary"""
    name = data["name"]
    types = [t["type"]["name"] for t in data["types"]]
    abilities = [a["ability"]["name"] for a in data["abilities"]]
    
    stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}

    return {
        "name": name,
        "types": types,
        "abilities": abilities,
        "stats": stats
    }
