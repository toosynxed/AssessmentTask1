import tkinter as tk

root = tk.Tk()
root.title("Man")

manlabel = tk.Label(root, font=("CourierK", 16))
manlabel.grid(row=0, column=0)

word = "tree"
word_with_blanks = '_' * len(word)
word_label = tk.Label(root, text=word_with_blanks, font=("Arial", 24))
word_label.grid(row=1, column=0)        

