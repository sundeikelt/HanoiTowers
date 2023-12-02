import turtle

#PART A -------------------------------------------------------
#The function returns a list representing the configuration of the hanoi towers.
def init(n):
    list = [[],[],[]]
    for i in range(n, 0, -1):
        list[0].append(i)
    return list

#the towers are numbered from 1 to 3 but in the confirguration they are numbered from 0 to 2
def nbDiscs(board, nt):
    return len(board[nt-1])

#returns the disc found on top of the tower nt (saved int the board at nt-1)
def supDisc(board, nt):
    len_nt = nbDiscs(board, nt)
    if len_nt == 0:
        return -1
    else:
        return board[nt-1][len_nt-1]

#returns the position of the disc in the configuration, board 
def posDisc(board, nd):
    for i in range(len(board)):
        for disc in board[i]:
            if disc == nd:
                return i+1

#returns True if the superiour disc on the tower nt1 can be moved on top of the tower nt2 or False otherwise         
def verifMove(board, nt1, nt2):
    supnt1 = supDisc(board, nt1)
    supnt2 = supDisc(board, nt2)
    if supnt1 != -1 and (supnt2 == -1 or supnt2 > supnt1):
        return True
    return False

#returns True if the first two towers are empty and the last one filled with all the discs or False otherwise
def verifVictory(board, n):
    if len(board[0])+len(board[1])== 0 and len(board[2]) == n:
        i = n
        while i > 0:
            if board[2][n-i]!=i:
                return False
            i -= 1
        return True
    else:
        return False


#PART B -------------------------------------------------------

#basic configuration for the turtle and setting the starting position at a predifined x and y which will later be used
t = turtle.Turtle()
t.speed(10)
x = -300
y = 100

#the variable composant_width will be used as a unity masure for the different size of the discs and table
composant_width = 15
#the variable width represents the width of the table and that of a disc
width = 20
#stickw represents the width of the three towers placed on the table
stickw = 6

#the function movepen is used to simplify the moving of the pen so that the three lines are not repeated
def movepen(a, b):
    t.up()
    t.goto(a, b)
    t.down()

def drawBoard(n):
    movepen(x, y)
    #the variable towerWidth is made by composant_width*(n+1) representing half of one tower
    #       so that the discs can fit on each tower, while leaving a space before and after the towers
    towerWidth = composant_width*(n+1)*2+stickw
    #since there are 3 towers, the board width is the the towerWidth*3
    boardWidth = towerWidth*3

    #in order to draw the board we repeat two times the following lines
    for i in range(2):
        t.forward(boardWidth)
        t.right(90)
        t.forward(width)
        t.right(90)

    #then, in order to draw al three towers we repeat 3 times
    for i in range(3):
        #every time we move the pen depending on the i to the coresponding tower and we add half of a towerWidth 
        #   in order to get to the x position where the tower is located, the y position remains unchanged
        movepen(x + i*(towerWidth) + composant_width*(n+1), y)
        #once again we repeat two times the drawing of the tower represented by 2 lines, 
        #   whose height represent the variable width*(n+1) in order to also leave space on top of a tower filled with the maximum of discs
        for i in range(2):
            t.forward(stickw)
            t.left(90)
            t.forward(width*(n+1))
            t.left(90)

    #then, we move the pen to the origin position
    movepen(x, y)

def drawDisc(nd, board, n):
    disc_tower = posDisc(board, nd)

    #the variable pos is required in order to know how much space to leave under the disc
    pos = 0
    while pos < len(board[disc_tower-1]) and board[disc_tower-1][pos]!=nd :
        pos+=1
    #at the end of the while pos will be equal to the position of 
    # nb in the list of its tower

    #once again the towerWidth is required and it represents the same size as before
    towerWidth = composant_width*(n+1)*2+stickw

    #in order to set the pen on the bottom left of the disc we need to move the pen at:
    #   discx = the widths of the tower before + the difference in width between the dic nd and the dic n
    #   discy = which represents the height from the table
    discx = x + (towerWidth)*(disc_tower-1) + composant_width*(n-nd+1)
    discy = y + 20*pos

    #Delete stick behind the disk
    t.color("white")
    t.left(90)  #turns the pen direction upwards
    for i in range(2):
        movepen(discx+(composant_width*nd) + stickw*i, discy)
        t.forward(width)
    t.right(90) #turns the pen back towards left

    #drawing the disc
    t.color("black")
    movepen(discx, discy)
    for i in range(2):
        t.forward((composant_width*nd)*2+stickw)
        t.left(90)
        t.forward(width)
        t.left(90)

def eraseDisc(nd, board, n):
    disc_tower = posDisc(board, nd)

    pos = 0
    while pos <= len(board[disc_tower-1]) and board[disc_tower-1][pos]!=nd :
        pos+=1
    #at the end of the while pos will be equal to the position of nb in the list of its tower

    #once again we need the width of a tower
    towerWidth = composant_width*(n+1)*2+stickw

    #in order to set the pen on the bottom left of the disc we need to move the pen at:
    #   discx = the widths of the tower before + the difference in width between the dic nd and the dic n
    #   discy = which represents the height from the table
    discx = x + (towerWidth)*(disc_tower-1) + composant_width*(n-nd+1)
    discy = y + 20*pos

    #delete the disc
    t.color("white")
    movepen(discx, discy)
    for i in range(2):
        t.forward((composant_width*nd)*2+stickw)
        t.left(90)
        t.forward(20)
        t.left(90)

    t.color("black")
    #redraws the the bottom part of the disc, which represent the top part of the disc below
    t.forward((composant_width*nd)*2+stickw)

    t.left(90)  #turns the pen direction upwards
    for i in range(2):
        movepen(discx+(composant_width*nd) + stickw*i, discy)
        t.forward(width)
    t.right(90) #turns the pen back towards left

def drawConfig(board, n):
    #draws the discs from the biggest to the smallest
    for i in range(n, 0, -1):
        drawDisc(i, board, n)

def resetConfig(board, n):
    #deletes all discs from the smallest to the biggest
    for i in range(1, n+1):
        eraseDisc(i, board, n)

#did not add the possible improvements part

#PART C -------------------------------------------------------
#OPTIMIZE
def readCoords(board): #ADD VERIF MOVE
    ok = False
    while not(ok):
        tower_start = int(input("Starting tower? "))
        if 1>tower_start or tower_start>3:
            print("The tower", tower_start, "does not exist!", end = "")
        elif supDisc(board, tower_start) == -1:
            print("Invalid, empty tower.", end="")
        else:
            ok = True
        
    ok = False
    tower_start_sup = supDisc(board, tower_start)
    while not(ok):
        tower_arrival = int(input("Arrival tower? "))
        if 1>tower_arrival or tower_arrival>3:
            print("The tower", tower_arrival, "does not exist!", end = "")
        elif tower_arrival == tower_start:
            print("Invalid, same tower.")
        elif verifMove(board, tower_start, tower_arrival)==False : #NEED TO IMPLEMENT MESSAGE FOR IF START = ARRIVAL
            print("Invalid, smaller disc.")
        else:
            ok = True
    
    return tower_start, tower_arrival

def playOne(board, n):
    tower_start, tower_arrival = readCoords(board)

    print("Moving disc", supDisc(board, tower_start), "to tower", tower_arrival)

    #erases disc on top of the start tower
    eraseDisc(supDisc(board, tower_start), board, n)

    disc = board[tower_start-1][len(board[tower_start-1])-1]
    board[tower_arrival-1].append(disc)
    board[tower_start-1].pop(len(board[tower_start-1])-1) 

    drawDisc(disc, board, n)

def playLoop(board, n):
    win = False
    remaining_moves = n*2
    while win != True and remaining_moves>0:
        remaining_moves-=1
        print("Move number", n*2-remaining_moves)
        playOne(board, n)

        win = win or verifVictory(board, n)
        if not(win):
            print("Remaining moves:", remaining_moves)
    if remaining_moves>0:
        x=input("Congrats! You won!")
    else:
        x=input("You lost!")

print("Hanoi towers, welcome")
n = int(input("How many discs? "))
board = init(n)
drawBoard(n)
drawConfig(board, n)
playLoop(board, n)
x = input()
