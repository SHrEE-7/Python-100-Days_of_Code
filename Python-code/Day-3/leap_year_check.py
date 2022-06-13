year = int(input("which year do you want to check?\n"))
if year % 4 ==0:
  if year % 100 ==0:
    if year % 400 ==0:
      print("Leap year\n") 
    else:
      print("not a leap year\n")
  else:
    print("Leap year\n")
else:
  print("Not a leap year\n")
