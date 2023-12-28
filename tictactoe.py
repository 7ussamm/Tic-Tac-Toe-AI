"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cx = 0
    co = 0
    for x in board:
        for y in x:
            if y==X:
                cx+=1
            elif y == O:
                co+=1
    if terminal(board):
        return None
    if cx==co:
        return X
    else:
        return O

            


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for x in range(3):
        for y in range(3):
            if board[x][y]==EMPTY:
                moves.add((x,y))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #if not a valid action
    if action not in actions(board):    
        raise Exception
    #return the resulting board
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check either O or X wins
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2]:
            return board[x][0]
        for y in range(3):
            if board[0][y] == board[1][y] == board[2][y]:
                return board[0][y]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    #if no winner
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if there is a winner
    if winner(board) != None:
        return True
    #if there is an empty cell this means the game is not yet over
    else:
        for x in board:
            for y in x:
                if y==EMPTY:
                    return False
    #if every cell is filled
    return True
        


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board)==X:
            v,move = max_value(board)
            return move
        else:
            v,move = min_value(board)
            return move
def min_value(board):
    v= 10
    move = None
    if terminal(board):
        return utility(board),None
    for action in actions(board):
        cv,cmove = max_value(result(board,action))
        if cv<v:
            v= cv
            move = action
    return v,move
def max_value(board):
    v = -10
    move = None
    if terminal(board):
        return utility(board),None
    #to choose first move quick when its the start of the game
    if board == initial_state():
        return 0,(1,1)

    for action in actions(board):
        cv,cmove = min_value(result(board,action))
        if cv>v:
            v = cv
            move = action
    return v,move