import random

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
        availiable = self.get_available_moves()
        
        if self.fainted:
            print("Error: " + self.name + " is fainted!")
        elif move not in avaiable:
            print("Error: " + move.name + " is not avaialble.")
        else:
            r = random.randint(1, 100)

            if r <= move.accuracy:
                damage = move.get_damage(self, target)
                target.apply_damage(damage)
                print(move.name + " hits " + target.name + " for " + str(damage) + "."
            else:
                print(move.name + "missed!")

            move.remaining_power -= 1

    def take_damage(self, amount):
        self.current_health -= amount
        
        if self.current_health <= 0:
            self.faint()

    def faint(self):
        self.current_health = 0
        print(self.name + " fainted!")
                  
    def heal(self, amount):
        pass

    def get_availiable_moves(self):
        result = []
                  
        for m in self.moves:
            if m.remaining_power > 0:
                  result.append(m)
                  
        return result
                  
    def get_move(self):
        avaialble = self.get_availiable_moves()
        return random.choice(avaialble)

    def draw(self):
        pass


class Move:
    STRONG = 2.0
    NORMAL = 1.0
    WEAK = 0.5
        
    effectiveness = {
            ('student' ,'administrator'): STRONG,
            ('student' ,'student'): NORMAL,
            ('student', 'teacher'): WEAK,
            ('teacher', 'student'): STRONG,
            ('teacher' ,'teacher'): NORMAL,
            ('teacher' ,'administrator'): WEAK,
            ('administrator' ,'teacher'): STRONG,
            ('administrator', 'administrator'): NORMAL,
            ('administrator', 'student'): WEAK
          }
                 
    def __init__(self, name, kind, powerpoint, power, accuracy):
        self.name = name
        self.kind = kind
        self.powerpoint = powerpoint
        self.power = power
        self.accuracy = accuracy

        self.remaining_power = remaining_power

    def get_damage(self, attacker, target):

        p = self.power
        a = attacker.attack
        d = target.defense
        e = effectiveness[(self.kind, target.kind)]

        return int(p * a / d * e)

                      
class Player:

    def __init__(self, characters):
        pass

    def fight(self, target):
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
    
    def draw(self):
        pass
                  
                  
class Game:

    def __init__():
        pass

    def loop(self):
        # get input

        # do logic stuff
        if player.intersects(pokemann):
            player.fight(pokemann)

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
