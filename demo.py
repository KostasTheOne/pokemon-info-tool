from fetch import fetch_pokemon
from parse import parse_pokemon
from visualize import plot_pokemon_stats, display_colored_types
from termcolor import colored

type_colors= {
    "normal": "white", "fire": "red", "water": "blue", "electric": "yellow",
    "grass": "green", "ice": "cyan", "fighting": "magenta", "poison": "magenta",
    "ground": "yellow", "flying": "cyan", "psychic": "magenta", "bug": "green",
    "rock": "yellow", "ghost": "magenta", "dragon": "blue", "dark": "white",
    "steel": "white", "fairy": "magenta"
}


def main():
    while True:
        name = input("Enter Pokemon name (or 'exit' to quit): ").strip()
        if name.lower() == "exit":
            print("Goodbye!")
            break
    
        try:
            data = fetch_pokemon(name)
            pokemon = parse_pokemon(data)

            print("\n=== Pokémon Info ===")
            print(f"Name: {pokemon['name']}")
            colored_types = [colored(t, type_colors.get(t, "white")) for t in pokemon['types']]
            print(f"Types: {', '.join(colored_types)}")
            print(f"Abilities: {', '.join(pokemon['abilities'])}")
            print("Stats:")
            for stat, value in pokemon['stats'].items():
                print(f"  {stat}: {value}")
            print("===================\n")

        except ValueError as e:
            print(e)
        except Exception as e:
            print("An unexpected error occurred:", e)
        
        plot_pokemon_stats(pokemon)

if __name__ == "__main__":
    main()