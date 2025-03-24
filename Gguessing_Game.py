# the library that generates random numbers
import random
# the variable that stores the random number
random_number = random.randint(1, 100)

# the game
while(True):
    # the user's guess input
    guess = int(input("Guess the number: "))
    # the logic
    # if the user's guess is higher than the random number
    if guess > random_number:
        print("Too high")
    # if the user's guess is lower than the random number
    elif guess < random_number:
        print("Too low")
    # if the user's guess is equal to the random number the game ends and the user wins
    else:
        print("Correct")
        break