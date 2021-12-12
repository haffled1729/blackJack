from os import system
from random import randint
from time import sleep

#cards = {'A':[1,11], 'K':10, 'Q':10, 'J':10, '10':10, '9':9, '8':8,'7':7, '6':6, '5':5, '4':4, '3':3, '2':2, '1':1}
cards = list(range(1, 12))

def hit():
    return cards[randint(1,10)]     #Randint generates integers from start till end, including end

def compare(ply_scr, dlr_scr):
    if ply_scr != 21 and dlr_scr == 21:
        print("\n\t\tDealer Black Jack, you lose!")
        return True
    elif ply_scr == 21 and dlr_scr != 21:
        print("\n\t\tPlayer Black Jack, you win!")
        return True
    else:
        return False
        

def score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
            cards[cards.index(11)] = 1
            return sum(cards)
    else:
        return score

def play():
    ply_crds = []
    dlr_crds = []
    
    ply_crds.append(hit()) 
    ply_crds.append(hit())
    dlr_crds.append(hit())
    dlr_crds.append(hit())
    
    print(f"\n\t\tYour Cards: {ply_crds}")
    print(f"\n\t\tDealer: [{dlr_crds[0]}, X]")

    if compare(score(ply_crds), score(dlr_crds)):
        print(f"\n\t\tYour Final Hand: {ply_crds}")
        print(f"\t\tDealer's Final Hand: {dlr_crds}")
        return
    elif score(ply_crds) == 21 and score(dlr_crds) == 21:
        print("\n\t\tBust!")
        sleep(2)
        return
    else: 
        while True: 
            rnd = int(input("\n\t\tHit(0) or Stay(1): "))

            if rnd == 1:
                while score(dlr_crds) < 17:
                        dlr_crds.append(hit())
                if score(dlr_crds) > score(ply_crds):
                    print("\n\t\tDealer Wins!")
                    print(f"\n\t\tYour Final Hand: {ply_crds}")
                    print(f"\t\tDealer's Final Hand: {dlr_crds}")
                    sleep(2)
                    return
                elif score(dlr_crds) < score(ply_crds):
                    print("\n\t\tYou Win!")
                    print(f"\n\t\tYour Final Hand: {ply_crds}")
                    print(f"\t\tDealer's Final Hand: {dlr_crds}")
                    sleep(2)
                    return
                else:
                    print("\n\t\tBust!")
                    sleep(2)
                    return
                    
            elif rnd == 0:
                ply_crds.append(hit())
                if score(ply_crds) > 21:
                        print("\n\t\tYou went over 21, you lose!")
                        print(f"\n\t\tYour Final Hand: {ply_crds}")
                        print(f"\t\tDealer's Final Hand: {dlr_crds}")
                        sleep(2)
                        return
                print(f"\n\t\tYour Cards: {ply_crds}")
            else:
                print("\n\t\tPlease enter a valid choice.")

def menu():
    choice = 1
    while(choice != 2):
        system('cls')
        print("\n\t\t\tBLACK JACK\n")
        print("\n\t\t1.Play a Game\n\t\t2.Exit")
        choice = int(input("\n\t\tChoose: "))
        if choice == 1:
            play()
        elif choice == 2:
            exit()
        else:
            print("\n\t\tPlease enter a valid choice.")
    
menu()
