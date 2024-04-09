import random

def play_turn(snail_names, snails, order):
    for snail_name in order:
        print(f"\nIt's {snail_name}'s turn:")
        input("Press Enter to roll the dice...")

        try:
            rolled_snail = random.choice(snail_names)
            print(f"{snail_name} rolled {rolled_snail}")

            move_distance = random.randint(1, 3)
            snails[snail_name] += move_distance
            print(f"{snail_name} moves to space {snails[snail_name]}!")

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

print("Welcome to Braulio's Pace Race!")
print("Roll the dice and move your snail to reach the finish line first.")
print("Be careful not to roll someone else's color!")

snail_names = ['Michael', 'Jailen', 'Nicolas', 'Francis']
snails = {name: 0 for name in snail_names}

order_of_snails = ['Michael', 'Jailen', 'Francis', 'Nicolas']

try:
    while all(position < 10 for position in snails.values()):
        play_turn(snail_names, snails, order_of_snails)

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    winner_name = next(name for name, position in snails.items() if position >= 10)
    print(f"\n{winner_name} wins the race!")
