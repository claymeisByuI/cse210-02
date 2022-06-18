import random

from game.card import Card


class Deck:
    """A list of cards.

    The responsibility of a Deck is to track all cards, and provide details of active Card.
   
    Attributes:
        cards_per_suit (int): The number of cards.
        suits (List[string]): The list of suits.
    """
    def __init__(self, cards_per_suit, suits):
        """Constructs a new instance of Deck with a list of cards 

        Args:
            self (Card, cards_per_suit, suits): An instance of Card.
        """
        self.Discarded_cards = []
        self.Deck = []
        for suit in suits:
            for number in range(1,cards_per_suit+1):
                if number == 0:
                    self.Deck.append(Card(number, "A", suit))
                elif number == 11:
                    self.Deck.append(Card(number, "J", suit))
                elif number == 12:
                    self.Deck.append(Card(number, "Q", suit))
                elif number == 13:
                    self.Deck.append(Card(number, "K", suit))
                else:
                    self.Deck.append(Card(number, number, suit))
        self.shuffle()
        self.active_card = None
        
    def shuffle(self):
        """Shuffles the deck.
        
        Args:
            self (Deck): An instance of Deck.
            """
        random.shuffle(self.Deck)
    
    def remaining_cards(self):
        """Returns the number of cards remaining in the deck.
        
        Args:
            self (Deck): An instance of Deck.
            """
        return len(self.Deck)

    def deal_card(self):
        """Deals a card from the deck.
        
        Args:
            self (Deck): An instance of Deck.
            """
        self.active_card = self.Deck.pop()
        self.Discarded_cards.append(self.active_card)
        return self.active_card
    
        

