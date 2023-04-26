from colorama.ansi import Style
import random
import colorama
from colorama import Fore

def deal_card(c, v):
    n = random.randint(1, 13) # Get a random number between 1 and 13 inclusive
    if n==11:
        c.append('J')
        v.append(10)
    elif n == 12:
        c.append('Q')
        v.append(10)
    elif n ==13:
        c.append('K')
        v.append(10)
    elif n == 1:
        c.append('A')
        v.append(1)
    else:
        c.append(str(n))
        v.append(n)
    return c, v


def display_cards(p,d):  #displaying dealer and player cards
    print('\n\n\n')
    print(Style.BRIGHT+Fore.GREEN +'DEALER:')
    for i in d:
        print(Fore.LIGHTRED_EX+ i, end = '    ')
    print(Style.BRIGHT+Fore.MAGENTA +'\nPLAYER:')
    for j in p:
        print(Fore.LIGHTRED_EX+ j, end = '    ')
  
    print('\n\n\n')

def play_blackjack(): # deals cards and displays the sum of dealer and player cards
    dealer_cards, dealer_values, player_cards, player_values = [], [], [], []
    
    dealer_cards, dealer_values = deal_card(dealer_cards, dealer_values)
    
    
    player_cards, player_values = deal_card(player_cards, player_values)
    player_cards, player_values = deal_card(player_cards, player_values)

    display_cards(player_cards, dealer_cards)
    print("Player Sum is: ", sum(player_values))
    print("Dealer Sum is: ", sum(dealer_values))
    
    while sum(player_values)<=21:
      player_decision = input('\nType h for Hit or s for Stand: ')
      if player_decision == 'h':
         player_cards, player_values = deal_card(player_cards, player_values)
         display_cards(player_cards, dealer_cards)
         print("Player Sum is: ", sum(player_values))
         print("Dealer Sum is: ", sum(dealer_values))
      
      else:
          break

    if player_decision == 'h':
        print(Fore.LIGHTGREEN_EX +'\nBust! You went over 21. Game over!')
    else:
        print(Fore.BLUE+'\nNow dealer will deal for himself')
        while sum(dealer_values) <17:
            dealer_cards, dealer_values = deal_card(dealer_cards, dealer_values)
            display_cards(player_cards, dealer_cards)
            print("Player Sum is: ", sum(player_values))
            print("Dealer Sum is: ", sum(dealer_values))


        if sum(dealer_values)>21:
            print(Fore.LIGHTGREEN_EX+ '\nThe dealer went bust! You win! Congrats!')
        elif sum(dealer_values)>sum(player_values):
            print(Fore.LIGHTGREEN_EX+'\nYou loose! Better luck next time!')#
        elif sum(dealer_values)== sum(player_values):
            print(Fore.LIGHTGREEN_EX+ '\nIt\'s a draw! You want to test your luck?')
        else:
            print(Fore.LIGHTGREEN_EX +"\nCONGRATULATIONS!!!!YAY YOU WIN!")
           
        
  
    
print(Style.BRIGHT+Fore.BLUE+ '\n\n\n\n Hello, Welcome to Blackjack Game! Let\'s play!')
play_blackjack()
ui = input('\nDo you want to play again? Type y or n: ')
while ui == 'y':
    play_blackjack()
    ui = input('\nDo you want to play again? Type y or n: ')
print(Fore.BLUE+ '\nThanks for playing!')
