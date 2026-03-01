import random
import matplotlib.pyplot as plt
from collections import Counter

def roll_dice(num_dice=1):
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return rolls, sum(rolls)

def simulate_rolls(num_dice, num_simulations):
    results = []
    for _ in range(num_simulations):
        _, total = roll_dice(num_dice)
        results.append(total)
    return results

def plot_distribution(results):
    counts = Counter(results)
    totals = sorted(counts.keys())
    frequencies = [counts[t] for t in totals]

    plt.bar(totals, frequencies)
    plt.xlabel("Dice Total")
    plt.ylabel("Frequency")
    plt.title("Dice Roll Distribution")
    plt.show()

def main():
    history = []

    while True:
        print("\n🎲 Dice Rolling Simulator")
        print("1. Roll Dice")
        print("2. View Roll History")
        print("3. Simulate Multiple Rolls (Probability)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num_dice = int(input("How many dice to roll? "))
            rolls, total = roll_dice(num_dice)
            history.append((rolls, total))
            print(f"Rolled: {rolls} | Total: {total}")

        elif choice == "2":
            if not history:
                print("No rolls yet.")
            else:
                for i, (rolls, total) in enumerate(history, 1):
                    print(f"{i}. Rolls: {rolls} | Total: {total}")

        elif choice == "3":
            num_dice = int(input("Number of dice: "))
            num_simulations = int(input("Number of simulations: "))
            results = simulate_rolls(num_dice, num_simulations)
            plot_distribution(results)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()