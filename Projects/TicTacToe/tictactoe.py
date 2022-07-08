
def getValue(state):
    '''
    Returns the value of a state. Only terminal states have values and 
    they are defined in the following way:

    X win = +1
   
    O win = -1
   
    Tie = 0

    If the state is not a terminal state, it returns None as its value
    '''
    value = None
    terminal = isTerminal(state)
    isWin = boardIsWin(state.board)
    nextSymbol = getNextPlayerSymbol(state)
    if(isWin and nextSymbol == "X"): # O player wins
        value = -1
    elif(isWin and nextSymbol == "O"): # X player wins
        value = 1
    elif(terminal and not isWin):
        value = 0
    return value


def boardIsWin(state):
    '''
    Returns True if either player has won the game, returns False otherwise.
    '''
    # Check row win/lose
    for i in range(len(state)):
        symbol = state[i][0]
        j = 0
        while(j < len(state[i]) and symbol != None):
            if(state[i][j] != symbol):
                break
            j += 1
        if(j == len(state[i])): 
            return True
                
    # Check column win/lose
    for i in range(len(state)):
        symbol = state[0][i]
        j = 0
        while(j < len(state[i]) and symbol != None):
            if(state[j][i] != symbol):
                break
            j += 1
            
        if(j == len(state)): 
            return True

    # Check diagonal win/lose
    isWin = True
    symbol = state[0][0]
    for i in range(len(state)):
        if(state[i][i] != symbol or symbol == None):
            isWin = False
            break 
    if(isWin):
        return True

    isWin = True
    symbol = state[-1][0]
    i = len(state) - 1
    j = 0
    while(i >= 0 and j < len(state)):
        if(state[i][j] != symbol or symbol == None):
            isWin = False
            break 
        i -= 1
        j += 1
    if(isWin):
        return True
    # If none of the above returned, check if there is a tie
    # A tie happens when none of the players won and there
    # are no empty spaces left in the board (i.e when there are no turns left)
    return False

def isTerminal(gameState):
    ''' 
    Returns True if the current state is a terminal state. Returns False otherwise. 
    A state is a terminal state if a player wins or if there are no more turns left.
    '''
    if(gameState.turnCounter == 0 or boardIsWin(gameState.board)): 
        return True
    return False

def getNextPlayerSymbol(gameState):
    '''
    Returns the symbol of the player whose turn occurs immediately after the current one.
    '''
    if(gameState.turnCounter %2 == 1): # current Player is X
        return "O"
    else: # Current Player is O
        return "X"

def getCurrPlayerSymbol(gameState):
    '''
    Returns the symbol of the player whose turn occurs immediately after the current one.
    '''
    if(gameState.turnCounter %2 == 1): # current Player is X
        return "X"
    else: # Current Player is O
        return "O"

def legalActions(state):
    '''
    Returns a list of the legal actions available in the current state of the game.
    '''
    nextSymbol = getCurrPlayerSymbol(state)
    legal = []
    for i in range(len(state)):
        for j in range(len(state[i])):
            if(state[i][j] == None):
                legal.append((nextSymbol, i, j))
    return legal


def stateDeepCopy(state):
    '''
    Returns a deep copy of a 2D array
    '''
    cpy = []
    i = 0
    for row in state:
        cpy.append([])
        for item in row:
            cpy[i].append(item)
        i += 1
    return cpy

def getSuccessor(state, action):
    symbol, i, j = action
    newState = stateDeepCopy(state)
    newState[i][j] = symbol
    return newState

def maxValue(state):
    '''
    Doc goes here
    '''
    terminal, _ = isTerminal(state)
    if(terminal):
        return getValue(state), None
    v = float("-inf")
    action = None

    for a in legalActions(state):
        successor = getSuccessor(state, a)
        v2, a2 = minValue(successor)
        if(v2 > v):
            v = v2
            action = a
    
    return v, action

def minValue(state):
    terminal, _ = isTerminal(state)
    if(terminal):
        return getValue(state), None
    v = float("inf")
    for a in legalActions(state):
        successor = getSuccessor(state, a)
        v2, a2 = maxValue(successor)
        if(v2 < v):
            v = v2
            action = a
    
    return v, action

# TODO: finish computeNextAction from state values
def computeNextAction(state, player):
    if(player == 'X'):
        value, action = maxValue(state)
        return action
    else:
        value, action = minValue(state)
        return action

def getPlayerMove(playerSymbol, board):
    legalMoves = legalActions(board)
    playerMove = None
    while(playerMove not in legalMoves):
        print("The legal moves are: ")
        for move in legalMoves():
            symb, i, j = move
            print(f"({i}, {j})")
        coord = input("Enter a move as a pair of numbers separated by a space: ").split()
        i = int(coord[0])
        j = int(coord[1])
        playerMove = (playerSymbol, i, j)
        if(playerMove not in legalMoves):
            print("You entered an illegal move.")
    return playerMove 

def printBoard(board):
    print()
    i = j = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] != None and j < len(board[0]) - 1):
                print(board[i][j], end =" | ")
            elif(board[i][j] != None):
                print(board[i][j])
            elif(board[i][j] == None and j < len(board[0]) - 1):
                print("-", end =" | ")
            else:
                print("-")
    print()



class GameState:
    def __init__(self, spaces) -> None:
        self.board = [ [ None for _ in range(spaces)] for _ in range(spaces)]
        self.turnCounter = spaces**2
    
        

def tictactoe(player):
    # create an empty board with a turn counter
    gameState = GameState(3)

    while(not isTerminal(gameState)):
        if(turnCounter %2 == 1): # X turn
            if(player == "X"):
                playerTurn("X")
            else:
                aiTurn("X")
        elif(turnCounter %2 == 0): # O turn
            if(player == "O"):
                playerTurn("O")
            else:
                aiTurn("O")

        turnCounter -= 1





    if(player == "X"):
        terminal, winner = isTerminal(board)
        while(not terminal):
            printBoard(board)
            print(board)
            playerMove = getPlayerMove(player, board)
            print(playerMove)
            board = getSuccessor(board, playerMove)
            if(terminal):
                break
            aiVal, aiMove = minValue(board)
            board = getSuccessor(board, aiMove)
            terminal, winner = isTerminal(board)
        printBoard(board)
        print(f"{winner} WINS!!!")
    else:
        terminal, winner = isTerminal(board)
        while(not terminal):
            aiVal, aiMove = minValue(board)
            board = getSuccessor(board, aiMove)
            printBoard(board)
            terminal, winner = isTerminal(board)
            if(terminal):
                break
            playerMove = getPlayerMove(player, board)
            print(playerMove)
            board = getSuccessor(board, playerMove)
            terminal, winner = isTerminal(board)
        printBoard(board)
        print(f"{winner} WINS!!!")
    
def main():

    player = None

    while(player != "X" and player != "O"):
        player = input("Enter what do you want to play as (X/O) (q to quit): ")
        if (player == "q"):
            return
        elif(player != "X" and player != "O"):
            print("You entered an invalid symbol. Try again.")
    tictactoe(player)

if(__name__ == "__main__"):
    main()