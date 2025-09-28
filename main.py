import random

def guess(x):
    random_number = round(random.uniform(1, x), 5)
    guess = 0.0
    close_low_guess = 1.0
    close_high_guess = 10.0
    while guess != random_number:
        guess = float(input(f'Guess a number between {close_low_guess} and {close_high_guess}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.', end="\n\n")
            if guess < close_low_guess:
                pass
            else:
                close_low_guess = guess
        elif guess > random_number:
            print('Sorry, guess again. Too high.', end="\n\n")
            if guess > close_high_guess:
                pass
            else:
                close_high_guess = guess
            
    print(f'Yay, congrats. You have guessed the number {random_number}')
    
guess(10)