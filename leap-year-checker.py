# Check if any given year is a leap year
year = int(input("Which year do you want to check? "))
# if year is cleanly divisible by 4 it's a leap year
if year % 4 == 0:
# unless it's also cleanly divisible by 100
  if year % 100 == 0:
# except when it's also cleanly divisible by 400
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
