'''
This file contains the functions that make up a minimax agent for a two player game
'''
def maxValue(game, gameState, alpha, beta):
    '''
    Returns a tuple (value, action) representing the action with the maximum value
    in the current state of the game.
    '''
    if(game.isTerminal(gameState)):
        return game.getValue(gameState), None
    v = float("-inf")
    action = None

    for a in game.legalActions(gameState):
        successor = game.getSuccessor(gameState, a)
        v2, a2 = minValue(game, successor, alpha, beta)
        if(v2 > v):
            v = v2
            action = a
            alpha = max(alpha, v)
        if(v >= beta):
            return v, action
    
    return v, action

def minValue(game, gameState, alpha, beta):
    '''
    Returns a tuple (value, action) representing the action with the minimum value
    in the current state of the game.
    '''
    if(game.isTerminal(gameState)):
        return game.getValue(gameState), None
    v = float("inf")
    for a in game.legalActions(gameState):
        successor = game.getSuccessor(gameState, a)
        v2, a2 = maxValue(game, successor, alpha, beta)
        if(v2 < v):
            v = v2
            action = a
            beta = min(beta, v)
        if(v <= alpha):
            return v, action
    
    return v, action

def computeNextAction(game, gameState, player):
    '''
    Main interface between the agent and the game.
    Calculates the agent's next action based on if it is
    the minimizer player or the maximizer player.
    '''
    value = None
    action = None
    if(player == 'max'): 
        # agent is the maximizer player
        value, action = maxValue(game, gameState, float("-inf"), float("inf"))
    else: 
        # agent is the minimizer player
        value, action = minValue(game, gameState, float("-inf"), float("inf"))
    print(f"AI Action: {action}, Value: {value}") # Prints the action of choice along with its value
    return action
