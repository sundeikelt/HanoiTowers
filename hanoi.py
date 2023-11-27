import turtle

#PART A -------------------------------------------------------
#The function returns a list representing the configuration of the hanoi towers.
def init(n):
    list = [[],[],[]]
    for i in range(n, 0, -1):
        list[0].append(i)
    return list

def nbDiscs(board, nt):
    return len(board[nt-1])

def supDisc(board, nt):
    len_nt = nbDiscs(board, nt)
    if len_nt == 0:
        return -1
    else:
        return board[nt-1][len_nt-1]
    
def posDisc(board, nd):
    for i in range(len(board)):
        for disc in board[i]:
            if disc == nd:
                return i+1
            
def verifMove(board, nt1, nt2):
    supnt1 = supDisc(board, nt1)
    supnt2 = supDisc(board, nt2)
    if supnt1 != -1 and (supnt2 == -1 or supnt2 > supnt1):
        return True
    return False

#TO BE OPTIMISED
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

t = turtle.Turtle()
t.speed(10)
x = -300
y = -200

length = 15
width = 20
stickw = 6

def movepen(a, b):
    t.up()
    t.goto(a, b)
    t.down()

def drawBoard(n):
    movepen(x, y)
    boardLength = (length*(n+1)*2+stickw)*3
    for i in range(2):
        t.forward(boardLength)
        t.right(90)
        t.forward(width)
        t.right(90)

    for i in range(3):
        movepen(x + i*((length*(n+1))*2+stickw) + length*(n+1), y)
        for i in range(2):
            t.forward(stickw)
            t.left(90)
            t.forward(width*(n+1))
            t.left(90)
    movepen(x, y)

def drawDisc(nd, board, n):
    tower = posDisc(board, nd)

    pos = 0
    while pos < len(board[tower-1]) and board[tower-1][pos]!=nd :
        pos+=1
    #at the end of the while pos will be equal to the position of 
    # nb in the list of its tower

    towerWidth = length*(n+1)*2+stickw
    discx = x + (towerWidth)*(tower-1) + length*(n-nd+1)
    discy = y + 20*pos

    #Delete stick behind the disk
    t.color("white")
    movepen(discx+(length*nd), discy)
    t.left(90)
    t.forward(width)
    movepen(discx+(length*nd)+6, discy)
    t.forward(width)
    t.right(90)
    #drawing the disk
    t.color("black")
    movepen(discx, discy)
    for i in range(2):
        t.forward((length*nd)*2+stickw)
        t.left(90)
        t.forward(width)
        t.left(90)

def eraseDisc(nd, board, n):
    tower = posDisc(board, nd)

    pos = 0
    while pos <= len(board[tower-1]) and board[tower-1][pos]!=nd :
        pos+=1
    #at the end of the while pos will be equal to the position of nb in the list of its tower

    towerWidth = length*(n+1)*2+stickw
    discx = x + (towerWidth)*(tower-1) + length*(n-nd+1)
    discy = y + 20*pos

    t.color("white")
    movepen(discx, discy)
    for i in range(2):
        t.forward((length*nd)*2+stickw)
        t.left(90)
        t.forward(20)
        t.left(90)

    t.color("black")
    t.forward((length*nd)*2+stickw)


    movepen(discx+(length*nd), discy)
    t.left(90)
    t.forward(20)
    movepen(discx+(length*nd)+6, discy)
    t.forward(20)
    t.right(90)

def drawConfig(board, n):
    for i in range(n, 0, -1):
        drawDisc(i, board, n)

def resetConfig(board, n):
    for i in range(1, n+1):
        eraseDisc(i, board, n)

#did not add the possible improvements part

#PART C -------------------------------------------------------
#OPTIMIZE
def readCoords(board): #ADD VERIF MOVE
    ok = False
    print("Enter the start tower? (1 / 2 / 3)", end = " ")
    while not(ok):
        tower_start = int(input(""))
        if 1>tower_start or tower_start>3:
            print("Wrong input! The tower", tower_start, "does not exist! \n Please enter a valid tower number (1 / 2 / 3): ", end = "")
        elif supDisc(board, tower_start) == -1:
            print("The selected tower does not have any discs on it. Please select another one: ", end="")
        else:
            ok = True
        
    ok = False
    tower_start_sup = supDisc(board, tower_start)
    print("Enter the destination tower? (1 / 2 / 3)", end = " ")
    while not(ok):
        tower_arrival = int(input(""))
        if 1>tower_arrival or tower_arrival>3:
            print("Wrong input! The tower", tower_arrival, "does not exist! \n Please enter a valid tower number (1 / 2 / 3): ", end = "")
        elif verifMove(board, tower_start, tower_arrival)==False : #NEED TO IMPLEMENT MESSAGE FOR IF START = ARRIVAL
            print("The superior disc on the arrival tower (", supDisc(board, tower_arrival), ") is smaller than the superior disc on the start tower (", tower_start_sup, ")")
            print("Please select another tower on which the disc ", tower_start_sup, "can be moved: ", end="")
        else:
            ok = True
    
    return tower_start, tower_arrival

def playOne(board, n):
    tower_start, tower_arrival = readCoords(board)

    #erases disc on top of the start tower
    eraseDisc(supDisc(board, tower_start), board, n)

    disc = board[tower_start-1][len(board[tower_start-1])-1]
    board[tower_arrival-1].append(disc)
    board[tower_start-1].pop(len(board[tower_start-1])-1) 

    drawDisc(disc, board, n)

def playLoop(board, n):
    win = False
    while win != True:
        playOne(board, n)
        win = win or verifVictory(board, n)
    x=input("Congrats! You won!")

n = 5
board = [[5, 3, 1], [4, 2], []]
drawBoard(n)
drawConfig(board, n)
playLoop(board, n)
x = input()