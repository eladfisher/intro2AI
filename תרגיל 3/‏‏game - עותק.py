'''
presents:
Elad Fisher 213924624
Yehoshua Gronspecht 332521103


The following code calculates the value of a certain state in a classic 4-in-a-row game.
We start off by making sure that nobody has already won. We do so by checking if any player has four of their own in a row.

After we made sure that the game hasn’t ended yet, we check to see how many 3 in a row and
2 in a row each player has and calculate how bad or good the current state is based on how many
each player has in a row. The computer can now know what to do next based on the value given to the current state.
'''

import copy
import alphaBetaPruning
import random

VICTORY=10**20 #The value of a winning board (for max) 
LOSS = -VICTORY #The value of a losing board (for max)
TIE=0 #The value of a tie
SIZE=4 #the length of winning seq.
COMPUTER=SIZE+1 #Marks the computer's cells on the board
HUMAN=1 #Marks the human's cells on the board

rows=6
columns=7


class game:
    board=[]
    size=rows*columns
    playTurn = HUMAN
    
     #Used by alpha-beta pruning to allow pruning

    '''
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    '''

def create(s):
        #Returns an empty board. The human plays first.
        #create the board
        s.board=[]
        for i in range(rows):
            s.board = s.board+[columns*[0]]
        
        s.playTurn = HUMAN
        s.size=rows*columns
        s.val=0.00001
    
        #return [board, 0.00001, playTurn, r*c]     # 0 is TIE

def cpy(s1):
        # construct a parent DataFrame instance
        s2=game()
        s2.playTurn = s1.playTurn
        s2.size=s1.size
        s2.board=copy.deepcopy(s1.board)
        print("board ", s2.board)
        return s2
    
'''
the following code checks if any player can win the game
'''
def isWinner(s,isComputer): #s - state , isComputer - boolean varible that helps us to check whther the player win or the computer

    temp = HUMAN

    if(isComputer):
        temp = COMPUTER #identify the symboll that we need to check

    #check for horizontal 4
    for i in range(rows):
        counter = 0
        for j in range(columns):
            if (s.board[i][j] == temp):
                counter = counter + 1

            else:
                counter = 0

            if(counter == 4):
                return True

    # check for vertical 4
    for i in range(columns):
        counter = 0
        for j in range(rows):
            if (s.board[j][i] == temp):
                counter = counter + 1

            else:
                counter = 0

            if (counter == 4):
                return True

    # check for 4 diagonally with "head toward up"
    for i in range(rows):

        for j in range(columns):
            counter = 0
            for w in range (4):
                if (i+w <rows and j+w <columns):
                    if (s.board[i+w][j+w] == temp):
                        counter = counter + 1

                    else:
                        counter = 0

                    if (counter == 4):
                        return True

    # check for 4 diagonally with "head toward down"
    for i in range(rows):

        # check for horizontal n
        for j in range(columns):
            counter = 0
            for w in range (4):
                if (i + w < rows and j - w >= 0):
                    if (s.board[i + w][j - w] == temp):
                        counter = counter + 1

                    else:
                        counter = 0

                    if (counter == 4):
                        return True


#identify the symboll that we need to check
def n_in_row(s, isComputer, n): #s - state , isComputer - boolean varible that helps us to check whther the player win or the computer

    temp = HUMAN
    other = COMPUTER
    if(isComputer):
        temp = COMPUTER
        other = HUMAN
    sequence = 0

    #check for horizontal 4
    for i in range(rows):
        counter = 0
        for j in range(columns):
            if (s.board[i][j] == temp):
                counter = counter + 1

            else:
                counter = 0

            if(counter == n):
                if j +1  < columns:
                    if(s.board[i][j+1] != other):
                        sequence = sequence + 1

                if j != 0:
                    if(s.board[i][j-1] != other):
                        sequence = sequence + 1

    # check for vertical 4
    for i in range(columns):
        counter = 0
        for j in range(rows):
            if (s.board[j][i] == temp):
                counter = counter + 1

            else:
                counter = 0

            if (counter == n):
                if i + 1 <columns :
                    if (s.board[j][i+1] != other):
                        sequence = sequence + 1

                if i > 0:
                    if (s.board[j][i-1] != other):
                        sequence = sequence + 1

    # check for n diagonally with "head toward up"
    for i in range(rows):
        counter = 0
        for j in range(columns):

            for w in range (4):
                if(i+w<rows and j+w<columns):
                    if (s.board[i+w][j+w] == temp):
                        counter = counter + 1

                    else:
                        counter = 0

                if (counter == n):
                    if j+w+1 <columns and i+w+1 < rows :
                        if (s.board[i + 1 + w][j + 1 + w] != other):
                            sequence = sequence + 1

                    if j - w != 0 and i - w != 0:
                        if (s.board[i-1][j - 1] != other):
                            sequence = sequence + 1

    # check for n diagonally with "head toward down"
    for i in range(rows):
        counter = 0
        for j in range(columns):

            for w in range (4):
                if(i+w<rows and j-w >= 0):
                    if (s.board[i+w][j - w] == temp):
                        counter = counter + 1

                    else:
                        counter = 0

                if (counter == n):
                    if j - w > 0 and i + w + 1 < rows:
                        if (s.board[i + 1 + w][j - 1 - w] != other):
                            sequence = sequence + 1

                    if j != 0 and i != 0:
                        if (s.board[i - 1][j - 1] != other):
                            sequence = sequence + 1
    return sequence


'''
The following code calculates the value of a certain state in a classic 4-in-a-row game. 
We start off by making sure that nobody has already won. We do so by checking if any player has four of their own in a row.

After we made sure that the game hasn’t ended yet, we check to see how many 3 in a row and
2 in a row each player has and calculate how bad or good the current state is based on how many
each player has in a row. The computer can now know what to do next based on the value given to the current state.
'''
def value(s):
#Returns the heuristic value of s

    if isWinner(s,True):
        return VICTORY

    if isWinner(s,False):
        return LOSS

    com_sequnce_3 = n_in_row(s,True,3)
    hum_sequence_3 = n_in_row(s,False,3)

    com_sequence_2 = n_in_row(s,True,2)
    hum_sequence_2 = n_in_row(s,False,2)


    state_value = (com_sequnce_3 - hum_sequence_3) * 100
    state_value = state_value + (com_sequence_2-hum_sequence_2) * 10

    if(state_value==0):
        return 1
    return state_value

def printState(s):
#Prints the board. The empty cells are printed as numbers = the cells name(for input)
#If the game ended prints who won.

        for r in range(rows):
            print("\n|",end = "")
        #print("\n",len(s[0][0])*" --","\n|",sep="", end="")
            for c in range(columns):
                if s.board[r][c]==COMPUTER:
                    print("X|", end="")
                elif s.board[r][c]==HUMAN:
                    print("O|", end="")
                else:
                    print(" |", end="")

        print()

        for i in range(columns):
            print(" ",i, sep = "",end="")

        print()
        
        val=value(s)

        if val==VICTORY:
            print("I won!")
        elif val==LOSS:
            print("You beat me!")
        elif val==TIE:
            print("It's a TIE")



def isFinished(s):
#Seturns True iff the game ended
        return value(s) in [LOSS, VICTORY, TIE] or s.size==0


def isHumTurn(s):
#Returns True iff it is the human's turn to play
        return s.playTurn==HUMAN
    


def decideWhoIsFirst(s):
#The user decides who plays first
        if int(input("Who plays first? 1-me / anything else-you : "))==1:
            s.playTurn=COMPUTER
        else:
            s.playTurn=HUMAN
            
        return s.playTurn
        

def makeMove(s, c):
#Puts mark (for huma. or comp.) in col. c
#and switches turns.
#Assumes the move is legal.

        r=0
        while r<rows and s.board[r][c]==0:
            r+=1

        s.board[r-1][c]=s.playTurn # marks the board
        s.size -= 1 #one less empty cell
        if (s.playTurn == COMPUTER ):
            s.playTurn = HUMAN
        else:
            s.playTurn = COMPUTER

   
def inputMove(s):
#Reads, enforces legality and executes the user's move.

        #self.printState()
        flag=True
        while flag:
            c=int(input("Enter your next move: "))
            if c<0 or c>=columns or s.board[0][c]!=0:
                print("Illegal move.")

            else:
                flag=False
                makeMove(s,c)

        
def getNext(s):
#returns a list of the next states of s
        ns=[]
        for c in list(range(columns)):
            print("c=",c)
            if s.board[0][c]==0:
                print("possible move ", c)
                tmp=cpy(s)
                makeMove(tmp, c)
                print("tmp board=",tmp.board)
                ns+=[tmp]
                print("ns=",ns)
        print("returns ns ", ns)
        return ns

def inputComputer(s):    
        return alphaBetaPruning.go(s)
