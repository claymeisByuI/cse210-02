import random

from hilo.game.card import Card


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
        self.Deck = []
        for suit in suits:
            for number in range(cards_per_suit):
                if number == 0:
                    self.Deck.append(Card(number, "Ace", suit))
                elif number == 11:
                    self.Deck.append(Card(number, "Jack", suit))
                elif number == 12:
                    self.Deck.append(Card(number, "Queen", suit))
                elif number == 13:
                    self.Deck.append(Card(number, "King", suit))
                else:
                    self.Deck.append(Card(number, number, suit))
        

