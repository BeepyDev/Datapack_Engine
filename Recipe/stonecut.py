from random import randint
from Common.makefile import mkfile


def makerecipe(name, ns, pkformat):
    print('What is the ingredient? (e.g. stone)')
    ingredient = input('> ')
    if ':' not in ingredient:
        ingredient = 'minecraft:' + ingredient
    print('What is the result? (e.g. stone_slab)')
    result = input('> ')
    if ':' not in result:
        result = 'minecraft:' + result
    print(f'How many {result.split(":")[1]} does it yield?')
    amount = input('> ')
    print('What is the name of the recipe? (e.g. stone_to_slabs)')
    filename = input('> ').replace('.json', '').replace(' ', '_')

    filename = filename if filename != '' else f'r{randint(0, 999_999)}'

    is48up = '48up' if pkformat >= 48 else 'pre48'

    with open(f'Engine/Placeholders/crafting.cut.{is48up}', 'r') as placeholder:
        finaljson = placeholder.read().replace(
            '--INGREDIENT',
            ingredient).replace(
            '--RESULTID',
            result).replace(
            '--AMOUNT',
            amount)

    mkfile(
        f'Projects/{name}/data/{ns}/{"recipes" if pkformat < 48 else "recipe"}/{filename}.json')
    with open(f'Projects/{name}/data/{ns}/{"recipes" if pkformat < 48 else "recipe"}/{filename}.json',
              'w') as recipe:
        recipe.write(finaljson)

    print(f'Stonecutting recipe created with name {filename}!')
