from game.deck import Deck
from game.card import Card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.deck = Deck(13, ["♥️", "♦️", "♣️", "♠️"])
        self.is_playing = True
        self.score = 300
        self.previous_card = None
        self.active_card = None
        self.guess_higher = True


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.do_show_card()
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.get_play_again_inputs()
            
    def do_show_card(self):
        """Draws a card and shows it to the user.
            
            Args:
                self (Director): an instance of Director.
        """
        # if first rownd of play, deal a card
        if self.active_card is None:
            self.active_card = self.deck.deal_card()
        print(f"The current card is {self.active_card}")

    def get_inputs(self):
        """Ask the user if think next card is higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        higher_lower = input("Higher or lower? [H/L] ").lower()
        self.guess_higher = (higher_lower == "h")
       

    def get_play_again_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        draw_again = input("Play again? [y/n] ").lower()
        self.is_playing = (draw_again == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        self.previous_card = self.deck.active_card
        self.active_card = self.deck.deal_card()
        if self.guess_higher:
            if self.active_card.number > self.previous_card.number:
                self.score += 100
            else:
                self.score -= 75
        else:
            if self.active_card.number < self.previous_card.number:
                self.score += 100
            else:
                self.score -= 75

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Next card was: {self.active_card}")
        print(f"Your score is: {self.score}\n")
        self.is_playing == (self.score > 0)