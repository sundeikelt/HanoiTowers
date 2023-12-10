import turtle
import copy
import time

#PART A -------------------------------------------------------
#The function returns a list representing the configuration of the hanoi towers.
def init(n):
    list = [[],[],[]]
    for i in range(n, 0, -1):
        list[0].append(i)
    return list

def nbDiscs(board, nt):
    return len(board[nt])

#returns the disc found on top of the tower nt
def supDisc(board, nt):
    len_nt = nbDiscs(board, nt)
    if len_nt == 0:
        return -1
    else:
        return board[nt][len_nt-1]

#returns the position of the disc in the configuration, board 
def posDisc(board, nd):
    for i in range(len(board)):
        for disc in board[i]:
            if disc == nd:
                return i

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
    while pos < len(board[disc_tower]) and board[disc_tower][pos]!=nd :
        pos+=1
    #at the end of the while pos will be equal to the position of 
    # nb in the list of its tower

    #once again the towerWidth is required and it represents the same size as before
    towerWidth = composant_width*(n+1)*2+stickw

    #in order to set the pen on the bottom left of the disc we need to move the pen at:
    #   discx = the widths of the tower before + the difference in width between the dic nd and the dic n
    #   discy = which represents the height from the table
    discx = x + (towerWidth)*(disc_tower) + composant_width*(n-nd+1)
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
    while pos <= len(board[disc_tower]) and board[disc_tower][pos]!=nd :
        pos+=1
    #at the end of the while pos will be equal to the position of nb in the list of its tower

    #once again we need the width of a tower
    towerWidth = composant_width*(n+1)*2+stickw

    #in order to set the pen on the bottom left of the disc we need to move the pen at:
    #   discx = the widths of the tower before + the difference in width between the dic nd and the dic n
    #   discy = which represents the height from the table
    discx = x + (towerWidth)*(disc_tower) + composant_width*(n-nd+1)
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
        tower_start = input("Starting tower? ")
        if tower_start != "":
            tower_start = int(tower_start)
            if 0>tower_start or tower_start>2:
                print("The tower", tower_start, "does not exist! ", end = "")
            elif supDisc(board, tower_start) == -1:
                print("Invalid, empty tower. ", end="")
            else:
                ok = True
        
    ok = False
    tower_start_sup = supDisc(board, tower_start)
    while not(ok):
        tower_arrival = int(input("Arrival tower? "))
        if 0>tower_arrival or tower_arrival>2:
            print("The tower", tower_arrival, "does not exist! ", end = "")
        elif tower_arrival == tower_start:
            print("Invalid, same tower. ",  end = "")
        elif verifMove(board, tower_start, tower_arrival)==False : #NEED TO IMPLEMENT MESSAGE FOR IF START = ARRIVAL
            print("Invalid, smaller disc.",  end = "")
        else:
            ok = True
    
    return tower_start, tower_arrival

def playOne(board, n, tower_start = -1, tower_arrival = -1):
    if tower_start == -1:
        tower_start, tower_arrival = readCoords(board)

    print("Moving disc", supDisc(board, tower_start), "from tower", tower_start, "to tower", tower_arrival)

    #erases disc on top of the start tower
    eraseDisc(supDisc(board, tower_start), board, n)

    disc = board[tower_start][len(board[tower_start])-1]
    board[tower_arrival].append(disc)
    board[tower_start].pop(len(board[tower_start])-1) 

    drawDisc(disc, board, n)

#PART D -------------------------------------------------------
def lastMove(moves):
    last_move = 0
    for move in moves:
        if move > last_move:
            last_move = move
    
    board1 = moves[last_move-1]
    board2 = moves[last_move]

    start_tower = -1
    arrival_tower = -1
    tower = 0
    while start_tower == arrival_tower and tower < len(board1):
        pos = 0
        while start_tower == arrival_tower and pos < nbDiscs(board1, tower):
            disc = board1[tower][pos]
            start_tower = posDisc(board1, disc)
            arrival_tower = posDisc(board2, disc)
            pos += 1
        tower+=1
    #both loops will stop when the position of a disc in board1 is different than its position in board2 
    
    return start_tower, arrival_tower

def cancelLast(moves):
    print("Cancelling last move.")
    last_move = 0
    for move in moves:
        if move > last_move:
            last_move = move

    start_tower, arrival_tower = lastMove(moves)
    last_configuration = copy.deepcopy(moves[last_move])
    before_last_configuration = copy.deepcopy(moves[last_move-1])
    disc = supDisc(last_configuration, arrival_tower)

    #the following three lines are used to store the number of discs in n
    n = 0
    for i in range(0, 3):
        n += nbDiscs(last_configuration, i)

    eraseDisc(disc, last_configuration, n)
    drawDisc(disc, before_last_configuration, n)

    del moves[last_move]
#did not add option part from the pdf
#END PART D

def playLoop(board, n):
    moves = {0:copy.deepcopy(board)}

    max_moves = 2**n-1
    move = 0
    win = False
    while win != True and move<max_moves:
        print("Move number", move+1, "---------------------------")
        print("Remaining moves:", max_moves-move)

        playOne(board, n)
        move += 1
        moves[move] = copy.deepcopy(board)

        win = win or verifVictory(board, n)

        if not(win):
            cancel = input("Cancel move? ")
            if cancel == "yes":
                cancelLast(moves)
                move -= 1
                board = copy.deepcopy(moves[move])

        win = win or verifVictory(board, n)
                
    if move<max_moves:
        print("Congrats! You won!")
    else:
        print("You lost!")
    nb_moves = move
    return nb_moves, win

#DID NOT ADD POSSIBLE IMPROVEMENTS PART C
#END PART C

#Part E ---------------------
def saveScore(scores, name,  n, nbmoves, game_time):
    print("Saving score")
    game = {"discs":n, "moves":nbmoves, "time":game_time}
    if name in scores:
        scores[name].append(game)
    else:
        scores[name] = [game]

def getBestScore(scores, name, nbdiscs):
    player_scores = scores[name]
    if len(player_scores) == 0:
        return -1
    best_score = -1
    for score in player_scores:
        if score["discs"] == nbdiscs and (best_score > score["moves"] or best_score == -1):
            best_score = score["moves"]
    return best_score

def displayScores(scores, n):
    ordered_players = []
    for player in scores:
        playerBestScore = getBestScore(scores, player, n)
        if playerBestScore != -1:
            i = 0
            while i<len(ordered_players) and playerBestScore > getBestScore(scores, ordered_players[i], n):
                i += 1
            ordered_players.insert(i, player)

    print("--------BEST SCORES FOR", n, "DISCS--------")
    for i in range(len(ordered_players)):
        print("Place", i+1, end=" ")
        if i < len(ordered_players):
            print(ordered_players[i])
        else:
            print("----EMPTY----")

def getBestTime(scores, name):
    player_scores = scores[name]
    if len(player_scores) == 0:
        print("Error, empty score")
        return -1
    best_time = -1
    for score in player_scores:
        if best_time > score["time"] or best_time == -1:
            best_time = score["time"]
    return best_time

def displayTimes(scores):
    ordered_players = []
    if len(scores) == 0:
        print("NO GAMES PLAYED")
    else:
        for player in scores:
            player_best = getBestTime(scores, player)
            i = 0
            while i < len(ordered_players) and \
                player_best > getBestTime(scores, ordered_players[i]):
                i+=1
            ordered_players.insert(i, player)

    print("-------PLAYERS RANKED BY THEIR TIME-------")
    for i in range(len(ordered_players)):
        print(i+1, ordered_players[i])

def avgTime(scores):
    average_per_player = {}
    for player in scores:
        nb_moves = 0
        time = 0
        for game in scores[player]:
            nb_moves += game["moves"]
            time += game["time"]
        avg_player = time/nb_moves
        average_per_player[player] = avg_player
    return average_per_player

def displayByAverage(scores):
    average_per_player= avgTime(scores)
    ordered_players = []
    for player in average_per_player:
        avg_player = average_per_player[player]
        i = 0
        while i < len(ordered_players) and avg_player > average_per_player[ordered_players[i]]:
            i+=1
        ordered_players.insert(i, player)
    
    print("-------PLAYERS RANKED BY AVERAGE THINKING TIME-------")
    for i in range(len(ordered_players)):
        print(i+1, ordered_players[i])
        
#did not add options 8, 10, 11
#END PART E -------------------

def autoSolve(n, disc=-1, source = 0, destination = 2, auxiliary = 1, moves = []):
    if disc == -1:
        disc = n
    if disc==1:
        moves.append([source, destination])
        return
    autoSolve(n, disc-1, source, auxiliary, destination, moves)
    moves.append([source, destination])
    autoSolve(n, disc-1, auxiliary, destination, source, moves)

    return moves

def animateMoves(board, n, moves):
    for move in moves:
        playOne(board, n, move[0], move[1])
    return 0

# each name of a player is the jey to a list of games, each game is also a list, which includes
#   the number of discs on the first poisiton and then the number of moves on the second position and the time on the third
#   that being said the dictionary scores looks something like this:
#   scores = { name:[
#           {"discs":x, "moves":y, "time":z},
#           {"discs":a, "moves":b, "time":c}] 
#           }
scores = {"Radu":[{"discs":4, "moves":2, "time":32}, \
                        {"discs":3, "moves":18, "time":4444}, \
                        {"discs":3, "moves":9, "time":99}], \
                        
            "Jhon":[{"discs":5, "moves":5, "time":42}, \
                        {"discs":3, "moves":10, "time":20}, \
                        {"discs":2, "moves":100, "time":5}], \
                        
            "Maya":[{"discs":4, "moves":66, "time":10}, \
                        {"discs":5, "moves":56, "time":10}, \
                        {"discs":3, "moves":33, "time":44}], \
                        
            "Jasmine":[{"discs":6, "moves":56, "time":33}, \
                        {"discs":4, "moves":44, "time":41}, \
                        {"discs":3, "moves":23, "time":55}], \
                        
            "Maxwell":[{"discs":4, "moves":22, "time":31234}, \
                        {"discs":5, "moves":13, "time":44344}, \
                        {"discs":6, "moves":96, "time":99333}], \
                            }


#scores = {}
board = [[],[],[]]
n = 0
print("Hanoi towers, welcome")
rep = "play"
while rep in ["play", "auto", "ranking scores", "ranking time", "ranking thinking time"]:
    rep = input("What do you want to do / see (play / auto / ranking scores / ranking time / ranking thinking time / goodbye) ? ")
    if rep == "play" or rep =="auto":
        if board != [[], [], []]:
            resetConfig(board, n)
            t.color("white")
            drawBoard(n)
            t.color("black")

        n = int(input("How many discs? "))
        board = init(n)
        drawBoard(n)
        drawConfig(board, n)

        if rep == "play":
            start_time = time.time()
            nbmoves, win = playLoop(board, n)
            game_time = round(time.time() - start_time, 2)

            if win:
                name = input("Name? ")
                saveScore(scores, name, n, nbmoves, game_time)
            else:
                rep = input("Do you want to see the solution? ")
                if rep == "yes":
                    rep = "auto" 
                    resetConfig(board, n)
                    board = init(n) 
                    drawConfig(board, n) #prepares the board for the solution simulation
                #changing rep into auto will trigger the if rep=="auto" lines underneath,
                #   while also allowing the simple response of "auto" when the player is asked what they want to do

        if rep == "auto":
            moves = autoSolve(n)
            animateMoves(board, n, moves)
    elif rep == "ranking scores":
        n = int(input("Ranking by score for how many discs? "))
        displayScores(scores, n)
    elif rep == "ranking time":
        displayTimes(scores)
    elif rep == "ranking thinking time":
        displayByAverage(scores)
    elif rep == "goodbye":
        rep = ""
    

print("Goodbye!")

input()

