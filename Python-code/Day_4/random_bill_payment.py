import random 
test_seed = int(input("create seed number:\n"))
random.seed(test_seed)
nameasCSV = input("Give me everybody's name separated by comma\n")
name = nameasCSV.split(",")
print(name)
num_items = len(name)
random_Choice = random.randint(0, num_items-1)
person_will_pay = name[random_Choice]
print("Ohhh ...!" +person_will_pay + " gonna pay the bill\n")