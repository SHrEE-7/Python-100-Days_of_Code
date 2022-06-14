import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '9', '8', '7', '6', '5', '4', '3', '2', '1']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']
print("Welcomer to the Password Generator\n")
num_letters = int(
    input("Enter how many letters would you like in your password\n"))
num_numbers = int(
    input("Enter how many numbers you would like in your password\n"))
num_symbols = int(
    input("Enter how many symbols you would like in your password\n"))

#EASY PASSOWORD
password =""
for char in range(1, num_letters+1):
  password += random.choice(letters)
for num in range(1,num_numbers+1):
  password += random.choice(numbers)
for sym in range(1,num_symbols+1):
  password += random.choice(symbols)
print(password)

#HARD LEVEL PASSWORD

password_list = []
for char in range(1, num_letters+1):
  password_list.append(random.choice(letters))
for num in range(1,num_numbers+1):
  password_list += random.choice(numbers)
for sym in range(1,num_symbols+1):
  password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password_list1 =""
for char in password_list:
  password_list1 += char
print(f"Your password is: {password_list1}")
   

