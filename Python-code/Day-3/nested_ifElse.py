print("welcome to the rollercoaster\n")
height = int(input("Plase tell me your height in cm\n"))
if height > 120:
  print("you can ride the rollercoaster\n")
  age = int(input("what is your age?\n"))
  if age <=18:
    print("You have to pay ₹50")
  if age >= 60:
    print("You cannot ride the rollercoaster\n")
  else:
    print("You have to pay ₹100")
else:
  print("You are too short to ride..sorry..!\n")