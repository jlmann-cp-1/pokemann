class Pokemann:

    def __init__(self, name, kind, attack, defense, speed, health, moves, image):

        self.name = name
        self.kind = kind
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health
        self.moves = moves # this is a list of Move objects
        self.image = image # path to image file

    def attack(self, target, move):
        pass
    
    def draw(self):
        pass


class Move:

    def __init__(self, name, kind, powerpoint, power, accuracy):

        self.name = name
        self.kind = kind
        self.powerpoint = powerpoint
        self.power = power
        self.accuracy = accuracy

class Player:

    def __init__(self, player_name, characters):
        self.player_name = player_name
        self.characters = characters

        self.x = 0
        self.y = 0

    def draw(self):
        pass

    def update(self, v_x, v_y):
        pass

    def capture(self, target):
        pass


class World:

    def __init__(self):
        pass

    def draw(self):
        pass


class Game:

    def __init__(self):
        pass

    def battle(self):
        """
        The logic of a Pokefight

         1) Player selects a move (how is player connected to Pokemann?)
         2) Other selects random move.
         3) Speed is checked. Player with higher speed goes first.
         4) First attack executed. Some formula needs to be devised to determine damage.
         5) Check for death.
         6) Second attack executed (if alive).
         7) Check for death.
         8) Repeat until one Pokemann is dead. (Does the next one in line move up?)

         What happens when all of a player's Pokemann are dead? Is that the end of the game?
        """

    def play(self):
        pass


if __name__ == '__main__':

    # Make some moves
    homework = Move("Homework", "teacher", 30, 40, 100)
    pop_quiz = Move("Pop quiz", "teacher", 30, 40, 100)
    lecture = Move("Lecture", "teacher", 30, 40, 100)
    dress_code = Move("Dress Code", "administrator", 30, 50, 95)
    id_violation = Move("ID Violation", "administrator", 30, 50, 95)
    excessive_talking = Move("Excessive Talking", "student", 30, 40, 100)
    disruptive_behavior = Move("Disruptive Behavior", "student", 30, 40, 100)

    # Create some Pokemann(s)
    coopasaur = Pokemann("coopasaur", "teacher", 30, 20, 50, 30, [homework, pop_quiz, id_violation], "coopasaur.png")
    mayfieldarow = Pokemann("mayfieldarow", "administrator", 30, 20, 50, 30, [dress_code, id_violation, lecture], "mayfieldarow.png")
    andrewag = Pokemann("andrewag", "student", 30, 20, 50, 30, [excessive_talking, disruptive_behavior, homework], "andrewag.png")
