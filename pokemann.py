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

        self.fainted = False
        self.current_health = health

    def get_available_moves(self):
        result = []
                  
        for m in self.moves:
            if m.remaining_power > 0:
                  result.append(m)
                    
        return result
    
    def execute_move(self, move, target):
        available = self.get_available_moves()
        
        if self.fainted:
            print("Error: " + self.name + " is fainted!")
        elif move not in available:
            print("Error: " + move.name + " is not available.")
        else:
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
        print(self.name + " fainted!")
                  
    def heal(self, amount):
        """
        Raises current_health by amount but not to more than the base health.
        """
        pass

    def draw(self):
        pass

    def __repr__():
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

     def __repr__():
        pass

                     
class Player:

    def __init__(self, name, characters):
        self.name = name
        self.characters = characters

    def get_available_characters(self):
        """
        Returns a list of all unfainted characters belonging to a player.
        """
        pass
    
    def select_character(self):
        """
        Human players use this.

        1) Generate a menu which shows a numbered list of all characters along with status (health).
        2) Have the player select a character.
        3) Move the selected character to position [0] in the characters list.
        """
        pass
    
    def select_move(self, character):
        """
        Human players use this.

        1) Generate a menu which shows a numbered list all available moves for a character.
        2) Have the player select a move.
        3) Return the selected move.
        """

        available = character.get_available_moves()
        
        print("Select a move:")
        
        for i, move in enumerate(available):
            print(str(i) + ") " + move.name)

        n = input("Your choice: ")
        n = int(n)
        
        return available[n]
        

    def get_random_character(self):
        """
        Computer controlled Pokemann use this.

        Return a random character from all unfainted.
        """
        pass
    
    def get_random_move(self):
        """
        Computer controlled Pokemann use this.

        Return a random move from all available.
        (A better Pokemann AI could be smarter about the move they choose.)
        """
        
        available = self.get_available_moves()
        return random.choice(available)

    def get_target(self):
        """
        Returns the first unfainted character in the characters list.
        """
        pass
    
    def fight(self, character, target):
        """
        1. Select player_move (from available of character)
        2. Select target_move (use get_random_move)
        3. Compare speeds of character and target
            If character.speed > target.speed, set first = character, second = target
            Otherwise, set first = target, second = character
            If speeds are equal, assign first and second randomly.
        4. Call
            first.execute_move(move, second)
        5. If second is still unfainted, call
            second.execute_move(move, first)
        """
        pass

    def catch(self, target):
        pass

    def battle(self, opponent):
        """
        This function controls all battle logic including decisions to reorder characters,
        fight, use potions, run away, and whatever else happens in Pokebattles.

        Use a loop so that this continues until all characters for either the player or
        opponent are fainted.
        """
        pass
    
    def draw(self):
        pass
                  
    def __repr__():
        pass

                  
class Game:

    def __init__():
        pass

    def loop(self):
        pass
    
        # get input

        # do logic stuff

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
    coopasaur = Pokemann("Coopasaur", "teacher", 30, 20, 50, 30, [homework, pop_quiz, id_violation], "coopasaur.png")
    cookmander = Pokemann("Cookmander", "teacher", 30, 20, 50, 30, [lecture, id_violation, homework], "cookmander.png")
    vincolairy = Pokemann("Vincolairy", "teacher", 30, 20, 50, 30, [lecture, id_violation, homework], "vincolairy.png")
    mayfieldarow = Pokemann("Mayfieldarow", "administrator", 30, 20, 50, 30, [dress_code, id_violation, lecture], "mayfieldarow.png")
    andrewag = Pokemann("Andrewag", "student", 30, 20, 50, 30, [excessive_talking, disruptive_behavior, homework], "andrewag.png")
    caseypuff = Pokemann("Caseypuff", "student", 30, 20, 50, 30, [excessive_talking, disruptive_behavior, homework], "caseypuff.png")
    colboreon = Pokemann("Colboreon", "student", 30, 20, 50, 30, [excessive_talking, disruptive_behavior, homework], "colboreon.png")
    blakachu = Pokemann("Blakachu", "student", 30, 20, 50, 30, [excessive_talking, disruptive_behavior, homework], "blakachu.png")
    zoeotto = Pokemann("Zoeotto", "student", 30, 20, 50, 30, [excessive_talking, disruptive_behavior, homework], "zoeotto.png")
    morganyta = Pokemann("Morganyta", "student", 30, 20, 50, 30, [excessive_talking, disruptive_behavior, homework], "morganyta.png")
    
    # Create Players
    pat = Player("Pat Riotum", [coopasaur, andrewag, caseypuff, blakachu])
    team = Player("Team Rocket", [colboreon, zoeotto, morganyta, cookmander])
    
