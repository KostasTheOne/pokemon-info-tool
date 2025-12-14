import matplotlib.pyplot as plt

type_colors= {
    "normal": "white", "fire": "red", "water": "blue", "electric": "yellow",
    "grass": "green", "ice": "cyan", "fighting": "magenta", "poison": "magenta",
    "ground": "yellow", "flying": "cyan", "psychic": "magenta", "bug": "green",
    "rock": "yellow", "ghost": "magenta", "dragon": "blue", "dark": "white",
    "steel": "white", "fairy": "magenta"
}

def plot_pokemon_stats(pokemon):
    stats = pokemon['stats']
    plt.figure(figsize=(8,4))
    plt.bar(stats.keys(), stats.values(), color='skyblue')
    plt.title(f"{pokemon['name'].capitalize()} Stats")
    plt.ylabel("Base Stat")
    plt.show()


