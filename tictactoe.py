"""
Tic Tac Toe Player
"""

import math
import copy

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
    X_list = list()
    O_list = list()

    if board == initial_state():
        return X
    else:
        for row in range(len(board)):
            for cell in range(len(board[row])):
                if board[row][cell]==X:
                    X_list.append(X)
                elif board[row][cell]==O:
                    O_list.append(O)
        if len(X_list) > len(O_list):
            return O
        elif len(O_list) == len(X_list):
            return X        
        
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] == None:
                action_set.add((row,cell))
    return action_set
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board
    raise NotImplementedError


def hori_win(board):
    for row in range(len(board)):
        if all(ele==board[row][0] for ele in board[row]):
            return board[row][0]

def main_win(board):
    main_list = list()
    for row in range(len(board)):
        main_list.append(board[row][row])
    if all(ele == main_list[0] for ele in main_list):
            return main_list[0]

def vert_win(board):
    vert_set = set()
    for row in range(len(board)):
        for cell in range(len(board[row])):
            # print(board[cell][row])
            vert_set.add(board[cell][row])
        if len(vert_set)==1:
            return list(vert_set)[0]
        else:
            empty_list = list()
            vert_set = set(empty_list)
            continue

def off_win(board):
    off_list = list()
    for row in range(len(board)):
        for cell in range(len(board)):
            if row+cell==len(board)-1:
                off_list.append(board[row][cell])
    if all(ele==off_list[0] for ele in off_list):
        return off_list[0]
                    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if hori_win(board) != None:
        return hori_win(board)
    elif off_win(board) != None:
        return off_win(board)
    elif main_win(board) != None:
        return main_win(board)
    elif vert_win(board) != None:
        return vert_win(board)
    else:
        return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    check_list = list()
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell]==None:
                pass
            else:
                check_list.append(board[row][cell])

    # if winner(board) == None:
    #     if len(check_list)!=9:
    #         return False
    #     else:
    #         return True
        
    if winner(board) != None:
        return True
    elif len(check_list)==9:
        return True
    else:
        return False
    # if winner(board) or utility(board)==0:
    #     return True
    # else:
    #     return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board)==X:
            return 1
        elif winner(board)==O:
            return -1
        else:
            return 0
    raise NotImplementedError


def max_value(board):
    if terminal(board):
        return utility(board)
    # else:
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v

def min_value(board):
    if terminal(board)==True:
        return utility(board)
    # else:
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    elif player(board)==X:
        x_action = list()
        for action in actions(board):
            # print(action)
            x_action.append(min_value(result(board,action)), )
        return list(actions(board))[x_action.index(max(x_action))]
        # return sorted(x_action, key=lambda x: x[0],reverse=True)[0][1]

    elif player(board)==O:
        o_action = list()
        for action in actions(board):
            # print(action)
            o_action.append(max_value(result(board,action)))
            # o_action.append([max_value(result(board,action)), action])

        return list(actions(board))[o_action.index(min(o_action))] 
        # return sorted(o_action,key=lambda x:x[0])[0][1]         
    raise NotImplementedError
