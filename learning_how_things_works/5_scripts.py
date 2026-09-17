#Calculate tip - 1
bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

tip = bill * (tip_percentage / 100)
total = bill + tip

print(f"Tip amount: ${tip:.2f}")
print(f"Total amount to be paid: ${total:.2f}")

#Generator of password - 2
import random
import re
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
# password = generate_password(12)
# print(f"Generated password: {password}")

#Work with time - 3 
import time

seconds = int(input("Enter the number of seconds to wait: "))
print(f"Waiting for {seconds} seconds...")
time.sleep(seconds)
print("Done waiting!")

#Work with system (finding files - 4)

import os

for file in os.listdir('.'):
    if file.endswith('.txt'):
        print(f"Found text file: {file}")


#Game "Guess the number" - 5
import random

number_to_guess = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break