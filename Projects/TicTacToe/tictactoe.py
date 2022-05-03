
class gameState:

    def __init__(self, board):
        self.board = board


'''
def whoWon(state):
    X = 0
    O = 0
    legal = []
    for row in state:
        for item in row:
            if(item == "X"):
                X += 1
            elif(item == "O"):
                O += 1
    nextSymbol = None
    if(X > O):
        nextSymbol = "O" 
    else:
        nextSymbol = "X"
'''
def getValue(state):
    value = None
    terminal, symbol = isTerminal(state) 
    if(terminal and symbol == "X"):
        value = 1
    elif(terminal and symbol == "O"):
        value = -1
    elif(terminal):
        value = 0
    return value
def isTerminal(state):
    # Check row win/lose
    for i in range(len(state)):
        symbol = state[i][0]
        j = 0
        while(j < len(state[i]) and symbol != None):
            if(state[i][j] != symbol):
                break
            j += 1
        if(j == len(state[i])): 
            return True, symbol
                
    # Check column win/lose
    for i in range(len(state)):
        symbol = state[0][i]
        j = 0
        while(j < len(state[i]) and symbol != None):
            if(state[j][i] != symbol):
                break
            j += 1
            
        if(j == len(state)): 
            return True, symbol

    # Check diagonal win/lose
    isWin = True
    symbol = state[0][0]
    for i in range(len(state)):
        if(state[i][i] != symbol or symbol == None):
            isWin = False
            break 
    if(isWin):
        return True, symbol

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
        return True, symbol

    for row in state:
        for item in row:
            if(item == None):
                return False, None 
    return True, None


def legalActions(state):
    X = 0
    O = 0
    legal = []
    for row in state:
        for item in row:
            if(item == "X"):
                X += 1
            elif(item == "O"):
                O += 1
    nextSymbol = None
    if(X > O):
        nextSymbol = "O" 
    else:
        nextSymbol = "X"

    for i in range(len(state)):
        for j in range(len(state[i])):
            if(state[i][j] == None):
                legal.append((nextSymbol, i, j))
    return legal


def stateCopy(state):
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
    newState = stateCopy(state)
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

    '''
    successors = [getSuccessor(state, action) for action in legalActions(state)]
    for successor in successors:
        v = max(v, min_value(successor))
    return v
    '''
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
    '''
    successors = [getSuccessor(state, action) for action in legalActions(state)]
    for successor in successors:
        v = max(v, min_value(successor))
    return v
    '''
# TODO: finish computeNextAction from state values
def computeNextAction(state, player):
    if(player == 'X'):
        value, action = maxValue(state)
        return action
    else:
        value, action = minValue(state)
        return action

def getPlayerMove(playerSymbol):
    coord = input("Enter coordinates of move: ").split()
    i = int(coord[0])
    j = int(coord[1])
    return (playerSymbol, i, j) 

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

def ticTacToe(player):
    board = [ [ None for _ in range(3)] for _ in range(3)]
    if(player == "X"):
        terminal, winner = isTerminal(board)
        while(not terminal):
            printBoard(board)
            print(board)
            playerMove = getPlayerMove(player)
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
            playerMove = getPlayerMove(player)
            print(playerMove)
            board = getSuccessor(board, playerMove)
            terminal, winner = isTerminal(board)
        printBoard(board)
        print(f"{winner} WINS!!!")

        

ticTacToe("O")
    