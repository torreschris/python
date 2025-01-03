import random
import csv
import os
import codecs
import webbrowser
from urllib import parse
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E
from PIL import ImageTk,Image

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Learn Kanji")
        master.eval('tk::PlaceWindow . center')
        master.protocol("WM_DELETE_WINDOW", self.on_close)

        self.read_csv_kanji()

        self.guess = ''
        self.num_guesses = 0
        self.randomrow = 0
        self.level = 1
        self.stage = 1
        self.total_exp = 0
        self.kanji_exp = 0
        self.reviewcard_handicap = 4
        self.kanji_cards = 0
        self.current_kanji = None
        self.previous_kanji = None
        self.file_name = None
        self.POKEBALLS = list(range(0,5))
        
        self.SPRITE_SHEETS = [['sprites/Pokemon 1st Generation Normal.png',256, 15, 15]]
        self.sprites = []
        self.loadPokemonImages()

        self.message = "Kanji Game"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)
        self.label.configure(font=("Courier", 44))
        self.label.bind("<Button-1>", lambda e : self.open_url())
        
        # Statusbar 
        self.status_label_text = StringVar()
        self.status_Label = Label(master, textvariable=self.status_label_text, bg='grey')
        self.level_up_check()
        self.update_status()

        self.entry = Entry(master)
        self.entry.bind('<Return>', self.return_Event)
        self.entry.configure(justify='center')

        self.guess_button = Button(master, text="Start - Romaji", command=self.guess_kanji)
        self.image_Label = Label(master)
        self.next_button = Button(master, text="Next", command=self.reset, state=DISABLED)

        self.label.grid(row=0, column=0, padx=5, pady=5, columnspan=3, sticky=W+E)
        self.entry.grid(row=1, column=0, padx=5, pady=5, columnspan=3, sticky=W+E)
        self.guess_button.grid(row=2, column=0, padx=5, pady=5)
        self.image_Label.grid(row=2, column=1, padx=10, pady=5)
        self.next_button.grid(row=2, column=2, padx=5, pady=5)
        self.status_Label.grid(row=3, columnspan=3, padx=5, pady=5,sticky=W+E)

        self.entry.focus()
        self.setImage(self.randomrow)
    
    def return_Event(self, event=None):
        if self.guess_button['state'] == 'normal':
            self.guess_kanji()
        else:
            self.reset()
            self.setImage(self.randomrow)


    def read_csv_kanji(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(dir_path, 'player.csv')
        if not os.path.exists(filepath):
            filepath = os.path.join(dir_path, 'allkanji.csv')
        
        mydict = csv.DictReader(open(filepath, encoding="utf-8"))
        self.mydict = []
        for row in mydict:
            self.mydict.append(row)


    def pick_Random_Kanji(self):
        while True:
            self.randomrow = random.randint(0, len(self.mydict)-1)

            if self.previous_kanji:
                if self.previous_kanji == self.mydict[self.randomrow]['japanese']:
                    continue

            # If empty row try again 
            if not self.mydict[self.randomrow]['pronounciation']:
                continue

            # If Kanji Review Card is TRUE then randomly display based off EXP 
            if self.mydict[self.randomrow]['reviewcard'] == 'TRUE':
                tryagain = [True]
                tryagain.extend([False] * int(self.mydict[self.randomrow]['EXP']))
                if random.choice(tryagain) is not True:
                    continue

            # Check if kanji is at or below current Level and Stage
            if int(self.mydict[self.randomrow]['level']) <= self.level:
                if int(self.mydict[self.randomrow]['stage']) <= self.stage:
                    break

        self.message = self.mydict[self.randomrow]['japanese'] 
        self.current_kanji = self.message
        self.previous_kanji = self.current_kanji  
        self.label_text.set(self.message)
        self.setImage(self.randomrow)
        
    def guess_kanji(self):
        if self.guess_button['text'] == 'Start - Romaji':
            self.guess_button.configure(text='Submit')
            self.pick_Random_Kanji()
            return

        pronounciation = self.mydict[self.randomrow]['pronounciation']
        translation = self.mydict[self.randomrow]['translation']
        self.guess = self.entry.get().strip()

        if not self.guess:
            return
        elif self.guess == pronounciation:
            self.message = "Correct!\n\n{}: {}\n\nTranslation: {}".format(
                self.message, pronounciation, translation)
            self.exp_up()
        else:
            self.message = "Incorrect\n\n{}: {}\n\nTranslation: {}".format(
                self.message, pronounciation, translation)

        self.label_text.set(self.message)
        self.guess_button.configure(state=DISABLED)
        self.next_button.configure(state=NORMAL)
        self.master.eval('tk::PlaceWindow . center')
        self.entry.focus()

        if self.guess == pronounciation:
            self.caughtImg()

    def reset(self):
        self.entry.delete(0, END)
        self.guess = ''

        self.pick_Random_Kanji()
        self.update_status()

        self.guess_button.configure(state=NORMAL)
        self.next_button.configure(state=DISABLED)
        self.status_Label.configure(bg='grey')
        self.master.eval('tk::PlaceWindow . center')
        self.entry.focus()

    def exp_up(self):
        self.total_exp += 1
        self.kanji_exp += 1

        self.set_kanji_exp()
        self.level_up_check()
        self.update_status()

    def level_up_check(self):
        reviewcard_count = self.reviewcard_handicap
        
        # Count review cards
        for row in self.mydict:
            if row['reviewcard'] == 'TRUE':
                reviewcard_count += 1
                self.kanji_cards = reviewcard_count - self.reviewcard_handicap
            
        try:
            # Turn label background color if stage increased
            if self.mydict[reviewcard_count]['stage'] != str(self.stage):
                self.status_Label.configure(bg='OrangeRed2')
                self.master.eval('tk::PlaceWindow . center')
        
            # Update stage or level 
            self.stage = int(self.mydict[reviewcard_count]['stage'])
            self.level = int(self.mydict[reviewcard_count]['level'])

        except ValueError:
            pass
            
    def set_kanji_exp(self):
        self.mydict[self.randomrow]['EXP'] = str(self.kanji_exp)
        if self.kanji_exp > 0:
            self.mydict[self.randomrow]['reviewcard'] = 'TRUE'

    def update_status(self):
        self.get_kanji_exp()
        self.status_message = "Level: {}\tStage: {}\tThis Kanji Exp: {}\tUnique Kanji Caught: {}".format(
            self.level, self.stage, self.kanji_exp, self.kanji_cards)
        self.status_label_text.set(self.status_message)

    def get_kanji_exp(self):
        if self.mydict[self.randomrow]['EXP'] == 'FALSE':
            self.mydict[self.randomrow]['EXP'] = '0'
        
        self.kanji_exp = int(self.mydict[self.randomrow]['EXP'])

    def on_close(self):
        ''' When closing the window, write the progress to a file'''
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(dir_path, 'player.csv')
        with codecs.open(filepath, 'w', 'utf-8') as csv_file: 
            writer = csv.DictWriter(csv_file, fieldnames=self.mydict[0].keys())
            writer.writeheader()
            for row in self.mydict:
                writer.writerow(row)
        
        self.master.destroy()

    def open_url(self):
        if self.current_kanji:
            url = \
            'https://www.tanoshiijapanese.com/dictionary/kanji_details.cfm?character_id=25173&k={}'.format(
                parse.quote(self.current_kanji, encoding='utf-8')
            )
            webbrowser.open_new_tab(url)

    def loadPokemonImages(self):
        '''Loads each sprite into object that defines upper-left, lower-right'''
        for spriteSheet in self.SPRITE_SHEETS:
            rez = spriteSheet[1]
            row = spriteSheet[2]
            col = spriteSheet[3]

            for i in range(row):
                y = i
                yd = i + 1
                for j in range(col):
                    x = j
                    xd = j + 1
                
                    crop_rectangle = (rez*x, rez*y, rez*xd, rez*yd)
                    self.sprites.append({spriteSheet[0]:crop_rectangle})

    def setImage(self, num):
        '''Crops and resizes sprite to 128x128. Then sets it to label bg'''
        try:
            file_name = list(self.sprites[num].keys())[0]
            # Do not re-read the file if previously opened 
            if file_name != self.file_name:
                self.img = Image.open(file_name).convert("RGBA")
            self.file_name = file_name

            self.cropped_im = self.img.crop(self.sprites[num][self.file_name])
            self.cropped_im.save('sprites/temp.png', 'png')

            img = Image.open("sprites/temp.png").convert("RGBA")
            img = img.resize((128,128), Image.ANTIALIAS)

            self.image = ImageTk.PhotoImage(img)
            self.image_Label['image'] = self.image  
        except Exception:
            print(Exception)

    def caughtImg(self):
        try:
            # Needs to be read each time because the last size will be not work
            if self.kanji_exp == 1: 
                caughtImg = Image.open("sprites/new_catch.png").convert("RGBA")
            else:
                caughtImg = Image.open("sprites/Mobile - Pokemon GO - Poke Balls.png").convert("RGBA")
                randBall = random.choice(self.POKEBALLS)
                crop_rectangle = (256*randBall, 0, 256*(randBall+1), 256)
                caughtImg = caughtImg.crop(crop_rectangle)

            # Opens the current sprite that's displayed and resizes
            tempImg = Image.open("sprites/temp.png").convert("RGBA")
            tempImg = tempImg.resize((128,128), Image.ANTIALIAS)

            # Range needs to be slightly larger than rez, otherwise image will not overlap
            for i in range(1,130,16):
                self.imgResized = caughtImg.resize((i,i), Image.ANTIALIAS)
                # Start in the center then expand 
                tempImg.paste(self.imgResized, (64-i//2, 64-i//2))
                self.image = ImageTk.PhotoImage(tempImg)
                self.image_Label['image'] = self.image 
                self.master.update()
            
        except Exception:
            print(Exception)

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()