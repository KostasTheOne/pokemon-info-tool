import matplotlib.pyplot as plt

def plot_pokemon_stats(pokemon):
    stats = pokemon['stats']
    plt.figure(figsize=(8,4))
    plt.bar(stats.keys(), stats.values(), color='skyblue')
    plt.title(f"{pokemon['name'].capitalize()} Stats")
    plt.ylabel("Base Stat")
    plt.show()


