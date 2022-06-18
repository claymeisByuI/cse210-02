import random


# TODO: Implement the Card  class as follows...

class Card:
    """A single card with a number, value (Ace to King) and a suit.

    The responsibility of a Card is to keep track of the value, number, and suit.
   
    Attributes:
        number (int): The number of the card.
        value (string): The value or face of the card.
        suit (string): The suit of the card.
    """
    def __init__(self, number, value, suit):
        """Constructs a new instance of Card with a value and points attribute.

        Args:
            self (Card, number, value, suit): An instance of Card.
        """
        self.number = number
        self.value = value
        self.suit = suit

