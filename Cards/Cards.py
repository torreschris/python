__author__ = 'torreschris'

import random

class Cards: 
    def __init__(self):
        self.deck_ref = {
            'A♥':'18', '2♥':'28', '3♥':'38', '4♥':'48',
            '5♥':'58', '6♥':'68', '7♥':'78', '8♥':'88',
            '9♥':'98', '10♥':'08', 'J♥':'', 'Q♥':'', 'K♥':'',
            'A♦':'14', '2♦':'24', '3♦':'34', '4♦':'44',
            '5♦':'54', '6♦':'64', '7♦':'74', '8♦':'84',
            '9♦':'94', '10♦':'04', 'J♦':'', 'Q♦':'', 'K♦':'',
            'A♧':'13', '2♧':'23', '3♧':'33', '4♧':'43',
            '5♧':'53', '6♧':'63', '7♧':'73', '8♧':'83',
            '9♧':'93', '10♧':'03', 'J♧':'', 'Q♧':'','K♧':'',
            'A♤':'16', '2♤':'26', '3♤':'36', '4♤':'46',
            '5♤':'56', '6♤':'66', '7♤':'76', '8♤':'86',
            '9♤':'96', '10♤':'06', 'J♤':'','Q♤':'','K♤':''    
        }
        self.deck = list(self.deck_ref.keys())

    def shuffle_cards(self):
        shuffled_deck = []

        while len(self.deck) > 0:
            i = random.randint(0,len(self.deck)-1)
            shuffled_deck.append(self.deck[i])
            self.deck.pop(i)

        self.deck = shuffled_deck
        return shuffled_deck

    def sort_deck(self):
        self.deck = list(self.deck_ref.keys())

def main():
    cards = Cards()
    cards.shuffle_cards()
    print(cards.deck)

if __name__ == "__main__":
    main()