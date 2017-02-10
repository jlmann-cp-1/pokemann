class Pokemann:

    def __init__(name, kind, attack, defense, speed, health, moves):

        self.name = name
        self.kind = kind
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health
        self.moves = moves # this is a list of Move objects

class Move:

    def __init__(name, kind, powerpoint, power, accuracy):
        
        self.name = name
        self.kind = kind
        self.powerpoint = powerpoint
        self.power = power
        self.accuracy = accuracy


bubble = Move("bubble", "water" 30, 40, 100)
ember = Move("ember", "fire", 30, 50, 95)

cooper = Pokemann("cooper", "water" 30, 20, 50, 30, [bubble, ember])


class Player:

    def __init__(player_name, pokedudes):
        self.player_name = player_name
        self.pokedudes = pokedudes

        x = 0
        y = 0

    def draw(self):
        pass

    def move(self):
        pass
