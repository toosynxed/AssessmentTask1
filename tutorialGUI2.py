# Importing tkinter
import tkinter as tk

# Function to clear out all widgets inside a frame
def clear_all_inside_frame():
    # Iterate through every widget inside the frame
    for widget in frame1.winfo_children():
        widget.destroy()  # deleting widget
# GUI
root = tk.Tk()
root.title("GFG")
root.geometry("400x200")
# Frame 
frame1 = tk.Frame(root, width=300, height=100)
frame1.pack()
# Label is inside the frame
label1 = tk.Label(frame1, text="Welcome to GeeksforGeeks", 
                  font=("Arial", 12, "bold"),bg="green",fg="white")
label1.pack()
# Button is inside the frame
btn1 = tk.Button(frame1,text="This is a button inside frame")
btn1.pack()
# Button outside the frame to delete all widgets inside the frame 'frame1'.
clear_button = tk.Button(root,text="Clear all",command=clear_all_inside_frame)
clear_button.pack(pady=25)
root.mainloop()