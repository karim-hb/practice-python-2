import random 
def play():
    user = input("what is your  choice 'o' for On hand and 'b' for back of hand : ")
    user = user.lower()
    computer1 = random.choice(['o','b'])
    computer2 = random.choice(['o','b'])


    if user == computer1 ==  computer2:
        return (0,user,computer1 ,computer2 )
    elif is_win(user,computer1,computer2):
        return (1,user,computer1 ,computer2)
    elif is_win(computer1,user,computer2):
        return (2,user,computer1 ,computer2)
    elif is_win(computer2,computer1,user):
        return (3,user,computer1 ,computer2)
   

def is_win(player1, player2,player3):
    if(player1 == 'b' and player2 =='o' and player3 == 'o') or (player1 == 'o' and player2 == 'b' and player3 == 'b'):
        return True
    else:
        return False
    

def game():
    user_win = 0
    computer_win1 = 0
    computer_win2 = 0
    while user_win + computer_win1 + computer_win2 != 5 :
        result, user, computer1, computer2= play()
        if result == 0:
            print('You and the computers have both chosen {}. \n'.format(user))
        elif result == 1:
            user_win += 1
            print('You chose {} and the computer1 chose {}  and the computer2 chose {} .  You won   :)   ! \n'.format(user, computer1,computer2))
        elif result == 2:
            computer_win1 += 1
            print('You chose {} and the computer1 chose {}  and the computer2 chose {} .  computer1 won   :(   ! \n'.format(user, computer1,computer2))
        else:
            computer_win2 += 1
            print('You chose {} and the computer1 chose {}  and the computer2 chose {} .  computer2 won   :(   ! \n'.format(user, computer1,computer2))

    if user_win > computer_win1 and user_win > computer_win2:
        print('You have won ! , your score is {} and computer1 score is {} and the computer2 score is {}'.format(user_win,computer_win1,computer_win2))
    elif computer_win1 > user_win and computer_win1 > computer_win2:
        print('You have lose ! and computer1 win , your score is {} and computer1 score is {} and the computer2 score is {}'.format(user_win,computer_win1,computer_win2))
    else:
         print('You have lose ! and computer2 win , your score is {} and computer1 score is {} and the computer2 score is {}'.format(user_win,computer_win1,computer_win2))
game()