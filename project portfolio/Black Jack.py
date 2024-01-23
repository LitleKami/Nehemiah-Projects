import random
## our black jack rules ###
# The deck is unlimited in size.
#There are no jokers.
#The Jack\Queen|King all count as 10.
#The ace can count as 11 or 1.
#use the following list as the deck of cards:

# The cards in the list have equal probability of been drawn.
#Cards are not removed from the deck as they are drawn.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card():
    fickle = random.choice(cards)
    return fickle
def score(total):
    g = sum(total)
    return g
def evaluation(player_score, computer_score):
    if player_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack "
    elif computer_score > 21:
        return "You win, opponent went over"
    elif player_score == 0:
        return "You win with Blackjack."
    elif player_score > 21:
        return "You went over, you lose."
    elif player_score > computer_score:
        return "You scored higher, you win!!"
    else:
        print("You lose") 
def play_game():
    your_cards = []
    computer_cards = []
    for _ in range(2): 
        your_cards.append(card())
        computer_cards.append(card())
    stop_game = False
    while stop_game == False:
        player_score = score(your_cards)
        computer_score = score(computer_cards)
        c_first_card = computer_cards[0]
        print(f"Your cards: {your_cards}, current score: {player_score}")
        print(f"Computers first card: {c_first_card}")
        if 11 in your_cards and player_score > 21:
            your_cards.remove(11)
            your_cards.append(1)
        draw_again = True
        while draw_again == True and player_score < 21:
            another_card = (input("Type 'y' to get another card, type 'n' to pass: ")).lower()
            if another_card == 'y':
                your_cards.append(card())
                player_score = score(your_cards)
                if computer_score < 17:
                    computer_cards.append(card())
                    computer_score = score(computer_cards)
                if player_score > 21:
                    evaluation(player_score, computer_score)
                print(f"Your cards: {your_cards}, current score: {player_score}")
                print(f"Computers first card: {c_first_card}")
            else:
                draw_again = False
        print(f"  Your final hand: {your_cards}, final score: {player_score}")
        print(f"  computers final hand: {computer_cards}, final score: {computer_score}")
        print(evaluation(player_score, computer_score))
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower() == 'y':
            print("****************************************")
            play_game()
        else:
            stop_game = True
play_game()