#Rock-Paper-Scissor game
#
import random

#step1: Stating game instructions
print('Rules of Rock-Paper-Scissor:\n Rock v/s Paper -> Paper wins \n Rock v/s Scissor -> Rock wins \n Scissor v/s Paper -> Scissor wins ')

# Step2: Taking user input
user = input('Enter your name: ')

while True:
    player_choice = input('Enter a choice: \n a. Rock \n b. Paper \n c. Scissor \n ').lower()

    # Step3: Checking for invalid input
    while True:
        if player_choice == 'a' or player_choice == 'b' or player_choice ==  'c':
            print('Good luck ' + user) 
            break
        else:
            print('Invalid choice. Please try again')

    

    # Step4: Initializing value of choice_name variable corresponding to the choice value
    if player_choice == 'a':
        player_choice_name = 'Rock'
    elif player_choice == 'b':
        player_choice_name = 'Paper'
    else:
        player_choice_name = 'Scissor'

    #step5: Creating a list of possible choices for computer
    possible_choice = ['Rock', 'Paper', 'Scissor']

    #step6: Computer chooses randomly from the available choices
    Computer_choice = possible_choice[random.randint(0,2)]
    print('Computer chooses ' + Computer_choice)

    ##step7: Game conditions
    if player_choice_name == Computer_choice:
        print(f"Both players selected {Computer_choice}. It's a tie!")
    elif player_choice_name == 'Rock':
        if Computer_choice == 'Scissor':
            print('Rock smashes Scissor. You win!')
        else:
            print('Paper covers Rock. You lose!')
    elif player_choice_name == 'Paper':
        if Computer_choice == 'Rock':
            print('Paper covers Rock. You win!')
        else:
            print('Scissor cuts Paper. You lose!')
    elif player_choice_name == 'Scissor':
        if Computer_choice == 'Paper':
            print('Scissor cuts Paper. You win!')
        else:
            print('Rock smashes Scissor. You lose!')

    #step8: Asking user wish to continue
    Option = input('Do you want to play again? \n 1. Yes \n 2. No \n')
    if Option != 1 or Option != 2:
        print('Invalid choice. Please try again!')
    elif Option == 2:
        break

#step9: Thanking the player after coming out the while loop
print('Thanks for playing ' + user)
