import os
import random
os.system('clear') #Clear terminal
alphabet = open(r"alphabet.txt","r") #call file
image = open(r"house_image.txt","r")

easy_words = open(r"Word Lists/easy_words.txt","r") 
medium_words = open(r"Word Lists/medium_words.txt","r")
hard_words = open(r"Word Lists/hard_words.txt","r")

easy_level = []
medium_level = []
hard_level = []
image_display = []
guessed_letters = [] #Initialises list
letters_remaining = [] #Initialises list

lives = 0
diff = 0
img = 0
scale = 0
word = ''
live = 0
replay = 1
replay_choice = True
again = False
    
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

def choose_word(level): #Function to pick a random word from the correct difficulty
    if level == "1":
        chosen_word = random.choice(easy_level) #Picks a random word from the list
        live = 16
        diff = 1
    elif level == "2":
        chosen_word = random.choice(medium_level) #Picks a random word from the list
        live = 8
        diff = 2
    elif level == "3":
        chosen_word = random.choice(hard_level) #Picks a random word from the list
        live = 4
        diff = 4
    else:
        return "", -1
    
    return chosen_word, live, diff

def return_game_values(): #Function 
    lives = 0
    print(f'{name}, Select a difficulty:')
    while lives < 1:
        difficulty = input(f'Easy [1]   Medium [2]   Hard[3]   ')
        chosen_word, lives, diff = choose_word(difficulty) #Assigns output from function as a global variable
    word = set(chosen_word) #Finds all distinct characters
    return chosen_word, lives, diff, word

def game():
    print(f"Good Luck, {name}!")
    pull() #Set values of lists
    replay_choice = False
    #return_game_values()
    chosen_word, lives, diff, word = return_game_values() #sets these values for later on
    while lives != 0 and len(word) != 0: #While game is still valid, and not won or lost
        print(f'Letters Remaining: {' '.join(letters_remaining)}') #Letters left to guess
        print(f'Letters Guessed: {' '.join(guessed_letters)}') #Letters already guessed
        print(f'Word Status: {' '.join(['_' if letter not in guessed_letters else letter for letter in chosen_word])}') #Prints out underscored word
    # for line in image: #Appending letters from hard file to the list
        #    image_display.append(line.replace('p', '\n'))
        img = diff*lives #calculate the difficulty multiplier for image based off remaining lives and difficulty
        print(img)
        scale = 16 - img #calculate the amount of lines to print based off 16 - multiplier
        print(scale)
        print(f'{'\n'.join(image_display[scale:16])}') #prints house image

        letter = input(f'{name}, pick a letter: ').lower() #Input line
        os.system('clear') #Clear terminal
        if letter not in guessed_letters and len(letter) == 1 and letter.isalpha() == True: #Makes sure that it hasn't been guessed already, is only 1 character long, is a valid letter
            letters_remaining.remove(letter) #Removes letter from alphabet
            guessed_letters.append(letter) #Adds letter to the list of already guessed letters

        # print(f'Wordd Status: {' '.join(['_' if letter not in guessed_letters else letter for letter in chosen_word])}')

            if letter in word: #Checks if the letter is in the set
                #print(f'{' '.join(['_' if letter not in guessed_letters else letter for letter in chosen_word])}')

                word.remove(letter) #Removes the correctly guessed letter from the set
                #letters_remaining.remove(letter)
                print(f'Good Job {name}! You have guessed a correct letter!')
                print(f'You have {lives} lives remaining!')
                #print(f'Letters Remaining: {' '.join(letters_remaining)}') #Letters left to guess
                #print(f'Letters Guessed: {' '.join(guessed_letters)}') #Letters already guessed

            elif letter not in word: #If not in set
                lives = lives - 1 #Lose a life, and image changes ****** IMAGE CHANGES HERE PLEASE!!! ******
                print(f'Uh, Oh!\n{name}, It seems that this letter is not in the word!\nYou have {lives} lives remaining!') #Feedback off incorrect guess

        elif letter.isalpha() == False or len(letter) != 1: #If input isn't a letter or only 1 character long
            print(f'Uh, Oh!\n{name}, You have entered an invalid input!\nPick again!')

        elif letter in guessed_letters: #If input has already been guessed before
            print(f'Uh, Oh!\n{name}, It seems that you have already guessed this letter!\nPick again!')

    if lives <= 0: #Lose condition
        os.system('clear')
        print(f"Oh, No!\n{name}, you weren't able to save the house in time! The people were trying to take my {chosen_word}.")
        
    elif len(word) == 0: #Win condition
        os.system('clear')
        print(f'Good Job {name}!\nYou managed to save my house from being destroyed!\nThe people were trying to take my {chosen_word}')

def play_again(choice): #Function to decide, based off an input from user, if they want to play again or not.
    
    if choice == 1:
        again = True
        return again
    else:
        again = False
        return again

#Start Game Code Here:

print(f"Hey! You there!\nYeah!\nYou!\nCan you help me?\nSome people are trying to destroy my home by taking things related to a hosue from it!\nGuess the the name of what they are stealing, to prevent them from taking everything!\n\nThank you so much for helping, and Good Luck!\n")
# ^Context for game
replay_choice = int(input(f"Enter '1', to start! ")) #To start game, enter 1
replay_choice = play_again(replay)

name = input(f"\nTHANK YOU so much!\nWhat can I call you?\n > My name is: ")

while play_again(replay_choice) == True:
    # object = level
    # properties = words inside list, lives values
    game()
    replay = int(input(f"To play again {name}, enter '1'\nor to exit, enter any other key: "))
    replay_choice = play_again(replay)
