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
        template = 'minecraft:' + template
    print('What is the base? (e.g. diamond_helmet)')
    base = input('> ')
    if ':' not in base:
        base = 'minecraft:' + base
    print('What is the addition? (e.g. iron_ingot)')
    addition = input('> ')
    if ':' not in addition:
        addition = 'minecraft:' + addition
    print('What is the result? (Or press enter to use the base again, e.g. for armor trims)')
    result = input('> ')
    print('Add any item data? (Advanced; read the docs for help!) Or press enter to skip')
    print(
        'Example: Trim:{material:"minecraft:netherite",pattern:"minecraft:vex"}')
    itemdata = input('> ')
    result = (result + '{' + itemdata + '}') if itemdata != '' else base
    print('What is the name of the recipe? (e.g. vex_trimmed_helmet)')
    filename = input('> ').replace('.json', '').replace(' ', '_')
    filename = filename if filename != '' else f'r{randint(0, 999_999)}'

    mkfile(
        f'Projects/{name}/data/{ns}/{"recipes" if pkformat < 48 else "recipe"}/{filename}.json')

    with (open('Engine/Placeholders/crafting.furnace', 'r') as placeholder):
        finaljson = placeholder.read().replace(
            '--TEMPLATE',
            template).replace(
            '--BASE',
            base).replace(
            '--ADD',
            addition).replace(
                '--RESULT',
            result)
        finaljson = finaljson.replace(
            '--ITEM/ID', ('item' if pkformat < 48 else 'id'))

        with open(f'Projects/{name}/data/{ns}/{"recipes" if pkformat < 48 else "recipe"}/{filename}.json',
                  'w') as recipe:
            recipe.write(finaljson)
            print(f'Smithing recipe created with name {filename}!')
