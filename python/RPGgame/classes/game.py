import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, mag, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = mag
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    # def generate_spell_damage(self, i):
    #     mgl = self.magic[i]["dmg"] - 5
    #     mgh = self.magic[i]["dmg"] + 5
    #     return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(bcolors.BOLD + self.name + bcolors.ENDC)
        print('Actions')
        for item in self.actions:
            print(str(i) + ':' + item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + 'Magic' + bcolors.ENDC)

        for spell in self.magic:
            print(str(i) + ':' + spell.name, '(Cost:', str(spell.cost) + ')')
            i += 1

    def choose_item(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print(str(i) + '.', item['item'].name, ':', item['item'].description, ' (x ' + str(item['quantity']), ')')
            i += 1

    def choose_target(self, enemies):
        i = 1
        print('\n' + bcolors.FAIL + bcolors.BOLD + '    TARGET:' + bcolors.ENDC)

        for enemy in enemies:
            if enemy.get_hp() != 0:
                print('        ' + str(i) + '.' + enemy.name)
                i += 1
        choice = int(input('Choose target:')) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ''
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += '█'
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += ' '

        hp_string = str(self.hp) + '/' + str(self.maxhp)
        current_hp = ''

        if len(hp_string) < 11:
            decrease = 11 - len(hp_string)

            while decrease > 0:
                current_hp += ' '
                decrease -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print('                              __________________________________________________')
        print(bcolors.BOLD + self.name + ':         ' + current_hp + ' |'
              + bcolors.FAIL + hp_bar + bcolors.ENDC + '|')

    def get_stats(self):
        hp_bar = ''
        bar_ticks = (self.hp / self.maxhp) * 100/4

        mp_bar = ''
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += '█'
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += ' '

        while mp_ticks > 0:
            mp_bar += '█'
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += ' '

        hp_string = str(self.hp) + '/' + str(self.maxhp)
        current_hp = ''

        if len(hp_string) < 9:
            decrease = 9 - len(hp_string)

            while decrease > 0:
                current_hp += ' '
                decrease -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + '/' + str(self.maxmp)
        current_mp = ''

        if len(mp_string) < 7:
            decrease = 7 - len(mp_string)

            while decrease > 0:
                current_mp += ' '
                decrease -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print('                            _________________________              __________')
        print(bcolors.BOLD + self.name + ':           ' + current_hp + ' |'
              + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + '|     '
              + current_mp + '|' + bcolors.OKBLUE + mp_bar + bcolors.ENDC + '|')