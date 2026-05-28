import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]
    suit_order = {"Hearts":1,"Diamonds":2, "Clubs":3, "Spades":4}

    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for rank in self.RANKS:
            for suit in self.SUITS:
                print(suit)
                combo = (rank,suit)
                
                self.__cards.append(combo)
                self.__cards.sort(key=lambda x: self.suit_order[x[1]])
        print(self.__cards)
                

    def shuffle_deck(self):
         random.shuffle(self.__cards)

    def deal_card(self):
        if self.__cards > 0:
            return self.__cards.pop()
        else: 
            return None

        
        


    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"


Test = DeckOfCards()
print(Test)