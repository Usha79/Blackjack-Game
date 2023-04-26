# Blackjack-Game
Project Summary - Python program to play Blackjack game between player and computer(dealer). It includes code using few libraries, functions ,lists, loops and conditions
Requirements/Libraries:
IDLE (or any other IDE)
Colorama library (install using pip)

Description:

The project uses python code to play several rounds of Blackjack against the computer until the user chooses to quit. The goal of blackjack is to beat the dealer's hand without going over 21.Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand. Please refer to the following link to understand the game of [Blackjack](youtube.com/watch?v=qd5oc9hLrXg) . To simplify, I have chosen to do the following:

1. Single player vs Computer
2. A's value is only considered as "1" 
3. The user has only the option to "Hit" or "Stand" (no split option)
4. No betting in the game 

There are three functions in the file: deal_card(), display_cards(), and play_blackjack. The play_blackjack() functions runs once per round and calls the other two functions multiple times. The deal_card() function will generate a new random card with a value and symbol. The display_cards() function displays all cards to the user on terminal. After a round of blackjack, the user is asked if they want to play again. If they choose to play, play_blackjack() is called again. This continues until the user chooses to quit.

An example round of the game is attached as a file for convenience.
