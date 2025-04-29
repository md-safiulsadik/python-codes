
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"Error ! {response.status_code}")
    else:
        return response.json()

pokemon_name = input("Enter a pokemon name : ").lower()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info is not None:
    
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']] 
    name = pokemon_info['name']
    height = pokemon_info['height']
    weight = pokemon_info['weight']


    print(f"Name : {name.capitalize()}")
    print(f"Height : {height} csm")
    print(f"Weight : {weight} kg")
    print(f"Abilities : {" , ".join(abilities)}")

else:
    print(f"'{pokemon_name}' Pokemon not found")






# print(f"Abilities : {pokemon_info['abilities']['name']}")
# print(f"Base Experience : {pokemon_info['base_experience']}")
# print(f"Cries : {pokemon_info['cries']}")
# print(f"Forms : {pokemon_info['forms']}")
# print(f"Game Indices : {pokemon_info['game_indices']}")
# print(f"Height : {pokemon_info['height']}")
# print(f"Held Items : {pokemon_info['held_items']}")
# print(f"ID : {pokemon_info['id']}")
# print(f"Is Default : {pokemon_info['is_default']}")
# print(f"Location Area Encounters : {pokemon_info['location_area_encounters']}")
# print(f"Moves : {pokemon_info['moves']}")
# print(f"Name : {pokemon_info['name']}")
# print(f"Order : {pokemon_info['order']}")
# print(f"Past Abilities : {pokemon_info['past_abilities']}")
# print(f"Past Types : {pokemon_info['past_types']}")
# print(f"Species : {pokemon_info['species']}")
# print(f"Sprites : {pokemon_info['sprites']}")
# print(f"Stats : {pokemon_info['stats']}")
# print(f"Types : {pokemon_info['types']}")
# print(f"Weight : {pokemon_info['weight']}")

# for key, value in pokemon_info.items():
#     print(f"{key.capitalize().replace('_', ' ')} : {value}")