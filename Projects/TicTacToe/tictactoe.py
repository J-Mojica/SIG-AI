
board = [ [ None for _ in range(3)] for _ in range(3)]
print(board)

# TODO: Create a game state class with the necessary functions
# TODO: getSuccessors getValue (for terminal states)

def max_value(gameState):
    '''
    Doc goes here
    '''
    if(isTerminal(gameState)):
        return gameState.getValue()
    v = float("-inf")
    for successor in gameState.getSuccessors():
        v = max(v, min_value(successor))

def min_value(gameState):
    if(isTerminal(gameState)):
        return gameState.getValue()
    v = float("inf")
    for successor in gameState.getSuccessors():
        v = min(v, max_value(successor))