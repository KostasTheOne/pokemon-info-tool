from modules.fetch import fetch_pokemon
from modules.parse import parse_pokemon
from modules.visualize import plot_pokemon_stats, type_colors
from termcolor import colored




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