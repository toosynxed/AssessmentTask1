import tkinter as tk
from threading import Thread
from cookie_clicker_bot import CookieClickerBot

class App:
    def __init__(self):
        self.create_variables()
        self.window_setup()
        self.create_start_gui()
        self.bot_thread = None
        self.run()


    def create_variables(self):
        self.clicking = False


    def window_setup(self):
        self.WINDOW = tk.Tk()
        self.WINDOW.title("CookieClikerBotGUI")


    def open_clicker(self):
        self.clicker = CookieClickerBot()
        self.clicker.stop_clicking = True
        self.bot_thread = Thread(target=self.clicker.click_cookie)
        self.bot_thread.start()
        self.create_gui()


    def create_gui(self):
        self.open_website_button.pack_forget()

        self.start_stop_button = tk.Button(self.WINDOW, text="Start Clicker", command=self.toggle_clicker, width=20, height=2)
        self.start_stop_button.pack(padx=10, pady=10)


    def create_start_gui(self):
        self.open_website_button = tk.Button(self.WINDOW, text="Open Website", command=self.open_clicker, width=20, height=2)
        self.open_website_button.pack(padx=10, pady=10)


    def toggle_clicker(self):
        if self.clicking:
            self.clicking = False
            self.clicker.stop_clicking = True
            self.start_stop_button.config(text="Start Clicker")
        else:
            self.clicking = True
            self.clicker.stop_clicking = False
            self.bot_thread = Thread(target=self.clicker.click_cookie)
            self.bot_thread.start()
            self.start_stop_button.config(text="Stop Clicker")


    def run(self):
        self.WINDOW.mainloop()

if __name__ == "__main__":
    App().run()