"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    x_counter = 0
    o_counter = 0
    for row in board:
        for cell in row:
            if cell == "X":
                x_counter += 1
            elif cell == "O":
                o_counter += 1

    if x_counter > o_counter:
        return 'O'
    else:
        return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                possible_actions.append([i, j])

    return tuple(possible_actions)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not action:
        return board
    if board[ action[0] ][ action[1] ]:
        raise Exception

    result_board = copy.deepcopy(board)
    result_board[ action[0] ][ action[1] ] = player(board)
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0,3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]

    for j in range(0,3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[0][j]:
            return board[0][j]

    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0]:
        return board[0][0]

    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[1][1]:
        return board[1][1]


    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        for row in board:
            for cell in row:
                if not cell:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_result = winner(board)

    if game_result == X:
        return 1
    elif game_result == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # actually not a AI play but start with the center square is a good play and saves a lot of time
    if not board[1][1]:
        return [1,1]
    action = aux_minimax(board)[1]
    if action:
        return action
    else:
        return None



def aux_minimax(board, action = []):
    """
    Auxiliary function to do the minimax work correctly
    """
    #the first call of this function does not take the action argument
    if action:
        new_board = result(board, action)
    else:
        new_board = copy.deepcopy(board)

    # the stop condition is if the action taken on the board is a terminal board
    if terminal(new_board):
        # utility indicates who is the winner or if it's a draw
        value = utility(new_board)
        return [value, action, value]

    player_of_round = player(new_board)
    possible_actions = actions(new_board)

    plays = []

    # this for creates list of plays with an utility value to make minimax work
    for action in possible_actions:
        plays.append(aux_minimax(new_board, action))
        plays[-1][1] = action
    best_play = copy.deepcopy(plays[0])

    for play in plays:
        # test each play to verify which is the best one
        if player_of_round == X:
            if best_play[0] <= play[0]:
                best_play = copy.deepcopy(play)
        else:
            if best_play[0] >= play[0]:
                best_play = copy.deepcopy(play)

    return best_play
