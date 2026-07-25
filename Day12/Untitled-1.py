import random
from art import logo
print(logo)

print("Welcome to the number guessing game!")

print("I'm thinking of a number between 1 and 100. ")

diff_level=input("Choose a Difficulty level.Type 'easy' or 'hard'")

random_number=random.randrange(1,100)

if diff_level.lower()=="easy":

    print("You have 10 attempts")
    remainder=10
    for i in range(1,11):
        guess=int(input("Make a guess: "))

        if guess==random_number:
            print("You win!!!")
            break
        elif guess<random_number:
            print("Too Low")
            print("Guess Again")
            remainder-=1
            print(f"You have {remainder} attempts left")
        elif(guess>random_number):
            print("Too High")
            print("Guess Again")
            remainder-=1
            print(f"You have {remainder} attempts left")

elif diff_level.lower()=='hard':
    print("You have 5 attempts")
    remainder=5
    for i in range(1,6):
        guess=int(input("Make a guess: "))

        if guess==random_number:
            print("You win!!!")
            break
        elif guess<random_number:
            print("Too Low")
            print("Guess Again")
            remainder-=1
            print(f"You have {remainder} attempts left")
        elif(guess>random_number):
            print("Too High")
            print("Guess Again")
            remainder-=1
            print(f"You have {remainder} attempts left")
            


            


        

    
