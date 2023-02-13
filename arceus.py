import random
thunderboltAcc = 50


class Pokemon:
    def __init__(self, hp, attack, defense, name, element):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.name = name
        self.element = element

    def do_an_attack(self, opponent, name_of_attack):
        randomchance = random.randint(1, 100)
        if randomchance < thunderboltAcc:
            name_of_attack(opponent)
        else:
            print("Git gud you missed")


class ElectricType(Pokemon):
    def __init__(self, hp, attack, defense, name):
        super().__init__(hp, attack, defense, name, 'electric')


    def thunderbolt(self, opponent):
        if self.element == opponent.element:
            result = opponent.hp - (self.attack - opponent.defense) / 2
        # elif opponent.element == 'ground':
        #     return "Your attack had no effect"
        else:
            result = opponent.hp + opponent.defense - self.attack
        opponent.hp = result
        print(opponent.name + " health is " + str(result))
        return result



class GroundType(Pokemon):
    def __init__(self, hp, attack, defense, name):
        super().__init__(hp, attack, defense, name, 'ground')



Gred = ElectricType(35, 55, 40, 'Gred')
Fred = ElectricType(40, 50, 40, 'Fred')

print(Fred.do_an_attack(Gred, Fred.thunderbolt))
