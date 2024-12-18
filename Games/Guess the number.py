import random

print("Do you want to play my super fun game")
rand = random.randint(1, 1000)
win = 0

while win != 1:
    try:
        guess = int(input("Take a guess between 1-1000: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if not (0 < guess <= 1000):
        print("Please enter a number within range")
        continue
    
    if guess > rand:
        print("Try lower!")
    elif guess < rand:
        print("Try higher!")
    else:
        print("That's right! The number was " + str(rand))
        win = 1

print("You win!")
