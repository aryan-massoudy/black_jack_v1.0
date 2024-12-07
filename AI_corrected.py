import random

# Define suits, ranks, and card values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')  # Card suits
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')  # Card ranks
values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
    'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11  # Ace has flexible value
}
playing = True  # Variable to keep track of whether the game is active

# Card class to represent individual cards
class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # Card suit (e.g., Hearts)
        self.rank = rank  # Card rank (e.g., Ace)

    def __str__(self):
        return self.rank + " of " + self.suit  # String representation of the card

# Deck class to manage a collection of cards
class Deck:
    def __init__(self):
        self.deck = []  # Start with an empty list for cards
        # Create a full deck by combining each suit with each rank
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ''  # Accumulate string representation of all cards
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return f'The deck has: {deck_comp}'

    def shuffle(self):
        random.shuffle(self.deck)  # Shuffle the deck randomly

    def deal(self):
        return self.deck.pop()  # Remove and return the top card

# Hand class to represent a player's hand
class Hand:
    def __init__(self):
        self.cards = []  # Cards currently in the player's hand
        self.value = 0   # Total value of the hand
        self.aces = 0    # Track the number of aces in the hand

    def add_card(self, card):
        self.cards.append(card)  # Add the card to the hand
        self.value += values[card.rank]  # Update the hand's value
        if card.rank == 'Ace':
            self.aces += 1  # Increment ace count if the card is an Ace

    def adjust_for_ace(self):
        # Adjust the value of aces if the hand's value exceeds 21
        while self.value > 21 and self.aces:
            self.value -= 10  # Convert an Ace from 11 to 1
            self.aces -= 1  # Reduce the ace count

# Chips class to manage the player's chips
class Chips:
    def __init__(self):
        self.total = 100  # Start with a default total of 100 chips
        self.bet = 0      # Initialize the bet to 0

    def win_bet(self):
        self.total += self.bet  # Add the bet amount to the total

    def lose_bet(self):
        self.total -= self.bet  # Subtract the bet amount from the total

# Function to take a bet from the player
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed your total chips.")
            else:
                break

# Function to handle a hit action (draw a card)
def hit(deck, hand):
    hand.add_card(deck.deal())  # Add a card to the hand
    hand.adjust_for_ace()      # Adjust for aces if necessary

# Function to decide whether to hit or stand
def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")
        if x[0].lower() == 'h':
            hit(deck, hand)  # Player chooses to hit
        elif x[0].lower() == 's':
            playing = False  # Player chooses to stand
        else:
            print("Sorry, please try again.")
            continue
        break

# Function to show some cards (dealer hides one card)
def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("<card hidden>")  # Hide the first dealer card
    print('', dealer.cards[1])  # Show the second dealer card
    print("\nPlayer's Hand:", *player.cards, sep='\n')

# Function to show all cards (reveal both hands)
def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print("Player's Hand =", player.value)

# Functions for game outcomes
def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player tie! It's a push.")

# Main game loop
while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n'
          'Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Initialize player and dealer hands
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Initialize player's chips
    player_chips = Chips()

    # Take the player's bet
    take_bet(player_chips)

    # Show initial cards
    show_some(player_hand, dealer_hand)

    while playing:  # While the game is ongoing
        hit_or_stand(deck, player_hand)  # Ask player to hit or stand
        show_some(player_hand, dealer_hand)  # Show current hands

        if player_hand.value > 21:  # Check if player busts
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:  # If player hasn't busted
        while dealer_hand.value < 17:  # Dealer hits until value >= 17
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)  # Show final hands

        # Determine the winner
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Show the player's total chips
    print("\nPlayer's winnings stand at", player_chips.total)

    # Ask if the player wants to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n': ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
