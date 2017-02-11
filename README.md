# Pokemann


### Planning

1) Invent three kinds of Pokemann(s). (We're going to avoid using the word 'type' since it is a Python reserved word.)

    Possible kinds: Teacher, Admin, Student? Moves might make sense in this context.

2) Invent several Pokemann moves. 

   Each move should be classified as one of the same three kinds as the Pokemann you have invented. Each move should works best against a Pokemann of a certain kind in a somewhat similar manner to rock-paper-scissors logic. 
   
   Moves should have the following string attributes:
   
   - name
   - kind 
   
   Moves should also have the following numeric attributes:
   
   - powerpoint (where is energy tracked?)
   - power
   - accuracy
   
   What is the range of values for numeric attributes? 1 to 100?
   
   Move ideas: lecture, homework, busywork, dress-code violation, id violation, detention, tardy pass, test, pop quiz, disruptive behavior, slow walking in hall, cafeteria food, excessive sarcasm, big project assigned, book report, gossip, excessive talking.
   
   It might even be a good idea to create a list of all your moves first and then categorize them into three types instead of starting with step 1.
   
3) Invent many Pokemann characters.

    Characters should have the following string attributes:

    - name
    - kind
    
    Characters should also have the following numeric attributes:
        
    - attack
    - defense
    - speed
    - health
        
    Finally, characters should have a `moves` attribute which is a list of all 4 moves that that character has. Are moves restricted to Pokemann by kind or can any Pokemann kind have any move kind?

4) Invent a formula for calculating damage of an attack. The formula should take into consideration the `kind` of attack as well as the `kind` of the victim. Comparing `kind`s should probably result in some sort of multiplier which can then be put into a formula involving the attacker's `power` and `attack` attributes as well as the victim's `defense` attribute.


5) Describe the logic of a Pokemann battle. You don't need to write code yet, although your logic can be written somewhat code-like. You probably want a loop with some conditional statements, and references to Pokemann attributes. Rather than write a paragraph or list steps, write out your logic using indentation like you would for actual Python code. Words like 'while' and 'if' would also be good to use.  Be sure to take `accuracy` into consideration. 

6) Test your battle logic. This should be done using pencil and paper, although you probably want to use the Python shell to generate random numbers. Use anything you learn while testing to refine Pokemann attributes, Move attributes, and battle logic. You do not want to write any code until you've worked out as many quirks as possible.

7) How might you catch a Pokemann? Devise a formula which takes into account attributes of the attacker and the victim to determine a probability that a catch is successful.

8) Simulate more battles and test your catch logic.

9) Create images for a few of the Pokemann that you have created. (We have a website full of teacher pictures.)

10) Consider game mechanics and graphics. Don't code yet. Just brainstorm. Perhaps write brief descriptions of various gameplay situations. Some sketches of game screens and in-game menus could be useful as would some rough sketches of maps.


### More questions Coop has...

What causes health to go up?


### Code

If you do want to write some code, don't do so in the context of a full game. Just make small testing programs where you can do things such as experiment with formulas and practice creating objects using initializers. Maybe try to code some battle logic with text-based menus. We should be getting a feel for how small components of the game might work before contemplating the overall structure of the game.


### Extra credit:

Make Pokemann Cards or make a website for your game. (docs in GitHub.)
