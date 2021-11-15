import random

NUMDIGITS = 3

MAXGUESS = 10

def main():
    print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))

    print('Here are some clues:')

    print('When I say:    That means:')

    print('  Pico         One digit is correct but in the wrong position.')

    print('  Fermi        One digit is correct and in the right position.')

    print('  None       No digit is correct.')#.format(NUMDIGITS))


    while True:

        secretNum = getSecretNum(NUMDIGITS)

        print('I have thought up a number. You have {} guesses to get it.'.format(MAXGUESS))

        numGuesses_number = 0


        while numGuesses_number <= MAXGUESS:

            guess = ""

            while len(guess) != NUMDIGITS or not  guess.isdecimal(guess):

                
                print ("guess{}:".format(numGuesses_number))

                guess=input("Again play")
            
                clues=getClues(guess, secretNum)

                numGuesses_number += 1

                if guess == secretNum:

                    break

                if numGuesses_number < MAXGUESS:

                    print ('You ran out of guesses. The answer was {}'.format(secretNum))
            
            print("Do you want to play again? (yes or no)")
            
            if not input().lower().startswith('y'):
            
                break
        
        print("thank you for playing")

def getSecretNum(numDigits):
    
    numbers = list(range(10))

    random.shuffle(numbers)

    secretNum = ''

    for i in range(numDigits):

        secretNum+=str(numbers[i])

    return secretNum

def getClues(guess, secretNum):
    
    if guess == secretNum:

        return 'You got it!'

    clue = []

    for i in range(len(guess)):

        if guess[i] == secretNum[i]:

            clue.append('Fermi')

        elif guess[i] in secretNum:

            clue.append('Pico')

        if len(clue) == 0:

            return 'None'
        else:
            clue.sort()

    return ' '.join(clue)

if __name__=='__main__':
   
    main()
