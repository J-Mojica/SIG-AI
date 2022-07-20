# SIG-AI TicTacToe AI project

This is the first project of NJIT ACM's SIG-AI. An implementation of an adversarial search agent which uses the minimax algorithm and alpha-beta pruning, one of the various 
topics we looked at during the Spring 2022 semester.

This project was developed as a demonstration of how to implement an AI from some of the theory we discussed during club meetings and is intended as an introduction for people who are new to AI. Most of it was done during club meetings in sessions of 1-2 hours, and later improved and cleaned up.

# How to play against the AI
First you need to have python installed on your device. Then download the files in this folder and, using your terminal navigate to the folder where you saved the files, and
run the [tictactoe.py](./tictactoe.py) program by entering the following command on your terminal:

```
python tictactoe.py
```

This is the main program. It contains the logic to manage the game between the AI and the player. 
In this case the AI is a [minimax](https://en.wikipedia.org/wiki/Minimax) agent, but it could potentially be replaced by a different 
type of agent. The agent algorithm also uses [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) to optimize the minimax search.

# How to make an AI of this type, step by step

## 1. Define the State Space:

The state space is the set of all states of the game. So, we need to define what a "state" is in our game. Depending on what game are you dealing with, the state of such game will be defined by different things. For example, the game
state of chess can be defined by the positions of the pieces on the board, which player is next to move, and how much time does each player have on their clock. Meanwhile, connect four can be defined by the state of the board and who is the next player to move. 

Choose what features of the game are relevant for your purposes and figure out a way of representing it in code. In general, you want to define the game state in a way that is convenient but also kept as small as possible in size. This is because the AI will be generating a great amount of game states when calculating their actions, hence, to save as much space as possible, you want to minimize the size of what a game state is. As tempting as it may be to pack as much information as you can into the game state, you must think carefully if the benefit you get from doing this is worth the space you will be using. This same principle applies to the way you define what an action is. 

In our case we defined the game state to be the board (a two-dimensional list), a turn counter (an integer), and a "dimension" variable (an integer) which represents the dimensions of the board and serves to define the turn counter. We could save more space by using a one-dimensional list and getting rid of the turn counter entirely, however since Tic Tac Toe is a very small and simple game we can afford to use little more space in order to make everything more convenient to work with and easier to understand. Formally, we can define our state space $S$ in the following manner:

$$
S = \\{(B,t,d)\\} 
$$ 

Where $t \in \mathbb{Z}^+$, $d \in \\{2^n + 1 \mid n \in \mathbb{N}\\}$,  $0 \leq t \leq d^2$, and $B$ is a $d \times d$ list of strings $\in \\{ \text{"X", "O"}, \epsilon \\}$ where $\epsilon$ is the empty string.

(You dont have to define it so rigurously, all you really need for implementation purposes is decide how to define it in your code. I am just trying to be thorough)

Clarification:
- $\mathbb{Z}^+ = \mathbb{N} \cup \\{0\\}$
- We define $d$ to be an odd number greater than three so the board has a center space and it's not a single space board.
## 2. Define the Action Space:

The action space is the set of all actions in the game. So we first define what an action is. As mentioned before, the same principle explained for the game state applies when defining what an action (a.k.a. operator or move) is: you want to define the actions in a way that is convenient using as little space as possible. What is "convenient" is often dependent on how you defined your state space and in the nature of the game. 

In our case, since we defined our board to be a two-dimensional list and to take an action (make a move) in Tic Tac Toe you must place your corresponding symbol in an empty space on the board, we defined an action as a 3-tuple $(w, i, j)$. The 3-tuple contains a string $w$ representing the symbol to be placed, and two integers $i$ and $j$ which are the indexes of where to place the symbol $w$ on the board (a two-dimensional list). Hence, we can formally define our action space $A$ in the following manner:

$$
A = \\{(w, i, j)\\}
$$

Where $w \in \\{X, O, \epsilon \\}$, $\epsilon$ representing the empty string, $i,j \in \mathbb{Z}^{+}$ and $0 \leq i,j \leq d-1$

## 3. Create functions to extract information from the game and to allow the AI to interact with it:

First you must have a game for the AI to play (duh!). So either you have to create the game from scratch or figure out a way to extract the necessary information from an existing game. This could be through using tecniques of computer vision, or hacking into the game code, or through an API provided by the game itself, etc. Whatever way you do it, it is necessary that you are able to translate the state of the game into something that the AI can use. In the case of this type of agent (minimax search) the functions we need are mentioned below.


### Creating the game from scratch:

The file [tictactoeGame.py](./tictactoeGame.py) contains the `GameState` class along with all functions necessary to
play the game and to extract all necessary information about the state of the game. If needed, more detailed explanation about all the functions implemented in this file is either found on the comments in the code or the code itself is self explanatory.

The Game State class is a wrapper for a tictactoe board (represented by a 2D list)
along with a turn counter.

This file contains all the functions necessary for the AI to extract 
information about the game. Namely:
- `isTerminal(gameState: GameState) -> bool`: A function to tell whether a game state is a terminal state or not.
- `getValue(state: GameState) -> float`: A function that returns the value of a given game state. 
- `legalActions(state: GameState) -> List`: A function to obtain a list of the legal actions in any given state.
- `getSuccessor(state: GameState, action) -> GameState`: A function that given a game state and an action 
returns a new game state which is the result of taking said action in said game state (i.e the successor of that state).

### Putting it formally
Formally, we need to define and differentiate the set of terminal states $S_T \in S$ and the set of non-terminal states $S_N \in S$, we also need to define a value function $V$, and we need to define a transition function $T$.

Terminal and Non-terminal States definitions:

$$
S_T = \\{(B,t,d) \in S \mid t=0 \text{ or there is a win on the board} \\}
$$

$$
S_N = S - S_T = \\{(B,t,d) \in S \mid t > 0 \text{ and there is no win on the board}\\}
$$

Hence, the `isTerminal` function is just a way for us to test the membership of state to the set $S_T$. The set $S_T$ is not explicitly defined in the code because that is not feasible nor practical in any way, so to test if a state is a member of $S_T$ we instead check if the state meets the rules of a terminal state as defined above.

We define a value only for terminal states since these are the only ones where there is a clear outcome for the AI. Thus, we define the value function as follows: 

$$
V: S_T \to \mathbb{R}
$$

$$
V(s_T) = \begin{cases}
        1 \quad \text{if "X" wins}\\
        0 \quad \text{if there is a tie}\\
        -1 \quad \text{if "O" wins}\\
    \end{cases}
$$

This is exactly the `getValue` function in the implementation.

We can only transition from a non-terminal state. Hence the input to our transition function $T$ must be an element in $S_N$:

$$
T: S_{N},A \to S
$$

$$
T(s_{N},a) = T ((B,t,d), (w,i,j)) = (B_{new}, t-1, d)
$$

Where $B_{new}[x][y] = B[x][y] \forall x,y$ except for  when $x = i, y = j$, in which case $B_{new}[i][j] = w$ and $B[i][j] = \epsilon$ (the empty string). If $B[i][j] \neq \epsilon$ then this function is undefined.

This is what the `getSuccessor` function implements. Wherever the function is undefined, the `getSuccessor` function returns `None`.

With this, the agent implicitly defines a value function for non-terminal states (and by consequence the actions that lead to them) in the following way:

$$
V_{AI}: S \to \mathbb{R}
$$

$$
V_{AI}(s) = \begin{cases}
            V(s) \quad \text{if } s \in S_T\\
            \max_{a} ( V_{AI} (T(s,a))) \quad \text{if } s \in S_N \text{ and its the maximizer player's turn}\\
            \min_{a}(V_{AI} (T(s,a))) \quad \text{if } s \in S_N \text{ and its the minimizer player's turn}\\
        \end{cases}
$$

This is what the functions defined in the [minimaxAgent.py](./minimaxAgent.py) file implement.

Once this is done, all that is left to do (if it hadn't been done before or while developing the AI) is to make a way for the AI to interface with the game and the user, which is what the [tictactoe.py](./tictactoe.py) file implements. One can also add further improvements on the the AI using such as [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) once we have a working agent. Alpha-beta pruning, in short, is a way to discard undesireable branches of the minimax search tree without having to fully explore them. This can save some computation time. Alpha-beta pruning was also implemented on the agent's code.
