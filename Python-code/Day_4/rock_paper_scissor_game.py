import random
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = [Rock, Paper, Scissor]
user_choice = int(input(" What do you want to choose?Type 0 for Rock,1 for paper and 2 for Scissor\n"))
print("Your choice\n")
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computers choice\n")
print(game_images[computer_choice])

if user_choice >=3 and user_choice < 0:
  print("You entered invalid input..You lose!\n")
elif user_choice == 0 and computer_choice == 2:
  print("Congratulations...You win!")
elif user_choice == 2 and  computer_choice == 0:
  print("You lose!")
elif user_choice < computer_choice:
  print("You lose!")
elif user_choice > computer_choice:
  print("You win!")
else:
  print("Ohhhh It's Draw..!")


