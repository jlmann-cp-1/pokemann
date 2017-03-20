import random

class Pokemann:

    def __init__(self, name, kind, attack, defense, speed, health, catch_rate, moves, image):

        self.name = name
        self.kind = kind
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health
        self.catch_rate = catch_rate
        self.moves = moves # this is a list of Move objects
        self.image = image # path to image file

        self.fainted = False
        self.current_health = health

    def get_available_moves(self):
        result = []
                  
        for m in self.moves:
            if m.remaining_power > 0:
                  result.append(m)
                    
        return result

    def get_random_move(self):
        available = self.get_available_moves()
                   
        return random.choice(available)

    def execute_move(self, move, target):
        r = random.randint(1, 100)

        if r <= move.accuracy:
            damage = move.calculate_damage(self, target)
            print(self.name + " hits " + target.name + " with " + move.name  + " for " + str(damage) + ".")
            target.take_damage(damage)
        else:
            print(move.name + "missed!")

        move.remaining_power -= 1

    def take_damage(self, amount):
        self.current_health -= amount
        
        if self.current_health <= 0:
            self.faint()

    def faint(self):
        self.current_health = 0
        self.fainted = True
        
        print(self.name + " fainted!")
                  
    def heal(self, amount):
        self.current_health += health

        if current_health > health:
            current_health = health

        fainted = False
        
        print(self.name + " was healed. Health is now " + str(self.current_health) + "/" + str(health) + ".")

    def restore(self):
        self.current_health = health
        self.fainted = False

        for m in self.moves:
            m.restore()
    
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

        self.remaining_power = powerpoint

    def calculate_damage(self, attacker, target):

        p = self.power
        a = attacker.attack
        d = target.defense
        e = self.effectiveness[(self.kind, target.kind)]

        return int(p * a / d * e)

    def restore(self):
        """
        Resets remaining_power to starting powerpoint.
        """
        self.remaining_power = powerpoint
        

class Character:
    
    def __init__(self, name, party, image):
        self.name = name
        self.party = party
        self.image = image

    def get_available_pokemann(self):
        result = []
                  
        for p in self.party:
            if p.fainted == False:
                  result.append(p)
                    
        return result
    
    def get_active_pokemann(self):
        available = self.get_available_pokemann()

        if len(available) > 0:
            return available[0]
        else:
            return None
    
    def restore(self):
        for poke in party:
            poke.restore()
    
    def draw(self):
        pass

    
class Player(Character):

    def __init__(self, name, pokemann, image):
        Character.__init__(self, name, pokemann, image)
        
        self.computer = []
        self.pokeballs = 0

    def catch(self, target):
        """
        Can only be applied to a wild pokemann. Determine a catch by generating a random
        value and comparing it to the catch_rate. If a catch is successful, append the
        target to the player's pokemann list. However, if the pokemann list already
        contains 6 pokemann, add the caught target to the players computer instead.
        Pokemann sent to the computer will be fully restored, but other caught pokemann
        will remain at the strength they were caught. Decrease the player's pokeball
        count by 1 regardless of success.

        Return True if the catch is successful and False otherwise.
        """
        r = random.randint(1, 100)

        if r <= target.catch_rate:
            pass
        else:
            print("It got away!")
    
    def run(self, target):
        """
        Can only be applied in the presence of a wild pokemann. Success is determined by
        comparing speeds of the player's active pokemann and the wild pokemann. Incoroporate
        randomness so that speed is not the only factor determining success.

        Return True if the escape is successful and False otherwise.
        """
        pass
    
class NPC(Character):

    def __init__(self, name, pokemann, image):
        Character.__init__(self, name, pokemann, image)
    
class Game:

    def __init__(self):
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

    # Create some Pokemann
    coopasaur = Pokemann("Coopasaur", "teacher", 30, 20, 50, 100, 10, [homework, pop_quiz, id_violation], "coopasaur.png")
    cookmander = Pokemann("Cookmander", "teacher", 30, 20, 50, 100, 20, [lecture, id_violation, homework], "cookmander.png")
    vincolairy = Pokemann("Vincolairy", "teacher", 30, 20, 50, 120, 5, [lecture, id_violation, homework], "vincolairy.png")
    mayfieldarow = Pokemann("Mayfieldarow", "administrator", 30, 20, 50, 90, 20, [dress_code, id_violation, lecture], "mayfieldarow.png")
    andrewag = Pokemann("Andrewag", "student", 30, 20, 50, 150, 1, [excessive_talking, disruptive_behavior, homework], "andrewag.png")
    caseypuff = Pokemann("Caseypuff", "student", 30, 20, 50, 170, 70, [excessive_talking, disruptive_behavior, homework], "caseypuff.png")
    colboreon = Pokemann("Colboreon", "student", 30, 20, 50, 80, 30, [excessive_talking, disruptive_behavior, homework], "colboreon.png")
    blakachu = Pokemann("Blakachu", "student", 30, 20, 50, 130, 8,[excessive_talking, disruptive_behavior, homework], "blakachu.png")
    zoeotto = Pokemann("Zoeotto", "student", 30, 20, 50, 100, 15, [excessive_talking, disruptive_behavior, homework], "zoeotto.png")
    morganyta = Pokemann("Morganyta", "student", 30, 20, 50, 160, 32, [excessive_talking, disruptive_behavior, homework], "morganyta.png")
    katlevee = Pokemann("Katlevee", "student", 30, 20, 50, 140, 4, [excessive_talking, disruptive_behavior, homework], "katlevee.png")
    marcelax = Pokemann("Marcelax", "student", 30, 20, 50, 30, 100, [excessive_talking, disruptive_behavior, homework], "marcelax.png")
    
    # Create Player
    pat = Player("Pat Riotum", [coopasaur, andrewag, caseypuff, blakachu], "pat.png")

    # Create Opponents
    rocket = NPC("Team Rocket", [colboreon, zoeotto, morganyta, cookmander], "rocket.png")
    jessie = NPC("Jessie", [vincolairy, mayfieldarow, katlevee, marcelax], "jessie.png")

    # Create a game
    g = Game()
