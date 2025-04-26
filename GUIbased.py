from tkinter import *
import random
from tkinter import messagebox
#root = tk.Tk()
root = Tk()
root.title("Guess The Word!")
root.geometry("500x500")

manlabel = Label(root, font=("CourierK", 16))
manlabel.grid(row=0, column=0)
manlabel.config(text="Welcome to Build A House!")
word_choices = ['apple', 'banana', 'cherry', 'date', 'elderberry']
word = random.choice(word_choices)
word = 'cherry' #just here to ensure that during testing, all variables remain the same
word_in_list_form = list(word)

length_of_chosen_word = len(word)
display_letters = []
display_letters = word_in_list_form
for i in range(0,length_of_chosen_word):
	display_letters[i] = '_'	
already_guessed = []
correct_score = 0
chn = 0
picked = 0
strike = 0
underscore_display_letters = []
underscore_display_letters = ' '.join(display_letters)
class House:
    def __init__(boxs,master):
        boxs.count=0
        boxs.main(master)
        boxs.rr=master
        #Input function#
    def main(boxs,master):
        #guess label#
        boxs.guessbox = Label(master, text="Pick a letter: ", font=("Arial", 16))
        boxs.guessbox.grid(row=1, column=0, sticky=W)
        #guess box#
        boxs.guess = Entry(master)
        boxs.guess.grid(row=1, column=1, sticky=W)
        #space#
        boxs.space = Label(master,)

		
#word_label = tk.Label(root, text=underscore_display_letters, font=("Arial", 24))
#word_label.grid(row=102, column=0)  


root.geometry("580x480")


app = House(root)
      
root.mainloop()

