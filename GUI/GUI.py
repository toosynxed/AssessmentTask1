from tkinter import *
import random
from tkinter import messagebox
import os
import threading
from threading import Event
import tkinter as tk
from tkinter import ttk
from functools import partial

#class
#init
#structure
#introducion text boxes
#play '1', enter box
#clear screen
#Name context boxes
#Name enter box
#Clear screen
#Difficulty context boxes
#Difficulty enter box
#Clear screen
#Game normal here

#clear function:
# def clear_all_inside_frame():
        # Iterate through every widget inside the frame
        #for widget in frame1.winfo_children():
        #widget.destroy() 
        
#clear function 2
#myCanvas.delete('all')
    


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Phase Game")
        self.geometry("600x400")

        self.frames = {}

        # Container frame that holds all other frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Initialize all pages and store in a dictionary
        self.frames["Play"] = self.PlayFrame(container, self.go_to_name_page)
        self.frames["Name"] = self.NameFrame(container, self.go_to_game_page)
        self.frames["Game"] = self.GameFrame(container, self.game_input_received, lives=5, letters_remaining="A B C D", guessed_letters="", word_display="_ _ _ _")

        # Grid all frames (stacked on top of each other)
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Play")  # Start with the Play page

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    # Callbacks for frame transitions
    def go_to_name_page(self, entry_value):
        if entry_value.strip() == "1":
            self.show_frame("Name")

    def go_to_game_page(self, player_name):
        print(f"Player name entered: {player_name}")
        self.show_frame("Game")

    def game_input_received(self, letter):
        print(f"Letter guessed: {letter}")

#class House(tk.Tk):
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
    live = 0
    replay = 1
    replay_choice = True
    again = False
    '''
    def __init__(self, master):
       

        
        self.count = 0
        self.structure(master)
        self.rr=master
        self.play = False
        
        self.pull()
        self.chosen_word, self.lives, self.diff, self.word = self.return_game_values()
        
        self.name = 'Eamon'
        print(self.word)
    '''
    '''
    def __init__(self):
        super().__init__()
        self.title('Main Menu')
        self.geometry('600x400')

        # initialize main menu as frame

        self.main_menu_frame = tk.Frame(self)
        ttk.Label(self.main_menu_frame, text='Main Menu').pack()
        button1 = ttk.Button(self.main_menu_frame, text='How To Play', command=self.show_how_to_play)
        button1.pack(expand=True)
        button2 = ttk.Button(self.main_menu_frame, text='Play', command=self.init_game)
        button2.pack(expand=True)

        # Direction Screen as frame

        self.instructions_frame = tk.Frame(self)
        ttk.Label(self.instructions_frame, text='Game Insturctions').pack()
        ttk.Label(self.instructions_frame, text='another label').pack()
        ttk.Button(self.instructions_frame, text='Exit', command=partial(self.back_to_main_menu, self.instructions_frame)).pack()
        
        # Game Screen as frame

        self.game_frame = tk.Frame(self)
        ttk.Label(self.game_frame, text='Hang Man').pack()
        ttk.Button(self.game_frame, text='Exit', command=partial(self.back_to_main_menu, self.game_frame)).pack()
        ttk.Label(self.game_frame, text='another label').pack(expand=True)
        
        # only pack menu to start with
        
        self.main_menu_frame.pack()

    # function to unload the menu frame, change the window title and load instructions frame
    
    def show_how_to_play(self):
        self.main_menu_frame.pack_forget()
        self.title('How To Play')
        self.instructions_frame.pack()

    # function to unload the menu frame, change the window title and load game frame
    
    def init_game(self):
        self.main_menu_frame.pack_forget()
        self.title('Hang Man')
        self.game_frame.pack()

    # function to unload either the instructions or game frame, change the window title and load menu frame
    # since it is triggeret by both the button in game and instructions frame the button has to pass the frame to unload
   
    def back_to_main_menu(self, from_where):
        from_where.pack_forget()
        self.title('Main Menu')
        self.main_menu_frame.pack()
    '''
 
        






    def pull(self):
        for line in open(r"house_image_GUI.txt","r"): #Appending letters from easy file to the list
            self.image_display.append(line.strip())
        for x in open(r"Word Lists/easy_words.txt","r"): #Appending letters from easy file to the list
            self.easy_level.append(x.strip())
        for x in open(r"Word Lists/medium_words.txt","r"): #Appending letters from medium file to the list
            self.medium_level.append(x.strip())   
        for x in open(r"Word Lists/hard_words.txt","r"): #Appending letters from hard file to the list
            self.hard_level.append(x.strip())
        for x in open(r"alphabet.txt","r"): #Appending letters from alphabet file to the list
            self.letters_remaining.append(x.strip())
    
    def choose_word(self, level): #Function to pick a random word from the correct difficulty
            if level == "1":
                chosen_word = random.choice(self.easy_level) #Picks a random word from the list
                live = 16
                diff = 1
            elif level == "2":
                chosen_word = random.choice(self.medium_level) #Picks a random word from the list
                live = 8
                diff = 2
            elif level == "3":
                chosen_word = random.choice(self.hard_level) #Picks a random word from the list
                live = 4
                diff = 4
            else:
                return "", -1, 0
        
            return chosen_word, live, diff
    
    def return_game_values(self): #Function 
        lives = 0
        print(f'Name, Select a difficulty:')
        while lives < 1:
            difficulty = input(f'Easy [1]   Medium [2]   Hard[3]   ')
            chosen_word, lives, diff = self.choose_word(difficulty) #Assigns output from function as a global variable

        word = set(chosen_word) #Finds all distinct characters
        return chosen_word, lives, diff, word
    
    def update_image(self, diff, lives):
        img = diff*lives #calculate the difficulty multiplier for image based off remaining lives and difficulty
       
        scale = 16 - img #calculate the amount of lines to print based off 16 - multiplier
        
        image = (f'{'\n'.join(self.image_display[scale:16])}') #prints house image
        return image

    def print_word(self, chosen_word, guessed_letters):
        label = {' '.join(['_' if letter not in guessed_letters else letter for letter in chosen_word])}
        return label

    def structure(self,master):
        '''
        #Phase 1 (play)
        play = False
        
            
        self.introduction_label_1 = Label(master, text="Hey! You there!\nYeah!\nYou!\nCan you help me?\nSome people are trying to destroy my home by taking things related to a hosue from it!\nGuess the the name of what they are stealing, to prevent them from taking everything!\n\nThank you so much for helping, and Good Luck!\n")
        self.introduction_label_1.grid(row = 0, column = 0, columnspan = 2, stick = W)

        self.play_label = Label(master, text = "Enter '1', to start!")
        self.play_label.grid(row = 1, column = 0, sticky = W)

        self.play_entry = Entry(master)
        self.play_entry.grid(row = 1, column = 1, sticky = W)

        self.phase_1_space1 = Label(master, text = " ")
        self.phase_1_space1.grid(row = 2, column = 0, sticky = W)

        
        
        self.play_submit = Button(master, text = "Enter", command=self.play_enter, height = 1, width = 20)
        self.play_submit.grid(row = 3, column = 1, sticky = W)

        master.bind('<Return>', self.play_enter)

        self.phase_1_space2 = Label(master, text = " ")
        self.phase_1_space2.grid(row = 4, column = 0, sticky = W) 
        

        

        
            
                

        
        # When the code above will be validated, the
       
        
        
        #phase/screen 2 (name)
            
        self.introduction_label_1.destroy()
        self.play_label.destroy()
        self.play_entry.destroy()
        self.phase_1_space1.destroy()
        self.play_submit.destroy()
        self.phase_1_space2.destroy()

        self.name_introduction_label = Label(master, text = "THANK YOU so much! \nWhat can I call you?")
        self.name_introduction_label.grid(row = 0, column = 0, sticky = W)

        self.name_label = Label(master, text = "My name is:")
        self.name_label.grid(row = 1, column = 0, sticky = W)

        self.name_entry = Entry(master)
        self.name_entry.grid(row = 1, column = 1, sticky = W)

        self.phase_2_space1 = Label(master, text = " ")
        self.phase_2_space1.grid(row = 2, column = 0, sticky = W)

        self.name_submit = Button(master, text = "Enter", command = self.name_enter, height = 1, width = 20)
        self.name_submit.grid(row = 4, column = 0, sticky = W)

        master.bind('<Return>', self.name_enter)

        #need to put space in here:
        
        self.phase_2_space2 = Label(master, text = " ")
        self.phase_2_space2.grid(row = 4, column = 0, sticky = W)
        
       

        #phase 3 (game)

        print(self.letters_remaining)
        self.game_introduction = Label(master, text = "Welcome? - Change")
        self.game_introduction.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.game_label = Label(master, text = "Name, pick a letter:") #Where to access name?
        self.game_label.grid(row = 1, column = 0, sticky = W)

        self.game_entry = Entry(master)
        self.game_entry.grid(row = 3, column = 0, sticky = W)

        self.game_space1 = Label(master, text = " ")
        self.game_space1.grid(row = 2, column = 0, sticky = W)

        self.game_submit = Button(master, text = "Enter", command = self.game_enter, height = 1, width = 20)
        self.game_submit.grid(row = 3, column = 1, sticky = W)

        master.bind('<Return>', self.game_enter)

        self.game_space2 = Label(master, text = " ")
        self.game_space2.grid(row = 4, column = 0, sticky = W)

        #
        self.game_space3 = Label(master, text = " ")
        self.game_space3.grid(row = 5, column = 0, sticky = W)

        self.game_life_label = Label(master, text = f"Lives Remaining: {self.lives}") #add variable life here?
        self.game_life_label.grid(row = 1, column = 2, columnspan = 2, sticky = W)

        self.game_display_message = Label(master, text = " ") #what does this do?
        self.game_display_message.grid(row = 6, column = 0, columnspan = 2, sticky = W)

        #word status

        self.game_remaining_letters = Label(master, text = f"Letters Remaining: {self.letters_remaining}")
        self.game_remaining_letters.grid(row = 4, column = 0, sticky = W)

        self.game_guessed_letters = Label(master, text = self.guessed_letters)
        self.game_guessed_letters.grid(row = 5, column = 0, sticky = W)

        self.game_word_status = Label(master, text = '') #FOR IN HERE: JUST MAKE A BIT THAT PRINTS OUT FOR LENGHT OF WORD, '_'
        self.game_word_status.grid(row = 7, column = 0, sticky = W)

        self.game_status_label = Label(master, text = f"Word Status: ")
        self.game_status_label.grid(row = 6, column = 0, sticky = W)

        #imgae:

        self.house = Label(master, text = 'Enter A Letter To Start!')
        self.house.grid(row = 9, column = 0, sticky = W)
        
    def current_status(self, letter):
        self.game_current_status = Label(self.rr, text = letter)
        self.game_current_status.place(x = 100, y = 130)
'''
    def play_enter(self, *args):
        choice = self.play_entry.get()
        if choice == 1:
            play = True
            return play
            
        elif choice != 1:
            play = False  
            return play 


    def name_enter(self, *args):
        self.name = self.name_entry.get()
        if len(self.name) >= 0:
            self.play_name = True
        
        elif len(self.name) <= 0:
            self.play_name = False
        
    def game_enter(self, *args):

        self.letter = self.game_entry.get()   

        if self.lives != 0 and len(self.word) != 0: #While game is still valid, and not won or lost

            if self.letter not in self.guessed_letters and len(self.letter) == 1 and self.letter.isalpha() == True: #Makes sure that it hasn't been guessed already, is only 1 character long, is a valid letter
                
                self.letters_remaining.remove(self.letter) #Removes letter from alphabet
                self.guessed_letters.append(self.letter) #Adds letter to the list of already guessed letters
                
                if self.letter in self.word: #Checks if the letter is in the set
                
                    self.word.remove(self.letter) #Removes the correctly guessed letter from the set                     
                    
                    #self.inst_lb2.config(text='Life:'+ str(10-self.count))
                    #self.inst_lb3.config(text='Right Guessed!')

                elif self.letter not in self.word: #If not in set
                    
                    self.lives = self.lives - 1 #Lose a life, and image changes ****** IMAGE CHANGES HERE PLEASE!!! ******
                    print(f'Uh, Oh!\nName, It seems that this letter is not in the word!\nYou have {self.lives} lives remaining!') #Feedback off incorrect guess
                    
                    #self.inst_lb2.config(text='Life:'+ str(10-self.count))
                    #self.inst_lb3.config(text='Right Guessed!')

            elif self.letter.isalpha() == False or len(self.letter) != 1: #If input isn't a letter or only 1 character long
                print(f'Uh, Oh!\nName, You have entered an invalid input!\nPick again!')

            elif self.letter in self.guessed_letters: #If input has already been guessed before
                print(f'Uh, Oh!\nName, It seems that you have already guessed this letter!\nPick again!')
        
            #print(f'{'\n'.join(image_display[self.scale:16])}') #prints house image

        if self.lives <= 0: #Lose condition
            
            print(f"Oh, No!\nName, you weren't able to save the house in time! The people were trying to take my {self.chosen_word}.")
            exit()
            
        elif len(self.word) == 0: #Win condition
            
            print(f'Good Job Name!\nYou managed to save my house from being destroyed!\nThe people were trying to take my {self.chosen_word}')
            exit()

        self.game_guessed_letters.config(text = f"Letters Guessed: {' '.join(self.guessed_letters)}")
        self.game_life_label.config(text = f"Lives Remaining: {self.lives}")
        self.house.config(text = self.update_image(self.diff, self.lives))
        self.game_word_status.config(text = ' '.join(self.print_word(self.chosen_word, self.guessed_letters)))
        self.game_remaining_letters.config(text = f"Letters Remaining: {' '.join(self.letters_remaining)}")


         
'''    
root = Tk()
root.title("Hangman Game")
root.geometry("800x480")
app = House(root)
root.mainloop()
'''
house = App()
house.mainloop()