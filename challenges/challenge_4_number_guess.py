"""
Number guessing game

You have 3 tries to guess a number between 1 and 20.
"""
import random


answer = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")
guess_count = 0

while guess_count < 3:
    guess = int(input("Make a guess: "))

    if guess == answer:
        print(f"You got it the answer is {answer}.")
        guess_count = 10
        break
    elif guess > answer:
        print(f"The answer is smaller.")        
    else:
        print("The answer is bigger.")
    
    guess_count += 1
        
if guess_count != 10:
    print(f"Sorry you ran out of guesses. The answer was {answer}")