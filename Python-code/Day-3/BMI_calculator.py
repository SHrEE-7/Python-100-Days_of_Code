
height = float(input("Enter you height in m:\n"))
weight = int(input("Enter your weight in kg:\n"))
BMI =  round(weight / height **2,2)
print(f"Your BMI is {BMI}")
print("conclusion from you BMI is:\n")
if BMI < 18.5:
  print("You are underwighted\n")
elif BMI <25:
  print("you have normal weight\n")
elif BMI <30:
  print("You are overwight\n")
elif BMI <35:
  print("You are clinically obese\n")