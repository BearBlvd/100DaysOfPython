import random
from art import logo
print(logo)

def get_star(data):
    random_selector=random.choice(data)
    name=random_selector['name']
    follower_count=random_selector['follower_count']
    description=random_selector['description']
    counrty=random_selector['country']
    print(f"{name} , {description} ,{counrty}")

    return follower_count

def compare_followers(user_choice,a_followers,b_followers):
    if (a_followers<b_followers and user_choice=='A'):
        return False
    elif(a_followers>b_followers and user_choice=='B'):
        return False

    return True

End_game=False

from game_data import data

while(End_game==False):
    A=get_star(data)

    from art import vs
    print(vs)

    B=get_star(data)
    
    user_choice=input("Who has more followers? Type 'A' or 'B' ")

    if (compare_followers(user_choice,A,B)==False):
        End_game=True





    
    


