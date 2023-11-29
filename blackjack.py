import random
import time

#LIST, INPUTS, INITIALIZATION
card_deck = ["A♠","A♣","A♦","A♥","2♠","2♣","2♦","2♥","3♠","3♣","3♦","3♥","4♠","4♣","4♦","4♥","5♠","5♣","5♦","5♥","6♠","6♣","6♦","6♥","7♠","7♣","7♦","7♥","8♠","8♣","8♦","8♥","9♠","9♣","9♦","9♥","10♠","10♣","10♦","10♥","J♠","J♣","J♦","J♥","Q♠","Q♣","Q♦","Q♥","K♠","K♣","K♦","K♥"]
player_card = []
dealer_card = []
start_game = input("This is a program for blackjack. Enter 'DEAL' when you are ready to play ")
player_card1 = ""
player_card2 = ""
player_card3 = ""
dealer_card1 = ""
dealer_card2 = ""
dealer_card3 = ""
x = 0
player_card_storage = ""
count = 0
dealer_count = 0
player_count = 0
player_move = 0
dealer_hand_value1 = 0
dealer_hand_value2 = 0
dealer_hand_value3 = 0
hand_value1 = 0
hand_value2 = 0
hand_value3 = 0
dealer_card1_value = 0
dealer_card2_value = 0
player_value = 0
dealer_value = 0
ace_check = 0
card = ""
card_value = 0
player_end_value = 0

#CARD VALUES FUNCTION
def value_function(card):
    if card == card_deck[0] or card == card_deck[1] or card == card_deck[2] or card == card_deck[3]:
        card_value = 11
    elif card == card_deck[4] or card == card_deck[5] or card == card_deck[6] or card == card_deck[7]:
        card_value = 2
    elif card == card_deck[8] or card == card_deck[9] or card == card_deck[10] or card == card_deck[11]:
        card_value = 3
    elif card == card_deck[12] or card == card_deck[13] or card == card_deck[14] or card == card_deck[15]:
        card_value = 4
    elif card == card_deck[16] or card == card_deck[17] or card == card_deck[18] or card == card_deck[19]:
        card_value = 5
    elif card == card_deck[20] or card == card_deck[21] or card == card_deck[22] or card == card_deck[23]:
        card_value = 6
    elif card == card_deck[24] or card == card_deck[25] or card == card_deck[26] or card == card_deck[27]:
        card_value = 7
    elif card == card_deck[28] or card == card_deck[29] or card == card_deck[30] or card == card_deck[31]:
        card_value = 8
    elif card == card_deck[32] or card == card_deck[33] or card == card_deck[34] or card == card_deck[35]:
        card_value = 9
    elif card == card_deck[36] or card == card_deck[37] or card == card_deck[38] or card == card_deck[39] or card == card_deck[40] or card == card_deck[41] or card == card_deck[42] or card == card_deck[43] or card == card_deck[44] or card == card_deck[45] or card == card_deck[46] or card == card_deck[47] or card == card_deck[48] or card == card_deck[49] or card == card_deck[50] or card == card_deck[51]:
        card_value = 10
    return card_value


#DEAL PLAYER CARDS
if start_game.upper() == "DEAL":
    player_card1 = random.choice(card_deck)
    player_card2 = random.choice(card_deck)
    while player_card2 == player_card1:
        player_card2 = random.choice(card_deck)
    player_cards = player_card1 + " " + player_card2
    hand_value1 = value_function(player_card1)
    hand_value3 = value_function(player_card2)
    if hand_value1 == 11 or hand_value3 == 11:
        print("Your hand is: " + player_cards)
    else:
        print("Your hand is: " + player_cards + " (" + str(hand_value1 + hand_value3) + ")")
    if hand_value1 + hand_value3 == 21:
        print("BLACKJACK! YOU WIN!")
        exit()
    player_card.append(hand_value1)
    player_card.append(hand_value3)

#DEALER FIRST CARD
    dealer_card1 = random.choice(card_deck)
    while dealer_card1 == player_card1 or dealer_card1 == player_card2:
        dealer_card1 = random.choice(card_deck)
    print("The dealer's hand is: " + dealer_card1 + " 🂠")

#PLAYER MOVE
    hit_stay = input("HIT or STAY? ")
    if hit_stay.upper().strip() == "HIT":
        player_move = 1
    elif hit_stay.upper().strip() == "STAY":
        player_move = 0
    if player_move == 1:
        player_card3 = random.choice(card_deck)
        while player_card3 == player_card1 or player_card3 == player_card2 or player_card3 == dealer_card1:
            player_card3 = random.choice(card_deck)
        player_cards = player_cards + " " + player_card3
        hand_value2 = value_function(player_card3)
        player_card.append(hand_value2)
        for x in range(len(player_card)):
            count += player_card[x]
        if count > 21:
            for i in range(len(player_card)):
                if player_card[i] == 11:
                    count -= 10
                    print("Your hand is: " + player_cards + " (" + str(count) + ")")
                    if count > 21:
                        print("BUST! YOU LOSE!")
                        exit()
            if count > 21:
                print("Your hand is: " + player_cards + " (" + str(count) + ")")
                print("BUST! YOU LOSE!")
                exit()
        elif count == 21:
            print("Your hand is: " + player_cards + " (" + str(count) + ")")
            print("BLACKJACK! YOU WIN!")
            exit()
        else:
            print("Your hand is: " + player_cards + " (" + str(count) + ")")
        while player_move == 1:
            count = 0
            hit_stay = input("HIT or STAY? ")
            if hit_stay.upper().strip() == "HIT":
                player_move = 1
            elif hit_stay.upper().strip() == "STAY":
                player_move = 0
            if player_move == 1:
                player_card_storage = player_card3
                player_card3 = random.choice(card_deck)
                while player_card3 == player_card_storage or player_card3 == player_card1 or player_card3 == player_card2 or player_card3 == dealer_card1:
                    player_card3 = random.choice(card_deck)
                player_cards = player_cards + " " + player_card3
                hand_value2 = value_function(player_card3)
                player_card.append(hand_value2)
                for x in range(len(player_card)):
                    count += player_card[x]
                if count > 21:
                    for i in range(len(player_card)):
                        if player_card[i] == 11:
                            count -= 10
                            print("Your hand is: " + player_cards + " (" + str(count) + ")")
                            if count > 21:
                                print("BUST! YOU LOSE!")
                                exit()
                    if count > 21:
                        print("Your hand is: " + player_cards + " (" + str(count) + ")")
                        print("BUST! YOU LOSE!")
                        exit()
                elif count == 21:
                    print("Your hand is: " + player_cards + " (" + str(count) + ")")
                    print("BLACKJACK! YOU WIN!")
                    exit()
                elif count < 21:
                    print("Your hand is: " + player_cards + " (" + str(count) + ")")
            elif player_move == 0:
                print("STAY at " + str(count))
    elif player_move == 0:
        count = value_function(player_card1) + value_function(player_card2)
        print("STAY at " + str(count))

#DEALER MOVE
    dealer_card2 = random.choice(card_deck)
    while dealer_card2 == player_card1 or dealer_card2 == player_card2 or dealer_card2 == player_card3 or dealer_card2 == player_card_storage or dealer_card2 == player_card3 or dealer_card2 == dealer_card1:
        dealer_card2 = random.choice(card_deck)
    dealer_hand_value1 = value_function(dealer_card1)
    dealer_hand_value2 = value_function(dealer_card2)
    dealer_card.append(dealer_hand_value1)
    dealer_card.append(dealer_hand_value2)
    count = dealer_hand_value1 + dealer_hand_value2
    dealer_string = dealer_card1 + " " + dealer_card2 + " "
    if count == 21:
        print("The dealer's hand is: " + dealer_string + " (" + str(count) + ")")
        print("BLACKJACK! YOU LOSE!")
        exit()
    elif dealer_hand_value1 == 11 and dealer_hand_value2 == 11:
        print("The dealer's hand is: " + dealer_card1 + " " + dealer_card2 + " (2/12)")
    elif dealer_hand_value1 == 11 or dealer_hand_value2 == 11:
        print("The dealer's hand is: " + dealer_card1 + " " + dealer_card2 + " (" + str(value_function(dealer_card1) + (value_function(dealer_card2) - 10)) + "/" + str(value_function(dealer_card1) + value_function(dealer_card2)) + ")")
    else:
        print("The dealer's hand is: " + dealer_card1 + " " + dealer_card2 + " (" + str(value_function(dealer_card1) + value_function(dealer_card2)) + ")")
    while count < 17:
        time.sleep(1.5)
        print("Dealer HITS")
        time.sleep(1.5)
        dealer_card3 = random.choice(card_deck)
        while dealer_card3 == player_card1 or dealer_card3 == player_card2 or dealer_card3 == player_card3 or dealer_card3 == player_card_storage or dealer_card3 == player_card3 or dealer_card3 == dealer_card1 or dealer_card3 == dealer_card2:
            dealer_card3 = random.choice(card_deck)
        dealer_hand_value3 = value_function(dealer_card3)
        dealer_card.append(dealer_hand_value3)
        count += dealer_hand_value3
        dealer_string = dealer_string + " " + dealer_card3
        if count > 21:
            for i in range(len(dealer_card)):
                if dealer_card[i] == 11:
                    count -= 10
                    print("The dealer's hand is: " + dealer_string + " " + " (" + str(count) + ")")
                    if count > 21:
                        print("BUST! YOU WIN!")
                        exit()
            if count > 21:
                print("The dealer's hand is: " + dealer_string + " (" + str(count) + ")")
                print("BUST! YOU WIN!")
                exit()
        elif count == 21:
            print("The dealer's hand is: " + dealer_string + " (" + str(count) + ")")
            print("BLACKJACK! YOU LOSE!")
            exit()
        else:
            print("The dealer's hand is: " + dealer_string + " (" + str(count) + ")")
    for x in range(len(player_card)):
        player_count += player_card[x]
    for x in range(len(dealer_card)):
        dealer_count += dealer_card[x]
    if dealer_count > player_count:
        print("YOU LOSE!")
    elif dealer_count == player_count:
        print("TIE!")
    else:
        print("YOU WIN!")







