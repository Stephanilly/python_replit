# Odd or Even
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")


# Treasure Island - choose your own adventure
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#Write your code below this line 👇
choice1 = input('You\'re at a cross road. Do you want to go left or right? \n').lower()
if choice1 == "left":
  choice2 = input('As you wander down the left path for a while, you wonder if there is anything to see. \nEventually, you come to a lake. There\'s an island in the middle of the lake, and you suspect that that might be where the treasure is. \nDo you "wait" for a boat? Or do you "swim" across? \n').lower()
  if choice2 == "wait":
    choice3 = input("After waiting for what seemed like an eternity, a mysterious boat arrives and you embark. \nYou amazingly arrive at the island unharmed. \nOn the island you approach a house and see 3 doors. One is red, one is yellow, and one is blue. \nWhich color door do you choose? \n").lower()
    if choice3 == "red":
      print("As the door closes behind you, a trap activates and the room is engulfed in flames. You die in agony. Game Over.")
    elif choice3 == "yellow":
      print("As the door closes behind you, you see a chest in the opposite corner. When you open it, you find riches beyond your wildest dreams! You Win!")
    elif choice3 == "blue":
      print("As the door closes behind you, you see a chest in the opposite corner. When you go to open it, you find too late that it's a mimic. You become its latest meal. Game Over.")
    else:
      print("You chose a door that doesn't exist and fall forever through the abyss. Game Over.")
  elif choice2 == "swim":
    print('''Since you\'re a strong swimmer, you decide to try the water; after all, the island doesn\'t look *that* far. \nUnfortunately, the water is infested with mutant trout, and you get attacked repeatedly and drown. Game Over.
            .'|_.-
         .'  '  /_
      .-"    -.   '>
   .- -. -.    '. /    /|_
  .-.--.-.       ' >  /  /
 (o( o( o )       \_."  <
  '-'-''-'            ) <
(       _.-'-.   ._\.  _\\
 \'----"/--.__.-) _-  \|
       "V""    "V"''')
  else:
    print("You've wandered away from the adventure, and the treasure is nowhere to be found. Game Over.")
elif choice1 == "right":
  print("You turn right and walk for a while until you step on soft ground. \nAs it gives way beneath your foot, you see you\'re falling into a pit with spikes at the bottom. \nYour death is gruesome and painful. Game Over.")
else:
  print("You've wandered away from the adventure, and the treasure is nowhere to be found. Game Over.")
