import random
HANGMAN = ['''
    +---+
    |   |
        |
        |
        |
        |
============''','''
    +---+
    |   |
    0   |
        |
        |
        |
============''','''
    +---+
    |   |
    0   |
    |   |
        |
        |
============''','''
    +---+
    |   |
    0   |
   /|   |
        |
        |
============''','''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
============''','''
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
============''','''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
============
HANG!!!!!!
''']

words = 'time  brave owl dragon code python chamber dungeon maze david play emerald stone rule world sun train ozzy gordon'.split()

def searchWordRand(listWords):
    randomWord = random.randint(0, len(listWords)-1)
    return listWords[randomWord]
def displayBoard(HANGMAN, wrongLetter, rightLetter, secretWord):
    print('HANGMAN'[len(wrongLetter)])
    print('')
    fin = " "
    print('wrong letter :', fin)
    for letter in wrongLetter:
        print(letter, fin)
    print("")
    space ="_" * len(secretWord)
    for i in range(len(secretWord)): 
        space = space[:i]
    for letter in space:
        print(letter, fin)
    print("")
def chooseLetter(someLetter):
    while True:
        print('Guess a letter:')
        letter = input()
        letter = letter.lower() #we change to lowecase the letter that the user choose
        if len(letter) != 1:
            print('Enter a letter at time:')
        elif letter in someLetter:
            print ('the lette is already tryed, please try whit another letter: ')
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print('please enter a letter.')
        else:
            return letter
def start():
    print('do you want to play again (Yes/No)')
    return input().lower().startswith('s')
print('H A N G M A N')
wrongLetter = ""
rightLetter = ""
secretWord =searchWordRand(words)
endGame = False
while True:
    displayBoard(HANGMAN, wrongLetter, rightLetter, secretWord)
    letter = chooseLetter(wrongLetter + rightLetter)
    if letter in secretWord:
        rightLetter = rightLetter + letter
        lettersFinded = True
        for i in range(len(secretWord)):
            if secretWord[i] not in rightLetter:
                lettersFinded = False
                break
            if lettersFinded:
                print('Well done!!, the secret word is = '+secretWord+'"You Win!!!"')
                endGame = True
            else:
                wrongLetter= wrongLetter + letter
                if len(wrongLetter) == len(HANGMAN)-1:
                    displayBoard(HANGMAN, wrongLetter, rightLetter, secretWord)
                    print('you lose the game after : \n' + str(len(wrongLetter)) + ' wrong letters and ' + str(len(rightLetter)) + ' rigth letters, the word was : ' + secretWord + '"')
                    endGame = True
                if endGame:
                    if start():
                        wrongLetter = ""
                        rightLetter = ""
                        endGame = False
                        secretWord = searchWordRand(words)
                    else:
                        break
