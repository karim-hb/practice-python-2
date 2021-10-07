import random 
def play():
    user = input("what is your  choice 'r' for rock and 'p' for paper and 's' for scissors : ")
    user = user.lower()
    computer = random.choice(['r','p','s'])

    if user == computer :
        return (0,user,computer)
    elif is_win(user,computer):
        return (1,user,computer)
    else :
        return (2,user,computer) 

def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    return False

def game():
    user_win = 0
    computer_win = 0
    while user_win + computer_win != 5 :
        result, user, computer = play()
        if result == 0:
            print('You and the computer have both chosen {}. \n'.format(user))
        elif result == 1:
            user_win += 1
            print('You chose {} and the computer chose {}. You won   :)   ! \n'.format(user, computer))
        else:
            computer_win += 1
            print('You chose {} and the computer chose {}. You lost  :(\n'.format(user, computer))

    if user_win > computer_win:
        print('You have won ! , your score is {} and copmuter score is {}'.format(user_win,computer_win))
    else:
        print('Unfortunately, the computer has won , your score is {} and copmuter score is {}'.format(user_win,computer_win))

game()