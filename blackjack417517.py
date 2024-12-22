# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:50:04 2023

@author: David Parr
"""

import random

deck_list = ['Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds']

def count_cards(cards):
    '''Function Determines what the cards add up to'''
    count = 0
    for i in range(len(cards)):
        if '2' in cards[i]:
            count += 2
        elif '3' in cards[i]:
            count += 3
        elif '4' in cards[i]:
            count += 4
        elif '5' in cards[i]:
            count += 5
        elif '6' in cards[i]:
            count += 6
        elif '7' in cards[i]:
            count += 7
        elif '8' in cards[i]:
            count += 8
        elif '9' in cards[i]:
            count += 9
        elif '10' in cards[i] or 'Jack' in cards[i] or 'Queen' in cards[i] or 'King' in cards[i]:
            count += 10
        elif 'Ace' in cards[i]:
            if count <= 10:
                count += 11
            elif count > 10:
                count += 1
    return count




chip = 100
chip2 = 100

players = int(input('1 or 2 players? '))

while chip > 0: #loop only ends when the user runs out of chips
    
    if chip != 0:
        print(f'Player 1 chips: {chip}')
        Playing_Chips = int(input('Player 1: How many chips will you bet? '))
        chip -= Playing_Chips
    if players == 2 and chip2 != 0:
        print(f'Player 2 chips: {chip2}')
        Playing_Chips2 = int(input('Player 2: How many chips will you bet? '))
        chip2 -= Playing_Chips2
    
    #shuffles the list of cards
    print('Shuffling Cards...\n')
    random.shuffle(deck_list)
    
    #deals cards
    if chip != 0 or Playing_Chips != 0:
        user_cards = deck_list[:2]
        print(f'Player 1\'s cards are cards are {user_cards[0]} and {user_cards[1]}')
    dealer_cards = deck_list[2:4]
    if players == 2 and (chip2 != 0 or Playing_Chips2 != 0):
        user_2cards = deck_list[4:6]
        if players == 2:
            print(f'Player 2\'s cards are {user_2cards[0]} and {user_2cards[1]}')
    
    
    print(f'The dealer\'s first card is {dealer_cards[0]}\n')
    
    
    
    
    print('\n Player 1\'s Turn!\n')
    
    i = 6
    
    #loop of the players turn
    #Player 1
    n = 0
    if chip != 0 or Playing_Chips != 0:
        while True:
            
            #determine if the user has black jack
            if count_cards(user_cards) == 21 and n == 0:
                print('Black Jack!')
                chip += Playing_Chips + int(Playing_Chips * 1.5)
                print(f'You have {chip} chips\n')
                break
            n += 1
            command = input('What would you like to do?(Hit, Stand, Surrender): ')
            
            if command == 'Hit': #will deal the player another card
                user_cards.append(deck_list[i])
                print(f'\nYour new card is: {deck_list[i]}\n')
                i += 1
                if count_cards(user_cards) > 21:
                    print('You Lose!\n') 
                    break
                elif count_cards(user_cards) <= 21:
                    continue
                #loop only contiues if the users cards are under 21
            elif command == 'Stand':
                break
            elif command == 'Surrender':
                print('You Lose!\n')
                chip += int(0.5 * Playing_Chips)
                break
        
    m = 0   
    if players == 2 and (chip2 != 0 or Playing_Chips2 != 0):
            print('\n Player 2\'s Turn!\n')
        
        
            #loop of the players turn
            #Player 2
            while True:
                #determine if the user has black jack
                if count_cards(user_2cards) == 21 and m == 0:
                    print('Black Jack!')
                    chip2 += Playing_Chips2 + int(Playing_Chips2 * 1.5)
                    print(f'You have {chip2} chips\n')
                    break
                m += 1
                command = input('What would you like to do?(Hit, Stand, Surrender): ')
                
                if command == 'Hit': #will deal the player another card
                    user_2cards.append(deck_list[i])
                    print(f'\nYour new card is: {deck_list[i]}\n')
                    i += 1
                    if count_cards(user_2cards) > 21:
                        print('You Lose!\n') 
                        break
                    elif count_cards(user_2cards) <= 21:
                        continue
                    #loop only contiues if the users cards are under 21
                elif command == 'Stand':
                    break
                elif command == 'Surrender':
                    print('You Lose!\n')
                    chip2 += int(0.5 * Playing_Chips2)
                    break
    
      
        
    if count_cards(user_cards) < 21 or count_cards(user_2cards) < 21: #dealers turn
        print('\n Dealer\'s Turn!')
        print(f'The Dealer\'s second card is: {dealer_cards[1]}')
        while True:
            if count_cards(dealer_cards) > 21:
                print('Win!\n')
                chip += (2 * Playing_Chips)
                chip2 += (2 * Playing_Chips2)
                break
            elif count_cards(dealer_cards) < 17:
                i += 1
                dealer_cards.append(deck_list[i])
                print(f'Dealer\'s new card is {dealer_cards[-1]}.')
            elif count_cards(dealer_cards) > 17:
                break
        
        #if else statements only needed if neither players or the dealer busts
    if count_cards(user_cards) <= 21 and count_cards(dealer_cards) <= 21 and (chip != 0 or Playing_Chips != 0):
        if count_cards(user_cards) > count_cards(dealer_cards):
            print('\nPlayer 1 wins!\n')
            chip += 2 * Playing_Chips
        elif count_cards(user_cards) < count_cards(dealer_cards) and count_cards(dealer_cards) <= 21:
            print('\nPlayer 1 Loses!\n')
        elif count_cards(user_cards) == count_cards(dealer_cards):
            print('\nPlayer 1 Pushed!\n')
            chip += Playing_Chips
            
    if count_cards(user_2cards) <= 21 and count_cards(dealer_cards) <= 21 and (chip2 != 0 or Playing_Chips2 != 0):
        if count_cards(user_2cards) > count_cards(dealer_cards):
            print('\nPlayer 2 wins!\n')
            chip2 += 2 * Playing_Chips2
        elif count_cards(user_2cards) < count_cards(dealer_cards) and count_cards(dealer_cards) <= 21:
            print('\nPlayer 2 Loses!\n')
        elif count_cards(user_2cards) == count_cards(dealer_cards):
            print('\nPlayer 2 Pushed!\n')
            chip2 += Playing_Chips2
    
    if chip == 0:
        print('Player 1 is out of chips!\n')
    elif chip2 == 0:
        print('Player 2 is out of chips!\n')
        

    
print('You\'ve both ran out of chips!')
