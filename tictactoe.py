"""
Tic Tac Toe Player
"""

import math
import sys
import copy
sys.setrecursionlimit(10000)
X = "X"
O = "O"
LIMIT = 100
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
    empty = all([True if board[i][j] == None else False for i in range(3) for j in range(3)])
    if empty:
        return X
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X :
                x += 1 
            elif board[i][j] == O:
                o += 1        
    if x <= o :
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibility = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibility.add((i,j))
    return possibility


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    p = player(board)
    board_c = copy.deepcopy(board)
    board_c[action[0]][action[1]] = p
    return board_c


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_value = 1
    o_value = -1
    values = []
    d1 = 0
    d2 = 0
    for i in range(3):
        temp_r = 0
        temp_c = 0
        for j in range(3):
            value_r = x_value if board[i][j] == X else o_value if board[i][j] == O else 0
            value_c = x_value if board[j][i] == X else o_value if board[j][i] == O else 0
            temp_r += value_r
            temp_c += value_c
            if (i,j) == (0,0):
                d1 += value_r            
            elif (i,j) == (1,1):
                d1 += value_r
                d2 += value_r
            elif (i,j) == (2,2):
                d1 += value_r
            elif (i,j) == (0,2):
                d2 += value_r
            elif (i,j) == (2,0):
                d2 += value_r
        
        values.append(temp_r)
        values.append(temp_c) 
        values.append(d1)
        values.append(d2)
    if max(values) == 3:
        return X
    elif min(values) == -3:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win is not None or not actions(board):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    util = 1 if win == X else -1 if win == O else 0
    return util
def minvalue(board,v ):
    if terminal(board) :
        return utility(board)
    value = float('inf')
    for action in actions(board):
        newvalue = maxvalue(result(board,action),value)
        if newvalue > v:
            return newvalue
        value = min(value,newvalue)
    return value
def maxvalue(board ,v ):
    if terminal(board)  :
        return utility(board)
    value = float('-inf') 
    for action in actions(board):
        newvalue = minvalue(result(board,action),value)
        if newvalue < v:
            return value
        value = max(value,newvalue)
    return value
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == initial_state():
        return (1,1)
    if terminal(board):
        return None
    possible = actions(board)
    index = 0
    c = 0
    value = -9999999
    for i in possible:
        temp = maxvalue(result(board,i),value)
        if temp > value:
            value = temp
            index = c
        c += 1
    c = 0
    for i in possible:
        if c == index:
            return i
        c += 1
