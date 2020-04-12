#!/usr/bin/env python3.7
from game_board import GameBoard

# ask the user for a board_size and a level 
board_size = input('Welcome to Minesweeper!\n  Please choose a board size: SMALL, MEDIUM, LARGE: ').upper()
level = input('Please choose a level: NOVICE, INTERMEDIATE, EXPERT: ').upper()

# create a game board
game_board = GameBoard(board_size=board_size, level=level)
game_board.render_board()

# Game Loop
while not game_board.is_winner():
    try:
        target_row = int(input('Enter a valid Row number: ')) - 1
        target_col = int(input('Enter a valid Column number: ')) - 1

        if not game_board.is_valid_cell(target_row, target_col):
            print('C''mon, Man.  Enter a valid cell: ')
            continue
    except:
        print('C''mon, Man.  Enter a valid cell: ')
        continue

    # check if the user chose a cell containing a mine
    if game_board.is_mine(target_row, target_col):
        game_board.render_board(game_over=True)
        print('\nYou lose! Thanks for playing.\n')
        break
    elif game_board.is_winner():
        game_board.render_board(game_over=True)
        print('\nAgainst all odds, you have won!\n')
    else:
        game_board.render_board()