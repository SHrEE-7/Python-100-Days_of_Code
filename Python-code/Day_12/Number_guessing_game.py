from art import logo
print(logo)
import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#fuction to check user's guess against actual answer
def check_answer(guess,answer,turns):
  """Checks answer against guess. Returns the number of turn left"""
  if guess > answer:
    print("Too high\n")
    return turns -1
  elif guess < answer:
    print("Too low:\n")
    return turns - 1
  else:
    print(f"Your got it..! The answer was {answer}")

#make function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. type 'easy' or 'hard': ")
  if level == "easy": 
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
def game():
    #choosing a random number between 1 and 100
    print("Welcome to the number guessing game..!") 
    print("I'am thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    # print(f"{answer}")

    turns = set_difficulty()

    #let the user guess a number 
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number.")
        guess = int(input("Guess the number:\n"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You have run out of guesses, you lose..")
            return
        elif guess != answer:
            print("Guess Again..")
game()