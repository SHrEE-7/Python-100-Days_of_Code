print("Welcome to LOVE CALULATOR....!")
name1 = input("what is you name?\n")
name2 = input("what is their name?\n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score >90:
  print(f"Your love score is {love_score}, yo go together like cocke and mentos...!\n")
elif love_score>=40 and love_score<=50:
  print(f"Your love score is{love_score} you are alright together\n")
else:
  print(f"your love socre is {love_score}")