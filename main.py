from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('-------------')
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.getter_type()}: {e1.health_points} HP left")
        print(f"{e2.getter_type()}: {e2.health_points} HP left")
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage
        print('-------------')

    if e1.health_points > 0:
        print(f'{e1.getter_type()} wins!')
    else:
        print(f'{e2.getter_type()} wins!')


def hero_battle(hero: Hero, enemy: Enemy):
    enemy.talk()
    while hero.health_points > 0 and enemy.health_points > 0:
        print('-------------')
        zombie.special_attack()
        print(f'Hero: {hero.health_points} HP left')
        print(f"{zombie.getter_type()}:{zombie.health_points} HP left")
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage
        print('-------------')

    if hero.health_points > 0:
        print('Hero wins!')
    else:
        print(f'{enemy.getter_type()} wins!')

zombie = Zombie(10, 1)
print(zombie.getter_type())
ogre = Ogre(20, 3)
hero = Hero(20, 1)

weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()


hero_battle(hero, ogre)
