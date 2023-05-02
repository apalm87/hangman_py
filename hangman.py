import random

#Global variables
words = ['chicken', 'dog', 'cat', 'mouse', 'frog', 'cow', 'horse' 'duckr']
livesRemain = 14
guessletters = ''


#controls the game
def play():
    word = pickWord()
    while True:
        guess = getGuess(word)
        if processGuess(guess, word):
            print('You win! Well Done')
            break
        if livesRemain == 0:
            print('You lose!')
            print('The word was: ' + word)
            break

#choses a random word from words
def pickWord():
    return random.choice(words)

def getGuess(word):
    printWordWithBlanks(word)
    print ('Lives Remaining: ' + str(livesRemain))
    guess = input(' Guess a letter or whole word?')
    return guess

def printWordWithBlanks(word):
    displayWord = ''
    for letter in word:
        if guessletters.find(letter) > -1:
            #letter found
            displayWord = displayWord + letter
        else:
            #letter not found
            displayWord = displayWord + '-'
    print(displayWord)


def processGuess(guess, word):
    if len(guess) > 1:
        return WholeWordGuess(guess, word)
    else:
        return singleLetterGuess(guess, word)

def WholeWordGuess(guess, word):
    global livesRemain
    if guess == word:
        return True
    else:
        livesRemain = livesRemain - 1
        return False
    
def singleLetterGuess (guess, word):
    global guessletters
    global livesRemain
    if word.find(guess) == -1:
        #letter guess was incorrect
        livesRemain = livesRemain - 1
    guessletters = guessletters + guess
    if AllLettersGuessed(word):
        return True
    return False

def AllLettersGuessed(word):
    for letter in word:
        if guessletters.find(letter) ==-1:
            return False
    return True
    
play()
