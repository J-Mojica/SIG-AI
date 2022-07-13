'''
This file contains the Game State class along with all functions necessary to
play the game and to extract all necessary information about the state of the game
'''
class GameState:
    '''
    Represents a TicTacToe game state. Contains the board and turn counter.
    A board is not limited to be 3x3, hence the dimensions of the board must be
    provided.
    '''
    def __init__(self, dimension) -> None:
        self.board = [ [ None for _ in range(dimension)] for _ in range(dimension)]
        self.turnCounter = dimension**2
        self.dimension = dimension
    
    def getDimension(self):
        return self.dimension
    def setDimension(self, newDim):
        '''
        Sets the dimensions of the board. When a new dimension is set, 
        the board is reset to fit those dimensions.
        '''
        self.dimension = newDim
        self.resetBoard()
    

    def getBoard(self):
        return self.board
    def setBoard(self, newBoard):
        self.board = newBoard
    def resetBoard(self):
        self.board = [ [ None for _ in range(self.dimension)] for _ in range(self.dimension)]
    

    def getTurnCounter(self):
        return self.turnCounter
    def setTurnCounter(self, newCounter):
        self.turnCounter = newCounter

def boardIsWin(state):
    '''
    Returns True if either player has won the game, returns False otherwise.
    '''
    # Check row win/lose
    board = state.getBoard()
    for i in range(len(board)):
        symbol = board[i][0]
        j = 0
        while(j < len(board[i]) and symbol != None):
            if(board[i][j] != symbol):
                break
            j += 1
        if(j == len(board[i])): 
            return True
                
    # Check column win/lose
    for i in range(len(board)):
        symbol = board[0][i]
        j = 0
        while(j < len(board[i]) and symbol != None):
            if(board[j][i] != symbol):
                break
            j += 1
            
        if(j == len(board)): 
            return True

    # Check diagonal win/lose
    isWin = True
    symbol = board[0][0]
    for i in range(len(board)):
        if(board[i][i] != symbol or symbol == None):
            isWin = False
            break 
    if(isWin):
        return True

    isWin = True
    symbol = board[-1][0]
    i = len(board) - 1
    j = 0
    while(i >= 0 and j < len(board)):
        if(board[i][j] != symbol or symbol == None):
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
    if(gameState.getTurnCounter() == 0 or boardIsWin(gameState)): 
        return True
    return False

def getNextPlayerSymbol(gameState):
    '''
    Returns the symbol of the player whose turn occurs immediately after the current one.
    '''
    if(gameState.getTurnCounter() %2 == 1): # current Player is X
        return "O"
    else: # Current Player is O
        return "X"

def getCurrPlayerSymbol(gameState):
    '''
    Returns the symbol of the player who is about to play.
    '''
    if(gameState.getTurnCounter() %2 == 1): # current Player is X
        return "X"
    else: # Current Player is O
        return "O"
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
    isWin = boardIsWin(state)

    # This is the player that is about to play if the state
    # is NOT a terminal state
    currSymbol = getCurrPlayerSymbol(state)

    
    if(isWin and currSymbol == "X"): 
        # If there is a win in board before the X player plays, then the O player wins
        value = -1
    elif(isWin and currSymbol == "O"): # X player wins
        # If there is a win in board before the O player plays, then the X player wins
        value = 1
    elif(isTerminal(state) and not isWin):
        # If there is no win on the board, but it is still a terminal state, then it is a tie
        value = 0
    return value

def legalActions(state):
    '''
    Returns a list of the legal actions available in the current state of the game.
    '''
    legal = []
    nextSymbol = getCurrPlayerSymbol(state)
    board = state.getBoard()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == None):
                legal.append((nextSymbol, i, j))
    return legal


def boardDeepCopy(board):
    '''
    Returns a deep copy of a board (2D array)
    '''
    cpy = []
    i = 0
    for row in board:
        cpy.append([])
        for item in row:
            cpy[i].append(item)
        i += 1
    return cpy

def getSuccessor(state, action):
    symbol, i, j = action
    newBoard = boardDeepCopy(state.getBoard())
    newBoard[i][j] = symbol
    newState = GameState(state.getDimension())
    newState.setBoard(newBoard)
    newState.setTurnCounter(state.getTurnCounter() - 1)
    return newState

def getPlayerMove(state, playerSymbol):
    legalMoves = legalActions(state)
    playerMove = None
    playerToAction = {}
    actionToPlayer = {}
    k = 1
    for i in range(state.getDimension()):
        for j in range(state.getDimension()):
            actionToPlayer[(playerSymbol, i, j)] = str(k)
            playerToAction[str(k)] = (playerSymbol, i, j)
            k += 1
    while(playerMove not in legalMoves):
        print("The available spaces are: ")
        for move in legalMoves:
            print(f"{actionToPlayer[move]}", end=" ")
        selection = input("\nSelect the space you want to place your symbol in using its number (1-9): ")
        playerMove = playerToAction[selection]
        if(playerMove not in legalMoves):
            print("You entered an unavailable or illegal space.")
    return playerMove 

def printBoard(board):
    '''
    Prints the board side by side with an instructive board which has each space numbered.
    '''
    print()
    i = j = 0
    k = 1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] != None and j < len(board[0]) - 1):
                print(board[i][j], end = " | ")
            elif(board[i][j] != None):
                print(board[i][j], end = "\t")
                for _ in range(len(board) - 1):
                    print(f"{k}", end = " | ")
                    k += 1
                print(k)
                k += 1
            elif(board[i][j] == None and j < len(board[0]) - 1):
                print("-", end = " | ")
            else:
                print("-", end = "\t")
                for _ in range(len(board) - 1):
                    print(f"{k}", end = " | ")
                    k += 1
                print(k)
                k += 1
    print()
