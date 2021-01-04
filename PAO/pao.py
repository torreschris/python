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
            # '00': {PAO_Enum.PERSON:'Ozzy Osborne',PAO_Enum.ACTION:'eating a bat',PAO_Enum.OBJECT:'bat'},
            # '01': {PAO_Enum.PERSON:'George Washington',PAO_Enum.ACTION:'sailing a boat',PAO_Enum.OBJECT:'boat'},
            # '02': {PAO_Enum.PERSON:'Obi-Wan Kanobi',PAO_Enum.ACTION:'fighting with lightsabers',PAO_Enum.OBJECT:'lightsaber'},
            # '03': {PAO_Enum.PERSON:'Octopus',PAO_Enum.ACTION:'grabbing fish with tenticals',PAO_Enum.OBJECT:'tenticles'},
            # '04': {PAO_Enum.PERSON:'Odin',PAO_Enum.ACTION:'riding horse with sword',PAO_Enum.OBJECT:'sword'},
            # '05': {PAO_Enum.PERSON:'Odin',PAO_Enum.ACTION:'riding horse',PAO_Enum.OBJECT:''},
            # }
    
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
    test = '04'
    print(test)
    print(pao.pao[test][PAO_Enum.TRANSLATION])
    print(pao.pao[test][PAO_Enum.PERSON]) 
    print(pao.pao[test][PAO_Enum.ACTION]) 
    print(pao.pao[test][PAO_Enum.OBJECT]) 

if __name__ == "__main__":
    main()
