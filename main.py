#Rollercoaster decision tree
# print("Welcome to the rollercoaster!")
# #are you tall enough to ride?
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#   print("You can ride the rollercoaster!")
#   #what price do we charge to ride?
#   age = int(input("What is your age? "))
#   if age < 12:
#     print("Child tickets are $5.")
#     bill = 5
#   elif age <= 18:
#     print("Youth tickets are $7.")
#     bill = 7
#   elif age >= 45 and age <= 55:
#     print("Everything is going to be okay. Have a free ride on us!")
#   else:
#     print("Adult tickets are $12.")
#     bill = 12
#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill += 3
#   print(f"Your final bill is ${bill}.")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# # Exercise 1 - Odd or Even
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
# #Write your code below this line 👇
# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")
# Exercise 2 - BMI 2.0
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
# #Write your code below this line 👇
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")
# # Exercise 3 - Leap Year
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
# #Write your code below this line 👇
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
# # Exercise 4 - Pizza Order Practice
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
# #Write your code below this line 👇
# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25
# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
# if extra_cheese == "Y":
#   bill += 1
# print(f"Your final bill is: ${bill}.")
# # Exercise 5 - Love Calculator
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
# #Write your code below this line 👇
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
# true = t + r + u + e
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
# love = l + o + v + e
# love_score = int(str(true) + str(love))
# if (love_score < 10) or (love_score > 90):
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}.")
# Day 3 Project - Treasure Island
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
