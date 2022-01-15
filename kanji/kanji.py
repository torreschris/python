import random
import csv
import os
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Learn Kanji")

        dir_path = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(dir_path, 'allkanji.csv')
        mydict = csv.DictReader(open(filepath))
        self.mydict = []
        for row in mydict:
            self.mydict.append(row)

        # Add method to read JSON file (if exists) and set EXP column to 5 

        self.guess = ''
        self.num_guesses = 0
        self.randomrow = 0
        self.level = 1

        self.message = "Kanji Game"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        self.status_message = "Lvl {}".format(self.level)
        self.status_label_text = StringVar()
        self.status_label_text.set(self.status_message)
        self.status_Label = Label(master, textvariable=self.status_label_text)

        self.entry = Entry(master)

        self.guess_button = Button(master, text="Start", command=self.guess_kanji)
        self.reset_button = Button(master, text="Next", command=self.reset, state=DISABLED)

        self.label.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky=W+E)
        self.label.configure(font=("Courier", 44))

        self.entry.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky=W+E)
        self.guess_button.grid(row=2, column=0, padx=5, pady=5)
        self.reset_button.grid(row=2, column=1, padx=5, pady=5)
        self.status_Label.grid(row=3, columnspan=2, padx=5, pady=5)

    def pick_Random_Kanji(self):
        while True:
            self.randomrow = random.randint(0, len(self.mydict)-1)
            if int(self.mydict[self.randomrow]['level']) <= self.level:
                break
        self.message = self.mydict[self.randomrow]['japanese']     
        self.label_text.set(self.message)

        # If empty row try again
        if not self.mydict[self.randomrow]['pronounciation']:
            self.pick_Random_Kanji()
        
        if int(self.mydict[self.randomrow]['level']) > self.level:
            print(int(self.mydict[self.randomrow]['level']))
            self.pick_Random_Kanji()
        

    def guess_kanji(self):
        if self.guess_button['text'] == 'Start':
            self.guess_button.configure(text='Submit')
            self.pick_Random_Kanji()
            return

        pronounciation = self.mydict[self.randomrow]['pronounciation']
        translation = self.mydict[self.randomrow]['translation']
        self.guess = self.entry.get().strip()
        if not self.guess:
            return
        elif self.guess == pronounciation:
            self.message = "Correct!\n{}: {}\nTranslation: {}".format(
                self.message, pronounciation, translation)
        else:
            self.message = "Incorrect\n{}: {}\nTranslation: {}".format(
                self.message, pronounciation, translation)

        self.label_text.set(self.message)
        self.guess_button.configure(state=DISABLED)
        self.reset_button.configure(state=NORMAL)

    def reset(self):
        self.entry.delete(0, END)
        self.guess = ''
        self.randomrow = 0

        self.pick_Random_Kanji()

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()