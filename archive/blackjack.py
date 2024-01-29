import numpy as np
import random as random
import time
from playsound import playsound
from PIL import Image
from matplotlib import pyplot
from matplotlib import image
from sys import exit

def blackjack(number_of_games):
    chips = 20
    for i in range(number_of_games):
        number = ["Ace", "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2]
        numbers = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2] * 4
        suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        chips = chips
        deck = []
        new_deck = []
        bust = False
        for i in range(len(suit)):  # generating the deck
            for j in range(len(number)):
                card = str(number[j]) + ' ' + 'of' + ' ' + str(suit[i])
                deck.append(card)
                new_deck.append(card)
        x = input("Type ready to start :)  ")  # ready confirmation
        if x != "ready":
            return "You lose :("
        else:
            print("Great!", "\n")
            time.sleep(1)
            print("You have",chips,"chips")
            time.sleep(1)
            print("How many chips would you like to bet?")
            bet = int(input())  # bet amount
        if bet < 1 or bet > chips:
            print("lol")
        else:  # initial phase
            time.sleep(1)
            print("Bets are in!")
            time.sleep(1)
            print("The dealer will now deal")
            player_card = []
            player_value = []
            dealer_card = []
            dealer_value = []
            dealer_unknown = []
            dealer_unknownv = []
            size = len(new_deck)
            r = random.randint(0, size)
            player_card.append(new_deck[r])
            player_value.append(numbers[r])
            new_deck.pop(r)
            numbers.pop(r)
            size = len(new_deck)
            r = random.randint(0, size)
            dealer_card.append(new_deck[r])
            dealer_value.append(numbers[r])
            dealer_unknown.append(new_deck[r])
            dealer_unknownv.append(numbers[r])
            new_deck.pop(r)
            numbers.pop(r)
            size = len(new_deck)
            r = random.randint(0, size)
            player_card.append(new_deck[r])
            player_value.append(numbers[r])
            new_deck.pop(r)
            numbers.pop(r)
            size = len(new_deck)
            r = random.randint(0, size)
            dealer_card.append("?")
            dealer_value.append("?")
            dealer_unknown.append(new_deck[r])
            dealer_unknownv.append(numbers[r])
            new_deck.pop(r)
            numbers.pop(r)
            size = len(new_deck)

            print("The dealers cards are ", dealer_card)

            for i in range(10):  # dealing phase
                if sum(player_value) > 21:
                    for i in range(len(player_value)):  # makes ace 1 or 11
                        if player_value[i] == 11:
                            player_value[i] -= 10
                        break
                time.sleep(1)
                print("Your cards are ", player_card)
                time.sleep(1)
                print("You have", sum(player_value), "\n")
                if len(player_value) == 2 and sum(player_value) == 21:
                    chips += bet * 2
                    print("Congrats!")
                    time.sleep(1)
                    playsound('21.mp3')
                    print("You got a black jack")
                    print("You now have ", chips, "chips")
                    bust = True
                    break
                if sum(player_value) > 21:
                    print("Aww you bust :( ")
                    time.sleep(1)
                    print("The dealer wins!")
                    chips -= bet
                    print("You now have ", chips, "chips")
                    bust = True
                    break
                elif sum(player_value) == 21:
                    print("Wow you got a 21!")
                    playsound('21.mp3')
                    break
                else:
                    hit = str(input("Hit or stick?"))
                if hit == "stick":
                    break
                elif hit == "hit":
                    size = len(new_deck)
                    r = random.randint(0, size)
                    player_card.append(new_deck[r])
                    player_value.append(numbers[r])
                    new_deck.pop(r)
                    numbers.pop(r)

            if bust == True:
                break
            else:
                for i in range(6):
                    if sum(dealer_unknownv) < 17:
                        size = len(new_deck)
                        r = random.randint(0, size)
                        dealer_unknown.append(new_deck[r])
                        dealer_unknownv.append(numbers[r])
                        new_deck.pop(r)
                        numbers.pop(r)
                        print("The dealers cards are", dealer_unknown)
                        time.sleep(1)
                        print("The dealer has", sum(dealer_unknownv))
                if sum(dealer_unknownv) > 21:
                    print("The dealer busts!")
                    time.sleep(1)
                    print("You win!!")
                    chips += bet
                    time.sleep(1)
                    print("You now have ", chips, "chips")
                else:
                    if sum(player_value) > sum(dealer_unknownv):
                        print("You win!!")
                        chips += bet
                        time.sleep(1)
                        print("You now have ", chips, "chips")
                    elif sum(player_value) == sum(dealer_unknownv):
                        print("Its a draw")
                        time.sleep(1)
                        print("You now have ", chips, "chips")
                        chips = chips
                    elif sum(player_value) < sum(dealer_unknownv):
                        print("Aww you lose :(")
                        chips -= bet
                        time.sleep(1)
                        print("You now have ", chips, "chips")

blackjack(2)