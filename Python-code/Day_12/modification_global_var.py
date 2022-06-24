#Modinfing Global variable
enemies = 1
def increase_enemies():
  print(f"Enemies inside the function:{enemies}")
  return enemies + 1
enemies = increase_enemies()
print(f"Enemies outside the functin: {enemies}")