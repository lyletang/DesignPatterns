# -*- coding: utf-8 -*-
# author: lyletang
# date: 2017-11-30

"""Python 3 Patterns & Idioms(Bruce Eckel著)一书中的例子。
   包含两个游戏，一个面向孩子，一个面向成人。
   在运行时，基于用户输入，决定该创建那个游戏并运行。游戏创建部分由一个抽象工厂维护。
   
   孩子的游戏名：FrogWorld
   doc：一只青蛙，喜欢吃虫子

   成人的游戏名：WizardWord
   doc：男巫战怪兽（如兽人）
"""

# Game：FrogWorld
class Frog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        """用于描述青蛙与障碍物（比如虫子、迷宫或其他青蛙）之间的交互"""
        print('{} the Frog encounters {}!'.format(self, obstacle, obstacle.action()))
    
class Bug:
    """例子中的障碍，虫子。当青蛙遇到一只虫子，只支持一种动作，那就是吃掉它！"""
    def __str__(self):
        return 'a bug'
    
    def action(self):
        return 'eats it'

class FrogWorld:
    """类FrogWorld是一个抽象工厂，负责创建游戏的主人公和障碍物"""
    def __init__(self, name):
        print(self)
        self.player_name = name
    
    def __str__(self):
        return '\n\n\t----- Frog World -----'
    
    def make_character(self):
        return Frog(self.player_name)
    
    def make_obstacle(self):
        return Bug()

# Game：WizardWorld
class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(self, obstacle, obstacle.action()))

class Ork:
    def __str__(self):
        return 'an evil ork'
    
    def action(self):
        return 'kills it'
    
class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t----- Wizard World -----'
   
    def make_character(self):
        return Wizard(self.player_name)
    
    def make_obstacle(self):
        return Ork()

class GameEnvironment:
    """类GameEnvironment是游戏的主入口。
       接受factory作为输入，用其创建游戏的世界。
       方法play()则会启动hero和obstacle之间的交互。
    """
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name):
    """提示用户提供一个有效的年龄"""
    try:
        age = input('Welcome {}. How old are you? '.format(name))
        age = int(age)
    except ValueError as err:
        print('Age {} is invalid, please try again...'.format(age))
        return (False, age)
    return (True, age)

def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()

if __name__ == '__main__':
    main()
