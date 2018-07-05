##Technical assigments for further use.
from computer_functions import get_computer_move, HEAPS
list(HEAPS)
num_of_players=int(input("Please enter the number of human players (1 or 2):"))
ROW=("Row?")
NUM=("How many?")
PLAY=(", it's your turn.")
counter=0
emptylist=0
playgame="y"

##Function that prints the game board
def bprint(HEAPS):
    i=0
    while i+1<=len(HEAPS):
        print(i+1,":")
        print("*" * HEAPS[i])
        i+=1
    return

##Function that excutes a change in the heaps, with given heaps,
##row and number. and returns the new board.
def turn(board,row,num):
    if num<=board[row]:
        board[row]=(board[row])-num
        return (list(board))


##Function that is checking if the game is over.
def finished(heaps):
    i=0
    game=True
    while i!=len(heaps):
        if heaps[i]!=0:
            game=False
            break
        i+=1
    return game
            
##Player Vs. computer mode. gets from the player a legal row and number of matches to remove.
##sends it to the "turn" func, which excutes the move. and check if the player
##won. if not, continues to the computer move, and so on...
if num_of_players==1:
    player1=input("Please enter your name:")
    bprint(list(HEAPS))
    while playgame=="y" or playgame=="Y":
        while True:
            print(player1,PLAY)
            player1r=(input(ROW))
            while True:
                if player1r>len(HEAPS):
                    player1r=int(input(ROW))
                elif HEAPS[player1r-1]==0:
                    print("the row is empty.")
                    player1r=int(input(ROW))
                else:
                    break

            player1n=int(input(NUM))
            while True:
                if player1n>HEAPS[player1r-1]:
                    player1n=int(input(NUM))
                else:
                    break


            newHEAPS=turn(list(HEAPS),(player1r)-1,player1n)


            final=finished(newHEAPS)
            if final==True:
                print("You won!")
                break
            bprint(newHEAPS)
            compmove=get_computer_move(newHEAPS)
            print("Computer takes", compmove[1], "from row", compmove[0]+1)
            HEAPS=turn(newHEAPS,compmove[0],(compmove[1]))
            final=finished(HEAPS)
            if final==True:
                print("Computer wins!")
                break
            bprint(HEAPS)
        playgame=input("Play again? Y/N")

## Two player mode. Very simillar to the 1st one, only instead of computer there's player2
## playing against the 1st player
elif num_of_players==2:
    player1=input("Name of first player:")
    player2=input("Name of second player:")
    bprint(list(HEAPS))
    while playgame=="y" or playgame=="Y":
        while True:
            print(player1,PLAY)
            player1r=int(input(ROW))
            while True:
                if player1r>len(HEAPS):
                    player1r=int(input(ROW))
                elif HEAPS[player1r-1]==0:
                    print("the row is empty.")
                    player1r=int(input(ROW))
                else:
                    break
            player1n=int(input(NUM))
            while True:
                if player1n>HEAPS[player1r-1]:
                    player1n=int(input(NUM))
                else:
                    break
            newHEAPS=turn(list(HEAPS),(player1r)-1,player1n)
            final=finished(newHEAPS)
            if final==True:
                print(player1, "you won!")
                break
            else:
                bprint(newHEAPS)
            print(player2,PLAY)
            player2r=int(input(ROW))
            while True:
                if player2r>len(HEAPS):
                    player2r=int(input(ROW))
                elif newHEAPS[player2r-1]==0:
                    print("the row is empty.")
                    player2r=int(input(ROW))
                else:
                    break
            player2n=int(input(NUM))
            while True:
                if player2n>HEAPS[player2r-1]:
                    player2n=int(input(NUM))
                else:
                    break
            HEAPS=turn(list(newHEAPS),(player2r)-1,player2n)
            final=finished(HEAPS)
            if final==True:
                print(player2, "you won!")
                break
            bprint(HEAPS)
        playgame=input("Play again? Y/N")

        
    
    




