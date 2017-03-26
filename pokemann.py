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
        """
        Raises current_health by amount but not to more than the base health.
        """
        self.current_health += amount

        if current_health > health:
            current_health = health

        fainted = False
        
        print(self.name + " was healed. Health is now " + str(self.current_health) + "/" + str(health) + ".")

    def restore(self):
        """
        Restores all health, unfaints, and resets powerpoint for all moves.
        """
        self.current_health = self.health
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
        self.remaining_power = self.powerpoint
        

class Character:
    
    def __init__(self, name, party, image):
        self.name = name
        self.party = party
        self.image = image

    def get_available_pokemann(self):
        """
        Returns a list of all unfainted Pokemann belonging to a character.
        """
        result = []
                  
        for p in self.party:
            if p.fainted == False:
                  result.append(p)
                    
        return result
    
    def get_active_pokemann(self):
        """
        Returns the first unfainted character in the pokemann list. If all pokemann
        are fainted, return None.
        """
        available = self.get_available_pokemann()

        if len(available) > 0:
            return available[0]
        else:
            return None
    
    def set_active_pokemann(self, poke):
        """
        Moves pokemann to first position [0] in the party.
        """
        self.party.remove(poke)
        self.party.insert(0, poke)
    
    def restore(self):
        for poke in party:
            poke.restore()
    
    def draw(self):
        pass

    
class Player(Character):

    def __init__(self, name, party, image):
        Character.__init__(self, name, party, image)
        
        self.computer = []
        self.pokeballs = 0

    def select_move(self):
        """
        1) Generate a numbered list all available moves for the active pokemann.
        2) Have the player select a move.
        3) Return the selected move.
        """
        active = self.get_active_pokemann()
        available = active.get_available_moves()
        
        print("Select a move:")
        
        for i, move in enumerate(available):
            print(str(i) + ") " + move.name)

        n = input("Your choice: ")
        n = int(n)
        
        return available[n]

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
            print("You caught a " + target.name + "!")

            if len(self.party) < 6:
                self.party.append(target)
            else:
                target.restore()
                self.computer.append(target)

            return True
        else:
            print("The " + target.name + " got away!")

            return False
    
    def run(self, target):
        """
        Can only be applied in the presence of a wild pokemann. Success is determined by
        comparing speeds of the player's active pokemann and the wild pokemann. Incoroporate
        randomness so that speed is not the only factor determining success.

        Return True if the escape is successful and False otherwise.
        """
        runner = self.get_active_pokemann()

        r = random.randint(0, 100)

        r += runner.speed
        r -= target.speed

        if r < 60:
            print("You got away!")
            return True
        else:
            print("Escape unsuccessful.")
            return False
    
    def switch_out(self):
        """
        1) Generate a menu which shows a numbered list of all available pokemann along with status (health).
        2) Have the player select a character.
        3) Set the selected character as the active pokemann.
        """
        available = self.get_available_pokemann()
        
        print("Select active Pokemann...")
                        
        for i, p in enumerate(available):
            print(str(i) + ") " + p.name)

        n = input("Your choice: ")
        n = int(n)

        self.set_active_pokemann(available[n])
    
    
class NPC(Character):

    def __init__(self, name, pokemann, image):
        Character.__init__(self, name, pokemann, image)

    
class Game:

    def __init__(self, player):
        self.player = player

    def encounter(self, target):
        """
        This function controls all logic when encountering a wild pokemann. For each turn,
        options are to catch, run, reorder, or select a move. The encounter continues until the
        wild pokemann is caught or fainted, the player successfully runs, or has all pokemann
        in it's party fainted.
        """
        print("You've found a " + target.name + "!")
        
        done = False

        while not done:
            active = self.player.get_active_pokemann()

            if active != None:
                print("Your " + active.name + " is ready.")
                choice = input("Would you like to (f)ight, (c)atch, (r)un, or (s)witch out? ")

                if choice == 'f':
                    active_move = self.player.select_move()
                    target_move = target.get_random_move()

                    if active.speed >= target.speed:
                        active.execute_move(active_move, target)

                        if not target.fainted:
                            target.execute_move(target_move, active)
                    else:
                        target.execute_move(target_move, active)

                        if not active.fainted:
                            active.execute_move(active_move, target)

                    if target.fainted:
                        done = True
                
                elif choice == 'c':
                    done = self.player.catch(target)

                    if not done:
                        target_move = target.get_random_move()
                        target.execute_move(target_move, active)
                
                elif choice == 'r':
                    done = self.player.run(target)
                
                    if not done:
                        target_move = target.get_random_move()
                        target.execute_move(target_move, active)
                
                elif choice == 's':
                    available = self.player.get_available_pokemann()

                    if len(available) > 1:
                        self.player.switch_out()
                        
                        active = self.player.get_active_pokemann()
        
                        target_move = target.get_random_move()
                        target.execute_move(target_move, active)             
                        
                    else:
                        print("You have no unfainted Pokemann to switch.")

                else:
                    print("Invalid selection. Please try again.")
                    
            else:
                print("Oh, no! All of the Pokemann in your party are fainted.")
                done = True

            print()
            
    def battle(self, npc):
        """
        This function controls all battle logic. For each turn, the player can fight
        or reorder. The battle continues until the entire party is defeated for either
        the player or the npc.
        """
        done = False

        while not done:

            active = self.player.get_active_pokemann()
            target = npc.get_active_pokemann()
            
            if active == None:
                print("You have been defeated.")
                done = True
            elif target == None:
                print("Congratulations! You have defeated " + npc.name + ".")
                done = True
            else:
                print("Your " + active.name + " is ready.")
                choice = input("Would you like to (f)ight or (s)witch out? ")

                if choice == 'f':
                    active_move = self.player.select_move()
                    target_move = target.get_random_move()

                    if active.speed >= target.speed:
                        active.execute_move(active_move, target)

                        if not target.fainted:
                            target.execute_move(target_move, active)
                    else:
                        target.execute_move(target_move, active)

                        if not active.fainted:
                            active.execute_move(active_move, target)

                elif choice == 's':
                    available = self.player.get_available_pokemann()

                    if len(available) > 1:
                        self.player.switch_out()
                        
                        active = self.player.get_active_pokemann()
        
                        target_move = target.get_random_move()
                        target.execute_move(target_move, active)             
                        
                    else:
                        print("You have no unfainted Pokemann to switch.")

            print()
        
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

    # Create NPCs
    rocket = NPC("Team Rocket", [colboreon, zoeotto, morganyta, cookmander], "rocket.png")
    jessie = NPC("Jessie", [vincolairy, mayfieldarow, katlevee, marcelax], "jessie.png")

    # Create a game
    g = Game(pat)
