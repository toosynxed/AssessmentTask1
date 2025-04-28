from tkinter import *
import random
from tkinter import messagebox
#root = tk.Tk()
#root = Tk()
#root.title("Guess The Word!")
#root.geometry("500x500")

#manlabel = Label(root, font=("CourierK", 16))
#manlabel.grid(row=0, column=0)
#manlabel.config(text="Welcome to Build A House!")
#word_choices = ['apple', 'banana', 'cherry', 'date', 'elderberry']
#word = random.choice(word_choices)
#word = 'cherry' #just here to ensure that during testing, all variables remain the same
#word_in_list_form = list(word)

#length_of_chosen_word = len(word)
#display_letters = []
#display_letters = word_in_list_form
#for i in range(0,length_of_chosen_word):
#	display_letters[i] = '_'	
#already_guessed = []
#correct_score = 0
#chn = 0
#picked = 0
#strike = 0
#underscore_display_letters = []
#underscore_display_letters = ' '.join(display_letters)
class House:
    #picked = 0
    def __init__(self,master):
        self.count=0
        self.structure(master)
        self.rr=master
        
        #Input function#
    def structure(self, master, play, word, display_letters, already_guessed, strike):
        self.yes = play
        self.chosen = word
        self.display = display_letters
        self.guessed = already_guessed
        self.strike_out = strike

    def add(self,master,play,word):
        return play + word
dog = House(1)
dog = House.structure(1,2,3,4,5,6,7,8,9)
print(dog.add())



    
    



		
#word_label = tk.Label(root, text=underscore_display_letters, font=("Arial", 24))
#word_label.grid(row=102, column=0)  


#root.geometry("580x480")


#app = House(root)
      
#root.mainloop()

