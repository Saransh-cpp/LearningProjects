from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

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
hielixir = Item('MegaElixir', 'elixir', "Fully restores HP/MP party's member", 9999)

grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)

player_spells = [fire, thunder, blizzard, blizzard, meteor, cure, cura]
player_items = [{'item': potion, 'quantity': 15}, {'item': hipotion, 'quantity': 5},
                {'item': superpotion, 'quantity': 5}, {'item': elixir, 'quantity': 5},
                {'item': hielixir, 'quantity': 5}, {'item': grenade, 'quantity': 5}]

player1 = Person('Valos', 500, 65, 60, 34, player_spells, player_items)
player2 = Person('Nick ', 500, 65, 60, 34, player_spells, player_items)
player3 = Person('Robot', 500, 65, 60, 34, player_spells, player_items)

enemy2 = Person('Magneto', 1200, 65, 215, 25, [], [])
enemy1 = Person('Imp    ', 120, 10, 300, 325, [], [])
enemy3 = Person('Imp    ', 120, 10, 300, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "ALL ENEMY ATTACKS!" + bcolors.ENDC)


while running:
    print('================================================')
    print('NAME                      HP                                    MP')
    for player in players:
        player.get_stats()

    print('\n')

    for enemy in enemies:
        enemy.get_enemy_stats()

    print('\n\n')

    for player in players:
        player.choose_action()
        choice = input('Choose Action\n')
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print('You attacked' + enemies[enemy].name.replace(' ', '') + ' for', dmg, 'points of damage')

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(' ', '') + ' has died.')
                del enemies[enemy]

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
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + '\n' + spell.name + ' deals ' + str(magic_dmg), 'point of damage to '
                      + enemies[enemy].name.replace(' ', '') + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(' ', '') + ' has died.')
                    del enemies[enemy]

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

                if item.name == 'MegaElixir':
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + '\n' + item.name + 'fully restores HP/MP' + bcolors.ENDC)
            elif item.type == 'attack':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + '\n' + item.name + ' deals', str(item.prop), 'points of damage to '
                      + enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(' ', '') + ' has died.')
                    del enemies[enemy]

    enemy_choice = 1
    target = random.randrange(0, 3)
    enemy_dmg = enemies[0].generate_damage()
    players[target].take_damage(enemy_dmg)
    print('Enemy attacks for', enemy_dmg)

    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    if defeated_enemies == 2:
        print(bcolors.OKGREEN + 'You Win!' + bcolors.ENDC)
        running = False
    elif defeated_players == 2:
        print(bcolors.FAIL + 'Your enemies has defeated you!' + bcolors.ENDC)
        running = False






