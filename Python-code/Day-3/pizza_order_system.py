
print("Welcome to python Pizaa deliveries...!\n")
size = input("what size pizza do you want? S, M or L?\n")
add_pepperoni = input("Do you want pepperoni? Press Y or N\n")
extra_cheese = input("Do you want extra cheese? Press Y or N\n")
bill = 0
if size == "S":
  bill+=15
elif size == "M":
  bill +=20
else:
  bill +=25

if add_pepperoni == "Y":
  if size == "S":
    bill +=2
  else:
    bill +=3
if extra_cheese == "Y":
   bill+=1 
  
print(f"your final bill amount is ₹{bill}")