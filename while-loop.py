import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)

isGuessRight =  False

while isGuessRight!= True:
    guess= input("Guess a number between 1 and 10: ")
    
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else: 
        if int(guess) < number:
            print(f"You guessed {guess}. Sorry, that isn’t it. Guess a number greater than {guess} Try again")
        else:
            print(f"You guessed {guess}. Sorry, that isn’t it. Guess a number less than {guess}")