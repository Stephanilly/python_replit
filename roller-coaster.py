# Rollercoaster decision tree
print("Welcome to the rollercoaster!")
#are you tall enough to ride?
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  #what price do we charge to ride?
  age = int(input("What is your age? "))
  if age < 12:
    print("Child tickets are $5.")
    bill = 5
  elif age <= 18:
    print("Youth tickets are $7.")
    bill = 7
  elif age >= 45 and age <= 55:
    print("Everything is going to be okay. Have a free ride on us!")
  else:
    print("Adult tickets are $12.")
    bill = 12
  wants_photo = input("Do you want a photo taken? Y or N. ").upper()
  if wants_photo == "Y":
    bill += 3
  print(f"Your final bill is ${bill}.")
else:
  print("Sorry, you have to grow taller before you can ride.")