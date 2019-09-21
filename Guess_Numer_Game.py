import random

print('Welcome to Guess Number Game ')

print('I am thinking of a number between 1 and 20. ')

randomNumber = random.randint(1,20)

for guessCount in range (1,7):

    guessNumber = int(input('Take a Guess. '))

    if guessNumber < randomNumber :
        print('Your guess is too low ')

        continue
    elif guessNumber > randomNumber :
        print('Your guess is too high ')

        continue
    
    elif guessNumber == randomNumber :
        print('Good Job! You guessed number in ' + str(guessCount) + ' guesses ! ')
        break


print('End of Guess Number Game. ')
