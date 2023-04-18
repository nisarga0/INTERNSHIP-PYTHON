import random

def generate_number():
    """Generate a 4-digit number with no repeating digits."""
    while True:
        number = str(random.randint(1000, 9999))
        if len(set(number)) == 4:
            return number

def get_guess():
    """Get a user's guess for a 4-digit number with no repeating digits."""
    while True:
        guess = input("Enter a 4-digit number with no repeating digits: ")
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) < 4:
            print("Invalid input. Please enter a 4-digit number with no repeating digits.")
        else:
            return guess

def evaluate_guess(guess, target):
    """Evaluate a guess and return the number of cows and bulls."""
    cows = 0
    bulls = 0
    for i in range(len(guess)):
        if guess[i] == target[i]:
            cows += 1
        elif guess[i] in target:
            bulls += 1
    return cows, bulls

# Main game loop
if __name__ == '__main__':
    print("Welcome to the Cows and Bulls Game!")
    target = generate_number()
    num_guesses = 0
    while True:
        guess = get_guess()
        num_guesses += 1
        cows, bulls = evaluate_guess(guess, target)
        print(f"{cows} cows, {bulls} bulls")
        if cows == 4:
            print(f"Congratulations! You guessed the number in {num_guesses} tries.")
            break
