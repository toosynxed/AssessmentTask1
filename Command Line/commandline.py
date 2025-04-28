import os
import random
os.system('clear') #Clear terminal
alphabet = open(r"alphabet.txt","r") #call file
guessed_letters = [] #Initialises list
letters_remaining = [] #Initialises list
word_choices = ['apple', 'banana', 'orange', 'pear']
chosen_word = random.choice(word_choices) #Picks a random word from the list
word = set(chosen_word) #Finds all distinct characters
print(chosen_word)
print(word)
lives = len(chosen_word) #Sets the life value  ***** LATER CHANGE THIS TO SET VALUE AFTER CREATING IMAGE OF HOUSE *****

for x in alphabet: #Appending letters from alphabet file to the list
    letters_remaining.append(x.replace('\n', ''))

#print(f'Word Status: {' '.join(['_' if letter not in guessed_letters else letter for letter in chosen_word])}')

while lives != 0 and len(word) != 0: #While game is still valid, and not won or lost
    print(f'Letters Remaining: {' '.join(letters_remaining)}') #Letters left to guess
    print(f'Letters Guessed: {' '.join(guessed_letters)}') #Letters already guessed
    print(f'Word Status: {' '.join(['_' if letter not in guessed_letters else letter for letter in chosen_word])}') #Prints out underscored word
    
    letter = input('Pick a letter: ').lower() #Input line
    os.system('clear')
    if letter not in guessed_letters and len(letter) == 1 and letter.isalpha() == True: #Makes sure that it hasn't been guessed already, is only 1 character long, is a valid letter
        letters_remaining.remove(letter) #Removes letter from alphabet
        guessed_letters.append(letter) #Adds letter to the list of already guessed letters

       # print(f'Wordd Status: {' '.join(['_' if letter not in guessed_letters else letter for letter in chosen_word])}')

        if letter in word: #Checks if the letter is in the set
            #print(f'{' '.join(['_' if letter not in guessed_letters else letter for letter in chosen_word])}')

            word.remove(letter) #Removes the correctly guessed letter from the set
            #letters_remaining.remove(letter)
            print('Good Job! You have guessed a correct letter!')
            print(f'You have {lives} lives remaining!')
            #print(f'Letters Remaining: {' '.join(letters_remaining)}') #Letters left to guess
            #print(f'Letters Guessed: {' '.join(guessed_letters)}') #Letters already guessed

        elif letter not in word: #If not in set
            lives = lives - 1 #Lose a life, and image changes ****** IMAGE CHANGES HERE PLEASE!!! ******
            print(f'Uh, Oh!\nIt seems that this letter is not in the word!\nYou have {lives} lives remaining!') #Feedback off incorrect guess

    elif letter.isalpha() == False or len(letter) != 1: #If input isn't a letter or only 1 character long
        print(f'Uh, Oh!\nInvalid Input!\nPick again!')

    elif letter in guessed_letters: #If input has already been guessed before
        print(f'Uh, Oh!\nIt seems that you have already guessed this letter!\nPick again!')

if lives <= 0: #Lose condition
    os.systen('clear')
    print(f'Oh, No!\nIt seems that you were not able to save the house in time!\nThe word was: {chosen_word}\nRestart to play again!')

elif len(word) == 0: #Win condition
    os.system('clear')
    print(f'Good Job!\nYou managed to save the house from being destroyed!\nThe word was: {chosen_word}\nRestart to play again!')
