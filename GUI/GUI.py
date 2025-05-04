from tkinter import *
import random
from tkinter import messagebox
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


class House:
    def __init__(self,master):
        self.count = 0
        self.structure(master)
        self.rr=master
   
    def structure(self,master):
        #Phase 1 (play)
        """ 
        self.introduction_label_1 = Label(master, text="Hey! You there!\nYeah!\nYou!\nCan you help me?\nSome people are trying to destroy my home by taking things related to a hosue from it!\nGuess the the name of what they are stealing, to prevent them from taking everything!\n\nThank you so much for helping, and Good Luck!\n")
        self.introduction_label_1.grid(row = 0, column = 0, columnspan = 2, stick = W)

        self.play_label = Label(master, text = "Enter '1', to start!")
        self.play_label.grid(row = 1, column = 0, sticky = W)

        self.play_entry = Entry(master)
        self.play_entry.grid(row = 1, column = 1, sticky = W)

        self.phase_1_space1 = Label(master, text = " ")
        self.phase_1_space1.grid(row = 2, column = 0, sticky = W)

        self.play_submit = Label(master, text = "Enter", command=self.play_enter, height = 1, width = 20)
        self.play_submit.grid(row = 3, column = 1, sticky = W)

        master.bind('<Return>', self.play_enter)

        self.phase_1_space2 = Label(master, text = " ")
        self.phase_1_space2.grid(row = 4, column = 0, sticky = W) 
        """
        '''
        #phase/screen 2 (name)

        self.name_introduction_label = Label(master, text = "THANK YOU so much! \nWhat can I call you?")
        self.name_introduction_label.grid(row = 0, column = 0, sticky = W)

        self.name_label = Label(master, text = "My name is:")
        self.name_label.grid(row = 1, column = 0, sticky = W)

        self.name_entry = Entry(master)
        self.name_entry.grid(row = 1, column = 1, sticky = W)

        self.phase_2_space1 = Label(master, text = " ")
        self.phase_2_space1.grid(row = 2, column = 0, sticky = W)

        self.name_submit = Button(master, text = "Enter", command=self.name_enter, height = 1, width = 20)
        self.name_submit.grid(row = 4, column = 0, sticky = W)

        master.bind('<Return>', self.name_enter)

        #need to put space in here:
        
        self.phase_2_space2 = Label(master, text = " ")
        self.phase_2_space2.grid(row = 4, column = 0, sticky = W)
        '''
        #Reset button?

        #phase 3 (game)

        self.game_introduction = Label(master, text = "Welcome? - Change")
        self.game_introduction.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.game_label = Label(master, text = "{name}, pick a letter:") #Where to access name?
        self.game_label.grid(row = 1, column = 0, sticky = W)

        self.game_entry = Entry(master)
        self.game_entry.grid(row = 3, column = 0, sticky = W)

        self.game_space1 = Label(master, text = " ")
        self.game_space1.grid(row = 2, column = 0, sticky = W)

        #self.game_submit = Button(master, text = "Enter", command = self.game_enter, height = 1, width = 20)
        #self.game_submit.grid(row = 3, column = 1, sticky = W)

        #master.bind('<Return>', self.game_enter)

        self.game_space2 = Label(master, text = " ")
        self.game_space2.grid(row = 4, column = 0, sticky = W)

        #phase 4:

#hello



root = Tk()
root.title("Hangman Game")
root.geometry("580x480")
app = House(root)
root.mainloop()