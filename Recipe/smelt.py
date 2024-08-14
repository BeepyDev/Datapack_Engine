from random import randint
from Common.makefile import mkfile


def makerecipe(name, ns, pkformat):
    print('Is this recipe for a furnace, smoker, blast furnace, or campfire?')
    furnacetype, method = None, None
    while furnacetype not in ['furnace', 'smoker', 'blast furnace', 'campfire']:
        furnacetype = input('> ').lower()
        if furnacetype in 'furnace':
            method = 'smelting'
        elif furnacetype in 'smoker':
            method = 'smoking'
        elif furnacetype == 'blast furnace':
            method = 'blasting'
        elif furnacetype == 'campfire':
            method = 'campfire_cooking'

    print('What is the ingredient? (e.g. raw_chicken)')
    ingredient = input('> ')
    if ':' not in ingredient:
        ingredient = 'minecraft:' + ingredient
    print('What is the result? (e.g. cooked_chicken)')
    result = input('> ')
    if ':' not in result:
        result = 'minecraft:' + result
    print('How much XP does it reward? (e.g. 0.1) Note: diamond ore, for example, rewards 1')
    xp = input('> ')
    print('How long does it take to smelt in ticks? (e.g. 200) Note: 20 ticks = 1 sec')
    ticks = input('> ')
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
