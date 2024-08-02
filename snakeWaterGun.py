# A GAME PLAY CODE IN PYTHON 

# importing random function
import random
# function defined to set rules of the game
def game(p1,p2):
    if p1 == p2:
        return None
    elif p1 == 's':
        if p2 == 'w':
            return False
        elif p2 == 'g':
            return False
    elif p1 == 'w':
        if p2 == 'g':
            return False
        elif p2 == 's':
            return True
    elif p1 == 'g':
        if p2 == 's':
            return False
        elif p2 == 'w':
            return True
        
    # choices made by players are to be as
print("choices are Snake (s), water (w), gun (g) ")
    # player1 choice as a random value 
print("player1 computer's choice? ")


# random function to let system choose any random move
rand = random.randint(1,3)
    # aloting random integer values a string variable 
if rand == 1:
    p1 = 's'
elif rand == 2:
    p1 = 'w'
elif rand == 3:
    p1 = 'g'
    # player 2 choice - user input
p2 = input("player2's choice? ")
# function call
play = game(p1,p2)

# printing choices using f string
print(f"player 1 chose {p1}")
print(f"player 2 chose {p2}")

# case conditions to make a decision
if play == None:
    print("tchh! it's a tie...")
elif play:
    print("Yahuuu! you win ")
else:
    print("Ahhh! you lose")
