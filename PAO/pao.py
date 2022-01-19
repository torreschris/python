__author__ = 'torreschris'

from enum import Enum
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
        with open('pao_list.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.pao[row['NUMBER']] = {
                    PAO_Enum.TRANSLATION:row['TRANSLATION'],
                    PAO_Enum.PERSON:row['PERSON'],
                    PAO_Enum.ACTION:row['ACTION'],
                    PAO_Enum.OBJECT:row['OBJECT']
                    }              

def main():
    pao = PAO()
    x1 = '04'
    x2 = '05'
    x3 = '06'
    x4 = '07'
    
    print(pao.pao[x1][PAO_Enum.TRANSLATION])
    print(pao.pao[x2][PAO_Enum.PERSON]) 
    print(pao.pao[x3][PAO_Enum.ACTION]) 
    print(pao.pao[x4][PAO_Enum.OBJECT]) 

if __name__ == "__main__":
    main()
