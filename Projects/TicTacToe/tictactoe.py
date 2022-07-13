import tictactoeGame as game
import minimaxAgent as AI

def tictactoe(player, dimension):
    gameState = game.GameState(dimension)

    while(not game.isTerminal(gameState)):
        move = None
        turnNumber = gameState.getTurnCounter()
        game.printBoard(gameState.getBoard())


        if(turnNumber % 2 == 1): # X turn
            if(player == "X"):
                move = game.getPlayerMove(gameState, "X")
            else:
                move = AI.computeNextAction(game, gameState, "max")
        elif(turnNumber % 2 == 0): # O turn
            if(player == "O"):
                move = game.getPlayerMove(gameState, "O")
            else:
                move = AI.computeNextAction(game, gameState, "min")
        
        gameState = game.getSuccessor(gameState, move)

    game.printBoard(gameState.getBoard())
    val = game.getValue(gameState)

    if(val == 1):
        print("X wins!")
    elif(val == -1):
        print("O wins!")
    else:
        print("No one wins. Can't beat the AI :P")

def main():

    selection = None
    dimension = 3
    while(selection != "X" and selection != "O"):
        selection = input("Enter which symbol do you want to play as (X/O) (q to quit): ").upper()
        if (selection == "Q"):
            return
        elif(selection != "X" and selection != "O"):
            print("You entered an invalid symbol. Try again.")
    tictactoe(selection, dimension)

if(__name__ == "__main__"):
    main()