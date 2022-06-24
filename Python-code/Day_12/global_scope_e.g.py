# Global scope

player_health = 10 
def game():
  def drink_potion():
    portion_strength = 2
    print(portion_strength)
  drink_potion()
game()
print(player_health)