import random

secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 - 50.')


#Ask the player to guess 8 times.

for guessesTaken in range(1,8):
    print('Take a guess.')
    guess=int(input())

#Guess logic of high and low

    if guess <secretNumber:
        print('No.The guess is too low')
    elif guess>secretNumber:
        print('No. The guess is too high.')
    else:

        break

#If the condition is correct guess

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) +' guesses!')
else:
    print('Nope. The number I was thinking of was '+str(secretNumber))