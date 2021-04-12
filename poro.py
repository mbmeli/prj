from random import randint
while True :
    print("\n \n \n ")
    #1
    print("let's play a game \n")

    #2

    #3(creat list for game)
    L = ["rock=1","paper=2","sicissor=3"]
    for i in L:
        print(i)

    computer=randint(1,3)

    #4
    player=int(input('enter your selection az number : '))
    if player == 1 :
        print("you choose rock")
    elif player==2 :
        print("you choose paper")
    elif player ==3 :
        print("you choose secissor")

    if computer == 1 :
        print("computer choose rock")
    elif computer== 2 :
        print("computer choose paper")
    elif computer== 3 :
        print("computer choose secissor")

    #5
    def game():
        if player == computer:
            print("mosavi")

        elif player== 1 and computer==2:
            print("computer bord")

        elif player==1 and computer==3:
            print("to bord")
        #---------------------------------------

        elif player==2 and computer==1:
            print("to bordi")

        elif player==2 and computer==3:
            print("computer bord")
        #---------------------------------------
        elif player==3 and computer==1:
            print("computer bord")
        
        elif player==3 and computer== 2: 
            print("to bordi")
        
        else :
            print("adad 1-3 hatman vared konid")
    game()