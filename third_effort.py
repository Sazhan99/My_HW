import os
import json

# list of file paths
files = ['ingredients_list.txt', 'ingredients_list1.txt', 'salad_list.txt']

# create list of lists where first element is file length and second element is file path
files_list = [[os.path.getsize(f), f] for f in files]

# sort list by file length
files_list.sort(key=lambda x: x[0])
cook_book = {}



def process_files():
    for file_info in files_list:
        file_length, file_path = file_info
        with open(file_path, 'r') as f:
            dish = None
            ingredients = []
            count = 0
            for line in f:
                if line.strip().isdigit():
                    count = int(line.strip())
                    continue
                elif '|' in line:
                    ingredient = line.strip().split('|')
                    ingredients.append({'ingredient_name': ingredient[0].strip(),
                                        'quantity': int(ingredient[1]),
                                        'measure': ingredient[2].strip()})
                    if len(ingredients) == count:
                        cook_book[dish] = ingredients
                        ingredients = []
                        dish = None
                        count = 0
                else:
                    dish = line.strip()
    return cook_book


def get_ingredients_for_people(dishes, people):
    cook_book = process_files()
    ingredients = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in ingredients:
                ingredients[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * people
            else:
                ingredients[ingredient['ingredient_name']] = {'quantity': ingredient['quantity'
                                                                          ] * people,
                                                              'measure': ingredient['measure']}
    return ingredients


def write_dict_to_file():
    file_name = input("Enter a file name: ") + ".txt"
    o = ""
    for dish, ingredients in cook_book.items():
        o += f"{dish}:\n"
        for ingredient in ingredients:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity']
            o += f"{ingredient_name: <30} {measure: <10} {quantity: <20}\n"
        o += "\n"
    print(o)
    with open(file_name, "w") as file:
        file.write(o)



dishes = ['Яйца фаршерованные', 'Фахитос', 'салат ёжик']
people = 40
ingredients = get_ingredients_for_people(dishes, people)

write_dict_to_file()

