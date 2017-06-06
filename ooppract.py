import time


class Person:
    name = "Player"
    defeated_enemy = 0

    def __init__(self, hp, attack):
        self.attack = attack
        self.hp = hp

    def deal_damage(self):
        print(Person.name + " deals %d to the monster" % (self.attack))
        return self.attack

    def loose_hp(self, number):
        self.hp -= number
        print(Person.name + " looses " + str(number) + "health. Now at %s health" % (self.hp))

    def defeat(self):
        print("Sorry, game over")

    @classmethod
    def defeat_enemy(cls):
        cls.defeated_enemy += 1


class Monster:
    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack

    def loose_hp(self, number):
        print("Monster currently have " + str(self.hp) + " health")
        self.hp -= number
        print("Monster looses " + str(number) + " health. Currently at : " + str(self.hp) + " health")

    def deal_damage(self):
        print("Monster deals " + str(self.attack) + " damage to the player")
        return self.attack

    def defeat(self):
        if self.hp <= 0:
            return True
        else:
            return False


class bossMonster(Monster):
    def __init__(self, hp, attack):
        super().__init__(hp, attack)

    def use_superpower(self):
        print("Monster uses superpower  and deals 5 extra damage to the player")
        return 5


class Main:
    def __init__(self):
        self.game = True
        self.player = Person(30, 5)

    def main(self):
        monster1 = Monster(10, 2)
        monster2 = Monster(10, 3)
        boss = bossMonster(20, 5)
        monster_list = [monster1, monster2, boss]
        for i in monster_list:
            while self.game:
                i.loose_hp(self.player.deal_damage())
                time.sleep(3)
                self.player.loose_hp(i.deal_damage())
                time.sleep(3)
                if i.defeat():
                    break

if __name__ == "__main__":
    main = Main()
    main.main()
