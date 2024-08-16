from random import randint
from Common.makefile import mkfile


def makerecipe(name, ns, pkformat):
    print('What is the ingredient? (e.g. diamond_boots)')
    ingredient = input('> ')
    if ':' not in ingredient:
        ingredient = 'minecraft:' + ingredient
    print('What is the template? (e.g. vex_armor_smithing_template)')
    template = input('> ')
    if ':' not in template:
        result = 'minecraft:' + template
    print('What is the base? (e.g. diamond_helmet)')
    base = input('> ')
    if ':' not in base:
        result = 'minecraft:' + base
    print('What is the addition? (e.g. iron_ingot)')
    addition = input('> ')
    if ':' not in addition:
        result = 'minecraft:' + addition
    print('What is the result? (e.g. netherite_helmet)')
    print('What is the name of the recipe? (e.g. chicken)')
    filename = input('> ').replace('.json', '').replace(' ', '_')
    filename = filename if filename != '' else f'r{randint(0, 999_999)}'

    mkfile(f'Projects/{name}/data/{ns}/{"recipes" if pkformat < 48 else "recipe"}/{filename}.json')

    with open('Engine/Placeholders/crafting.furnace', 'r') as placeholder:
        finaljson = placeholder.read().replace('--METHOD', method
                                               ).replace('--INGREDIENT', ingredient
                                                         ).replace('--RESULTID', result
                                                                   ).replace('--XP', xp
                                                                             ).replace('--TIME', ticks)
        finaljson = finaljson.replace('--ITEM/ID', ('item' if pkformat < 48 else 'id'))

    with open(f'Projects/{name}/data/{ns}/{"recipes" if pkformat < 48 else "recipe"}/{filename}.json',
              'w') as recipe:
        recipe.write(finaljson)
    print(f'{method.capitalize()} recipe created!')
