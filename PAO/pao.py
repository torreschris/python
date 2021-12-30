__author__ = 'torreschris'

from enum import Enum
import tkinter as tk 
import csv

class PAO_Enum(Enum):
    NUMBER = 0
    TRANSLATION = 1
    PERSON = 2
    ACTION = 3
    OBJECT = 4

class PAO:
    def __init__(self):
        self.pao = {}
        self.init_pao_list()
    
    def init_pao_list(self):
        #file_path = tk.filedialog.askopenfilename()
        file_path = r'PAO/pao_list.csv'
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.pao[row['NUMBER']] = {
                    PAO_Enum.TRANSLATION:row['TRANSLATION'],
                    PAO_Enum.PERSON:row['PERSON'],
                    PAO_Enum.ACTION:row['ACTION'],
                    PAO_Enum.OBJECT:row['OBJECT']
                    }              

def main():
    #textboxNumber = tk.text()

    pao = PAO()
    test = '00'
    print(test)
    print(pao.pao[test][PAO_Enum.TRANSLATION])
    print(pao.pao[test][PAO_Enum.PERSON]) 
    print(pao.pao[test][PAO_Enum.ACTION]) 
    print(pao.pao[test][PAO_Enum.OBJECT]) 

if __name__ == "__main__":
    main()
