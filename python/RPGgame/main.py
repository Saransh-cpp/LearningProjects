from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

print('\n\n')

fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('Quake', 14, 140, 'black')

cure = Spell('Cure', 12, 120, 'white')
cura = Spell('Cura', 18, 200, 'white')

potion = Item('Potion', 'potion', 'Heals 50 HP', 50)
hipotion = Item('Hi-Potion', 'potion', 'Heals 100 HP', 100)
superpotion = Item('Super Potion', 'potion', 'Heals 500 HP', 500)
elixir = Item('Elixir', 'elixir', 'Fully restores HP/MP of one party member', 9999)
hielixir = Item('Elixir', 'elixir', "Fully restores HP/MP party's member", 9999)

grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)

player_spells = [fire, thunder, blizzard, blizzard, meteor, cure, cura]
player_items = [{'item': potion, 'quantity': 15}, {'item': hipotion, 'quantity': 5},
                {'item': superpotion, 'quantity': 5}, {'item': elixir, 'quantity': 5},
                {'item': hielixir, 'quantity': 5}, {'item': grenade, 'quantity': 5}]

player1 = Person('Valos', 460, 65, 60, 34, player_spells, player_items)
player2 = Person('Nick ', 460, 65, 60, 34, player_spells, player_items)
player3 = Person('Robot', 460, 65, 60, 34, player_spells, player_items)

enemy = Person('Magneto', 1200, 65, 45, 25, [], [])

players = [player1, player2, player3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "ALL ENEMY ATTACKS!" + bcolors.ENDC)


while running:
    print('================================================')
    print('NAME                      HP                                    MP')
    for player in players:
        player.get_stats()

    print('\n\n')

    for player in players:
        player.choose_action()
        choice = input('Choose Action\n')
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print('You attacked for', dmg, 'points of damage')
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:\n")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + '\nNot enough MP\n' + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + '\n' + spell.name + " heals for", str(magic_dmg), "HP" + bcolors.ENDC)
            elif spell.type == 'black':
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + '\n' + spell.name + ' deals ' + str(magic_dmg), 'point of damage' + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input('Choose item:\n')) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]['item']

            if player.items[item_choice]['quantity'] == 0:
                print(bcolors.FAIL + '\n' + 'None left....' + bcolors.ENDC)
                continue

            player.items[item_choice]['quantity'] -= 1

            if item.type == 'potion':
                player.heal(item.prop)
                print(bcolors.OKGREEN + '\n' + item.name + ' heals for', str(item.prop), 'HP' + bcolors.ENDC)
            elif item.type == 'elixir':
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + '\n' + item.name + 'fully restores HP/MP' + bcolors.ENDC)
            elif item.type == 'attack':
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + '\n' + item.name + ' deals', str(item.prop), 'points of damage', bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print('Enemy attacks for', enemy_dmg)

    print('=================================================')
    print('Enemy HP:', bcolors.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + bcolors.ENDC + '\n')

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + 'You Win!' + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + 'Your enemy has defeated you!' + bcolors.ENDC)
        running = False






