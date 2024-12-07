# black_jack_v1.0
This code implements a Blackjack game where the player competes against a dealer to get as close to 21 as possible without exceeding it.

Basic Setup:

Uses a standard deck of 52 cards with suits (Hearts, Diamonds, etc.) and ranks (Two, Three, etc.).
Card values are predefined, with Ace being flexible (1 or 11).
Gameplay:

Both the player and dealer are dealt two cards at the beginning.
The player's goal is to achieve a hand value as close to 21 as possible without exceeding it.
The player decides to "hit" (draw another card) or "stand" (keep their current hand).
The dealer must keep drawing cards until their hand's value is at least 17.
Winning Conditions:

If the player's hand exceeds 21, they bust and lose the round.
If the dealer busts or the player has a higher value than the dealer without busting, the player wins.
If the dealer's value is higher but does not exceed 21, the dealer wins.
If both have the same value, it's a tie (push).
Betting System:

Players start with 100 chips.
They can place bets at the start of each round.
Winning a round increases their chips by the bet amount; losing a round decreases their chips.
Adjusting for Aces:

If a hand's value exceeds 21 but contains an Ace valued at 11, the Ace's value is adjusted to 1 to prevent busting.
Interaction:

The player is asked to:
Place bets.
Choose actions (hit or stand).
Decide whether to play another round after finishing the current one.
Dealer's Rules:

The dealer’s first card is hidden initially.
The dealer must hit until their hand's value reaches 17 or more.
Game Loop:

The game repeats until the player chooses to quit.
Example Flow:
The player starts with 100 chips and places a bet.
Two cards are dealt to both the player and the dealer (one dealer card is hidden).
The player decides to hit or stand based on their hand's value.
If the player stands, the dealer plays according to the rules (hits until 17 or more).
The winner is determined based on the hand values.
The player's chip total is updated.
The player can decide to play another round or quit.
