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

        self.current_health = health

    def execute_move(self, move, target):
        damage = move.get_damage(self, target)
        target.apply_damage(damage)

        move.remaining_power -= 1

    def apply_damage(self, amount):
        pass

    def heal(self, amount):
        pass

    def get_move(self):
        return random.choice(moves) # be sure to check powerpoint

    def draw(self):
        pass


class Move:

    def __init__(self, name, kind, powerpoint, power, accuracy):

        self.name = name
        self.kind = kind
        self.powerpoint = powerpoint
        self.power = power
        self.accuracy = accuracy

        self.remaining_power = remaining_power

    def get_effectiveness(self, target):
        
        multipliers = {
                        ('fire' ,'grass'): 2.0,
                        ('fire' ,'fire'): 1.0,
                        ('fire', 'water'): 0.5,
                        ('water', 'fire'): 2.0,
                        ('water' ,'water'): 1.0,
                        ('water' ,'grass'): 0.5,
                        ('grass' ,'water'): 2.0,
                        ('grass', 'grass'): 1.0
                        ('grass', 'fire'): 0.5
                      }

        return multipliers[(self.kind, target.kind)]

    def get_damage(self, attacker, target):

        p = self.power
        a = attacker.attack
        d = target.defense
        e = self.get_effectivness(target)

        return int(p * a / d * e)

class Player:

    def __init__(self, characters):
        pass

    def battle(self, target):
        '''
        1. Select a move (from available of character[0])
        2. target_move = target.get_move()
        3. check speed for 1st attack
        4. one attacks two
            self.execute_move(move, target)
        5. if two alive, two attacks 1
            target.execute_move(move, self)
        '''
        pass

    def catch(self, target):
        pass

class Game:

    def __init__():
        pass

    def loop(self):
        # get input

        # do logic stuff
        if player.intersects(pokemann):
            player.battle(pokemann)

        if player.intersects(potion):
            # pick character to heal
            pass

        # draw stuff


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
