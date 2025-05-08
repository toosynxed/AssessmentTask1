from tkinter import *
import random
from tkinter import messagebox

class House():
    #Initialises lists
    easy_level = []
    medium_level = []
    hard_level = []
    image_display = []
    guessed_letters = [] 
    letters_remaining = [] 
    #Initialises variables
    lives = 0
    diff = 0
    img = 0
    scale = 0
    
    

    def __init__(self, master): #Initalises structure as the main.
        self.structure(master)
        self.rr=master
        self.pull() #Initialises and fills lists from files

    def pull(self): #Command to pull info from files and add to lists
        for line in open(r"Packet_Eamon_Wong/house_image_GUI.txt","r"): #Appending house image lines to the list
            self.image_display.append(line.strip())
        for x in open(r"Packet_Eamon_Wong/Word Lists/easy_words.txt","r"): #Appending letters from easy file to the list
            self.easy_level.append(x.strip())
        for x in open(r"Packet_Eamon_Wong/Word Lists/medium_words.txt","r"): #Appending letters from medium file to the list
            self.medium_level.append(x.strip())   
        for x in open(r"Packet_Eamon_Wong/Word Lists/hard_words.txt","r"): #Appending letters from hard file to the list
            self.hard_level.append(x.strip())
        for x in open(r"Packet_Eamon_Wong/alphabet.txt","r"): #Appending letters from alphabet file to the list
            self.letters_remaining.append(x.strip())

    def update_image(self, diff, lives): #Command to update image dispaly
        self.img = self.diff*self.lives #calculate the difficulty multiplier for image based off remaining lives and difficulty
       
        self.scale = 16 - self.img #calculate the amount of lines to print based off 16 - multiplier
        
        image = (f'{'\n'.join(self.image_display[self.scale:16])}') #defines house image
        return image

    def print_word(self, chosen_word, guessed_letters): #Command to update the word display
        label = {' '.join(['_' if letter not in guessed_letters else letter for letter in chosen_word])} #Defines the output of the word status
        return label
    
    def set_game_difficulty_easy(self, *args): #Command for easy level button
        self.chosen_word = random.choice(self.easy_level) #Picks a random word from the list
        self.lives = 16
        self.diff = 1
        self.word = set(self.chosen_word) #Finds all distinct character
        #Removes/hides difficulty choice buttons to allow space for the main game functions
        self.game_difficulty_selector_easy.destroy() 
        self.game_difficulty_selector_medium.destroy()
        self.game_difficulty_selector_hard.destroy()
        self.game_difficulty_selector_label.destroy()
        self.game_cover_box.destroy()
        self.game_introduction.destroy()
        
    def set_game_difficulty_medium(self, *args): #Command for medium level button
        self.chosen_word = random.choice(self.medium_level) #Picks a random word from the list
        self.lives = 8
        self.diff = 2
        self.word = set(self.chosen_word) #Finds all distinct character
        #Removes/hides difficulty choice buttons to allow space for the main game functions
        self.game_difficulty_selector_easy.destroy()
        self.game_difficulty_selector_medium.destroy()
        self.game_difficulty_selector_hard.destroy()
        self.game_difficulty_selector_label.destroy()
        self.game_cover_box.destroy()
        self.game_introduction.destroy()
        
    def set_game_difficulty_hard(self, *args): #Command for hard level button
        self.chosen_word = random.choice(self.hard_level) #Picks a random word from the list
        self.lives = 4
        self.diff = 4    
        self.word = set(self.chosen_word) #Finds all distinct character
        #Removes/hides difficulty choice buttons to allow space for the main game functions
        self.game_difficulty_selector_easy.destroy()
        self.game_difficulty_selector_medium.destroy()
        self.game_difficulty_selector_hard.destroy()
        self.game_difficulty_selector_label.destroy()
        self.game_cover_box.destroy()
        self.game_introduction.destroy()
        
    def structure(self, master): #Main structure for GUI visuals
        
        self.game_cover_box = Label(master, text = ' ', width = 100, height = 100) #This box lays-over the main game layout, and sits below difficulty choice buttons. This is to "create" a new page.
        self.game_cover_box.grid(row = 1, column = 0, sticky = W)

        self.game_difficulty_selector_label = Label(master, text = "Select a difficulty:") #Difficulty information label.
        self.game_difficulty_selector_label.place(x = 147, y = 170)
        self.game_difficulty_selector_label.tkraise()

        self.game_difficulty_selector_easy = Button(master, text = 'Easy', command = self.set_game_difficulty_easy, height = 2, width = 10, highlightbackground = "#5efc03" ) #Easy difficulty level button
        self.game_difficulty_selector_easy.place(x = 142, y = 200)
        self.game_difficulty_selector_easy.tkraise()

        self.game_difficulty_selector_medium = Button(master, text = 'Medium', command = self.set_game_difficulty_medium, height = 2, width = 10, highlightbackground = "#fc9803") #Medium difficulty level button
        self.game_difficulty_selector_medium.place(x = 142, y = 250)
        self.game_difficulty_selector_medium.tkraise(aboveThis=None)

        self.game_difficulty_selector_hard = Button(master, text = 'Hard', command = self.set_game_difficulty_hard, height = 2, width = 10, highlightbackground = "#fc0303") #Hard difficulty level button
        self.game_difficulty_selector_hard.place(x = 142, y = 300)
        self.game_difficulty_selector_hard.tkraise()
        
        self.game_introduction = Label(master, text = f"Hey!\nCan you help me?\nSome people are trying to destroy my home by taking things\n related to a hosue from it!\nGuess the the name of what they are stealing, to prevent them from taking everything!\n\nThank you so much for helping, and Good Luck!\n", wraplength = 450) #Introduction label that provides context for game, sits infront of the box for first "page".
        self.game_introduction.grid(row = 0, column = 0, columnspan = 4, sticky = W)
        self.game_introduction.tkraise()

        self.game_label = Label(master, text = "Pick a letter!") #This is the label to prompt the user to enter a letter.
        self.game_label.grid(row = 1, column = 0, sticky = W)

        self.game_entry = Entry(master) #This is the entry box for the user to enter a letter
        self.game_entry.grid(row = 3, column = 0, sticky = W)

        self.game_space1 = Label(master, text = " ") #Space to gap layout
        self.game_space1.grid(row = 2, column = 0, sticky = W)

        self.game_submit = Button(master, text = "Enter", command = self.game_enter, height = 1, width = 20, foreground = '#50c4fa', border = 1, activeforeground = '#50c4fa', highlightcolor = '#50c4fa', highlightthickness = 1) #This is the button that submits what has been entered into the guess box, and runs/calls a command to process it.
        self.game_submit.place(x = 198, y = 41)
        self.game_submit.tkraise(aboveThis=self.game_cover_box)

        master.bind('<Return>', self.game_enter) #Allows the user to enter the letter in the guess box using the 'enter' key.
    
        self.game_space2 = Label(master, text = " ") #Space to gap layout
        self.game_space2.grid(row = 4, column = 0, sticky = W)

        self.game_space3 = Label(master, text = " ") #Space to gap layout
        self.game_space3.grid(row = 5, column = 0, sticky = W)

        self.game_life_label = Label(master, text = f"Lives Remaining: {self.lives}") #This is the label that displays the current amount of lives remaining for the user
        self.game_life_label.place(x = 203, y = 0)
        self.game_life_label.tkraise(aboveThis=self.game_cover_box)

        self.game_display_message = Label(master, text = " ") #This is the label that will display input feedback when a guess/letter is entered/guessed.
        self.game_display_message.grid(row = 6, column = 0, columnspan = 2, sticky = W)

        self.game_remaining_letters = Label(master, text = f"Letters Remaining: {self.letters_remaining}") #This label displays the letters that can still be guessed
        self.game_remaining_letters.grid(row = 4, column = 0, sticky = W)

        self.game_guessed_letters = Label(master, text = self.guessed_letters) #This label displays the letters that have already been guessed by the user.
        self.game_guessed_letters.grid(row = 5, column = 0, sticky = W)

        self.game_word_status = Label(master, text = '') #This label displays the status of the guessed word
        self.game_word_status.grid(row = 7, column = 0, sticky = W)

        self.game_status_label = Label(master, text = f"Word Status: ") #Label that provides some context for the word display above.
        self.game_status_label.grid(row = 6, column = 0, sticky = W)

        self.house = Label(master, text = 'Hit The Enter Key To Start!') #This provides some context on how to start the game running after the difficulty is chosen, is removed after difficulty selection.
        self.house.grid(row = 9, column = 0, sticky = W)

        self.game_indicator = Label(master, text = '') #This label will display the feedback from the users inputed/guessed letter
        self.game_indicator.place(x = 203, y = 160)
        self.game_indicator.tkraise(aboveThis=self.game_cover_box)

    def game_enter(self, *args): #This is the main game function that runs when a guess is inputted

        self.letter = self.game_entry.get() #Gets input from box

        if self.lives != 0 and len(self.word) != 0: #While game is still valid, and not won or lost

            if self.letter not in self.guessed_letters and len(self.letter) == 1 and self.letter.isalpha() == True: #Makes sure that it hasn't been guessed already, is only 1 character long, is a valid letter
                
                self.letters_remaining.remove(self.letter) #Removes letter from alphabet
                self.guessed_letters.append(self.letter) #Adds letter to the list of already guessed letters
                
                if self.letter in self.word: #Checks if the letter is in the set
                
                    self.word.remove(self.letter) #Removes the correctly guessed letter from the set                     
                    self.game_indicator.config(text = f"Good Job!\nYou have guessed a correct letter!", bg = 'orange', wraplength = 200, pady = 10, padx = 10, width = 20)
                   
                elif self.letter not in self.word: #If not in set
                    
                    self.lives = self.lives - 1 #Lose a life, and image changes
                    self.game_indicator.config(text = f"Uh, Oh!\nIt seems that this letter is not in the word!\nYou have {self.lives} lives remaining!", bg = 'orange', wraplength = 200, pady = 10, padx = 10, width = 20) #Updates the indicator label with feedback that it is an incorrect guess
                
            elif self.letter.isalpha() == False or len(self.letter) != 1: #If input isn't a letter or only 1 character long
                
                self.game_indicator.config(text = f"Uh, Oh!\nYou have entered an invalid input!\nPick again!", bg = 'orange', wraplength = 200, pady = 10, padx = 10, width = 20) #Updates indicator label that the input is and invalid guess

            elif self.letter in self.guessed_letters: #If input has already been guessed before
                
                self.game_indicator.config(text = f"Uh, Oh!\nIt seems that you have already guessed this letter!\nPick again!", bg = 'orange', wraplength = 200, pady = 10, padx = 10, width = 20) #Updates indicator label that the input has already been guessed.

        if self.lives <= 0: #Lose condition
            
            message = f"Oh, No!\nYou weren't able to save the house in time! The people were trying to take my {self.chosen_word.upper()}."
            self.game_indicator.config(text = message, bg = '#fa2020', height = 15, fg = 'white', font = ("Arial", 15)) #Updates indicator with lose condition message, outlined above.
            
        elif len(self.word) == 0: #Win condition
            message = f"Good Job!\nYou managed to save my house from being destroyed!\nThe people were trying to take my {self.chosen_word.upper()}."                                                                                                                #FIX HERE   FIXE HERE   FIX HERE
            self.game_indicator.config(text = message, bg = '#3dff08', height = 15, fg = 'red', font = ("Arial", 15)) #Updates indicator with win condition message, outlined above.

        self.game_guessed_letters.config(text = f"Letters Guessed: {' '.join(self.guessed_letters)}") #Updates letters guessed label
        self.game_life_label.config(text = f"Lives Remaining: {self.lives}") #Updates lives remaining label
        self.house.config(text = self.update_image(self.diff, self.lives)) #Updates image display
        self.game_word_status.config(text = ' '.join(self.print_word(self.chosen_word, self.guessed_letters))) #Updates word status label
        self.game_remaining_letters.config(text = f"Letters Remaining: {' '.join(self.letters_remaining)}") #Update remaining letters label

root = Tk() #Sets root
root.title("Save The House!") #Window title
root.geometry("417x480") #Window size


app = House(root) #Creates object 'app'
root.mainloop() #Runs object 'app'

