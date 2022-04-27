
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
    isWin, symbol = isTerminal(state) 
    if(isWin and symbol == "X"):
        value = 1
    elif(isWin and symbol == "O"):
        value = -1
    elif(isWin):
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
            isWin = False, None
            break 
    if(isWin):
        return True, symbol

    isWin = True
    symbol = state[-1][0]
    i = len(state) - 1
    j = 0
    while(i >= 0 and j < len(state)):
        if(state[i][j] != symbol or symbol == None):
            isWin = False, None
            break 
        i -= 1
        j += 1
    if(isWin):
        return True, symbol

    return False, None

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

def getSuccessor(state, action):
    symbol, i, j = action
    newState = stateCopy(state)
    newState[i][j] = symbol
    return newState

def max_value(state):
    '''
    Doc goes here
    '''
    terminal, _ = isTerminal(state)
    if(terminal):
        return getValue(state)
    v = float("-inf")
    successors = [getSuccessor(state, action) for action in legalActions(state)]
    for successor in successors:
        v = max(v, min_value(successor))
    return v

def min_value(state):
    terminal, _ = isTerminal(state)
    if(terminal):
        return getValue(state)
    v = float("inf")
    successors = [getSuccessor(state, action) for action in legalActions(state)]
    for successor in successors:
        v = max(v, min_value(successor))
    return v

# TODO: finish computeNextAction from state values
def computeNextAction(state):
    actions = legalActions(state)
    

initialState = [ [ None for _ in range(3)] for _ in range(3)]


