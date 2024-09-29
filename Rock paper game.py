import random

print("Instructions of Game")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
print("If you want to QUIT the game enter quit")

def play_game():
    options=['Rock','Paper','Scissors']
    while True:
        user_choice=input("Enter Your Choice:Rock,Paper or Scissors=")
        if user_choice=='quit':
            print("Thanks For Playing")
            break
        if user_choice not in options:
            print("OH NO! Please enter correct choice")
            continue
        computer_choice=random.choice(options)
        print(f"Your choice:{user_choice}")
        print(f"COMPUTER CHOICE:{computer_choice}")

        if user_choice==computer_choice:
            print("ITS A TIE")
        elif(user_choice=="Rock" and computer_choice=="Scissors") or \
            (user_choice=="Paper" and computer_choice=="Rock") or \
            (user_choice=="Scissors" and computer_choice=="Paper"):
            print("HURRAY!! YOU HAVE WON")
            
        else:
            print("OOPS COMPUTER WON")
            
play_game()




