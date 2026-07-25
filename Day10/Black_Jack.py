#Hint-1: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
from art import logo


def compare(u_score,c_score):

    if u_score==c_score:
        return "Draw :]"
    elif c_score==0 :
        return "Lose,Opponent has BlackJack :["
    elif u_score==0:
        return "Win with a BlackJack :]"
    elif u_score>21:
        return "You went over.You lose :["
    elif c_score>21:
        return "Opponet went over.You win :]"
    elif u_score>c_score:
        return "YOU WIN !!!"
    else:
        return "YOU LOSE !!!"
    
     


def deal_card():
    import random 
    card_list=[11,2,3,4,5,6,7,8,9,10,10,10,10]

    random_card=random.choice(card_list)

    return random_card
  
#Hint-3:Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(card_list):

    card_sum=sum(card_list)
    #Hint-4: Inside calculate_score() check for a blackjack#
    # (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. #
    # 0 will represent a blackjack in our game.

    if sum(card_list)==21 and len(card_list)==2:
        return 0 # BlackJack !!!
    
    #Inside calculate_score() check for an 11 (ace).#
    # If the score is already over 21, remove the 11 and replace it with a 1.
    # You might need to look up append() and remove().
    elif (card_sum>21):
    
        if 11 in card_list :
            card_list.remove(11)
            card_list.append(1)
            card_sum=card_sum(card_list)

        return card_sum

    return card_sum



#Hint-2:Deal the user and computer 2 cards each using deal_card() and append().
def play_game():
    
    print(logo)
    end_game=False
    user_cards = []
    computer_cards = []
    computer_score=-1
    user_score=-1

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())  

    #Hint 6: If the game has not ended, ask the user if they want to draw another card. 
    # If yes, then use the deal_card() function to add another card to the user_cards List. 
    # If no, then the game has ended.


    while end_game==False:

    #Hint-5:Call calculate_score().
    # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your cards:{user_cards},Current score:{user_score}")
        print(f"Computer's first card :{computer_cards[0]}")
        
        if user_score==0 or computer_score==0 or user_score>21:
            end_game=True
            
        else:
            response=input("Would you like to draw again ? : Y -> (draw) / N-> (pass) ")

            if response.upper()=='Y':
                user_cards.append(deal_card())
            else:
                end_game=True

    while computer_score!=0 and computer_score<17 :
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand : {user_cards}, final score : {user_score}")
    print(f"Computers final hand : {computer_cards}, final score : {computer_score}")
    print(compare(user_score,computer_score))


while input("Do you want to play a game of BlackJack? Type 'Y' or 'N' : " )=="Y":
    play_game()
    print("\n"*20)



#CODE COMPUTERS TURN,CREATE COMPARE FUNCTION 

