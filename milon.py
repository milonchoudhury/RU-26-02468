import random


def explore_river(score, health):
  score += 50
  print(f"You found a treasure! Score: {score} | Health: {health}")
  return score, health


def explore_cave(score, health, fixed_damage=None):
  damage = (
      fixed_damage if fixed_damage is not None else random.randint(10, 40)
  )
  health = max(0, health - damage)

  print(f"Cave: Monster attacks! Damage: {damage}. Health: {health}")

  if health > 0:
    score += 20
    print(f"You found a key! Score: {score}")

  return score, health


def explore_forest(starting_health=100, fixed_damage=None):
  health = starting_health
  score = 0

  print("Welcome to the Text-Based Adventure Game!")
  print(f"You are in the Forest. Starting Health: {health} | Score: {score}\n")

  while health > 0:
    print("Choices: 1 (Cave), 2 (River), 3 (Quit)")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
      score, health = explore_cave(score, health, fixed_damage)
      if health == 0:
        print(f"Game Over! Final score: {score}")
        break

    elif choice == "2":
      score, health = explore_river(score, health)

    elif choice == "3":
      print(f"You left the adventure. Final score: {score} | Health: {health}")
      break

    else:
      print("Invalid choice. Enter 1, 2 or 3.")

    print()


if __name__ == "__main__":
  explore_forest(starting_health=100, fixed_damage=None)