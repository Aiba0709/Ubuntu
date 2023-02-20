import random

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name (self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health (self):
        return self.__health 

    @health.setter
    def health (self, value):
        if value < 0:
            self.__health = 0
        self.__health = value

    @property
    def damage (self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage =value  

    def __str__(self):
        return f"{self.__name} health: {self.__health} damage: {self.__damage}"                          

class Boss (GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return  self.__defence  

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.super_ability

    def hit(self, heroes):
         for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage


    def __str__(self):
        return "Boss" + super().__str__() + f"{self.__defence}" 

class Heroes(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super(Heroes, self).__init__(name, health, damage) 
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability   

    def hit(self, boss):
        if boss.health > 0 and self.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass

class Warrior(Heroes):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, "CRITICAL_DAMAGE")

    def apply_super_power(self, boss, heroes):
        coef = random.randint(1,5)
        boss.health -= self.damage * coef
        print(f"CRITICAL_DAMAGE {self.damage * coef}")        

class Magic(Heroes):
    pass

class Medic(Heroes):
    pass

round_counter = 0

def print_statistic(boss, heroes):
    print(f"______________ROUND {round_counter} _____________")
    print(boss)
    for hero in heroes:
        print(hero)



def play_round(bosss, heroes):
    global round_counter
    round_counter -= 1
    boss.choose_defence(heroes)
    boss.hit(heroes)

    for hero in heroes:
        hero.hit(boss)
        hero.apply_super_power(boss, heroes)


    print_statistic(boss, heroes)    


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!")
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False 
            break
    if all_heroes_dead:
        print("Boss won!")

    return all_heroes_dead           


def start_game():
    boss = Boss("Сыймык", 1000, 50)

    warrior = Warrior("Алихан", 270, 18)

    heroes = [warrior,]

    print_statistic(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)

# start_game()        



boss = Boss()

h1 = Heroes()
h2 = Heroes()

heroes_liist = [h1, h2]

start_game()