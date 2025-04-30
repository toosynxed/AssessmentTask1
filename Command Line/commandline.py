import os
import random
os.system('cledsar') #Clear terminal
alphabet = open(r"alphabet.txt","r") #call file
image = open(r"house_image.txt","r")
print(alphabet)
easy_words = open(r"Word Lists/easy_words.txt","r") 
medium_words = open(r"Word Lists/medium_words.txt","r")
hard_words = open(r"Word Lists/hard_words.txt","r")

def choose_word(level): #Function to pick a random word from the correct difficulty
    if level == "1":
        chosen_word1 = random.choice(easy_level) #Picks a random word from the list
        live = 16
        diffs = 1
    elif level == "2":
        chosen_word1 = random.choice(medium_level) #Picks a random word from the list
        live = 8
        diffs = 2
        
    elif level == "3":
        chosen_word1 = random.choice(hard_level) #Picks a random word from the list
        live = 4
        diffs = 4
    else:
        return "", -1
    
    return chosen_word1, live, diff
def return_game_values():
    lives = 0
    print(f'Select a difficulty:')
    while lives < 1:
        difficulty = input(f'Easy [1]   Medium [2]   Hard[3]   ')
        chosen_word, lives, diff = choose_word(difficulty) #Assigns output from function as a global variable
    word = set(chosen_word) #Finds all distinct characters
    return chosen_word, lives, diff, word
    
def game():
    
    
    replay_choice = False
    #return_game_values()
    chosen_word, lives, diff, word = return_game_values()
    while lives != 0 and len(word) != 0: #While game is still valid, and not won or lost
        print(f'Letters Remaining: {' '.join(letters_remaining)}') #Letters left to guess
        print(f'Letters Guessed: {' '.join(guessed_letters)}') #Letters already guessed
        print(f'Word Status: {' '.join(['_' if letter not in guessed_letters else letter for letter in chosen_word])}') #Prints out underscored word
    # for line in image: #Appending letters from hard file to the list
        #    image_display.append(line.replace('p', '\n'))
        img = diff*lives
        print(img)
        scale = 16 - img
        print(scale)
        print(f'{'\n'.join(image_display[scale:16])}')

        letter = input('Pick a letter: ').lower() #Input line
        #os.system('clear')
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
        # os.system('clear')
        print(f'Oh, No!\nIt seems that you were not able to save the self in time!\nThe word was: {chosen_word}\nRestart to play again!')
        
        

    elif len(word) == 0: #Win condition
        #   os.system('clear')
        print(f'Good Job!\nYou managed to save the self from being destroyed!\nThe word was: {chosen_word}\nRestart to play again!')

def play_again(choice):
    
    if choice == 1:
        again = True
        return again
    else:
        again = False
        return again


answer = '1'
def pull():
    for line in image: #Appending letters from easy file to the list
        image_display.append(line.replace('\n', ''))
    for x in easy_words: #Appending letters from easy file to the list
        easy_level.append(x.replace('\n', ''))
    for x in medium_words: #Appending letters from medium file to the list
        medium_level.append(x.replace('\n', ''))   
    for x in hard_words: #Appending letters from hard file to the list
        hard_level.append(x.replace('\n', ''))
    for x in alphabet: #Appending letters from alphabet file to the list
        letters_remaining.append(x.replace('\n', ''))

diffs = 0
easy_level = []
medium_level = []
hard_level = []
image_display = []
guessed_letters = [] #Initialises list
letters_remaining = [] #Initialises list
image = []
alphabet = []
lives = 0
diff = 0
img = 0
scale = 0
word = ''
live = 0
replay = 1
replay_choice = True
again = False


while answer == '1':
    # object = level
    # properties = words inside list, lives values

    print('hello')
    for letters in image: #Appending letters from easy file to the list
        image_display.append(letters.replace('\n', ''))
   
    for letters in alphabet: #Appending letters from alphabet file to the list
        letters_remaining.append(letters.replace('\n', ''))
    
    print(letters_remaining)
    print(image_display)
    print(hard_level)
    print(easy_level)
    print('mhm')
    game()
    diffs = 0
    easy_level = []
    medium_level = []
    hard_level = []
    image_display = []
    guessed_letters = [] #Initialises list
    letters_remaining = [] #Initialises list
    image = []
    alphabet = []
    lives = 0
    diff = 0
    img = 0
    scale = 0
    word = ''
    live = 0
    replay = 1
    replay_choice = True
    again = False
    for x in image: #Appending letters from easy file to the list
        image_display.append(x.replace('\n', ''))
    for x in easy_words: #Appending letters from easy file to the list
        easy_level.append(x.replace('\n', ''))
    for x in medium_words: #Appending letters from medium file to the list
        medium_level.append(x.replace('\n', ''))   
    for x in hard_words: #Appending letters from hard file to the list
        hard_level.append(x.replace('\n', ''))
    for line in alphabet: #Appending letters from alphabet file to the list
        letters_remaining.append(x.replace('\n', ''))
    answer = int(input("Enter 1 to play again: "))
   
    #terminal.replay = int(input("To play again, enter '1'\nTo exit, enter any other key: "))
    #terminal.replay_choice = terminal.play_again(terminal.replay)
    
  
    
#print(chosen_word)
#print(word)
#lives = len(chosen_word) #Sets the life value  ***** LATER CHANGE THIS TO SET VALUE AFTER CREATING IMAGE OF self *****



#print(f'Word Status: {' '.join(['_' if letter not in guessed_letters else letter for letter in chosen_word])}')
