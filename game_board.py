import random
import os 


class GameBoard():

    # number of rows and columns on the board
    SIZES = {
        'SMALL': 4,
        'MEDIUM': 8,
        'LARGE': 12
    }

    # % of squares that will contain mines
    LEVELS = {
        'NOVICE': .15,
        'INTERMEDIATE': .25,
        'EXPERT': .35
    }

    # default board size
    SIZE = SIZES['SMALL']
    LEVEL = LEVELS['NOVICE']

    # list of lists containing mine locations and list of lists of containing what the user sees
    MINES = None
    USER_BOARD = None

    MINE_MARKER = '*'
    NON_MINE_MARKER = '-'


    def __init__(self, board_size, level):
        """
        Set up the game board.  If the user doesn't provide an appropriate board_size or level
        then they default to 'SMALL' and 'NOVICE' respectively.
        """
        GameBoard.SIZE = GameBoard.SIZES.get(board_size, GameBoard.SIZE)
        GameBoard.LEVEL = GameBoard.LEVELS.get(level, GameBoard.LEVEL) 
        
        # create a list of lists with board_size as the number of lists to represent the game_board
        GameBoard.MINES = [[] for _ in range(GameBoard.SIZE)]
        GameBoard.USER_BOARD = [[] for _ in range(GameBoard.SIZE)]
        
        # initialize a blank game board
        for row in GameBoard.USER_BOARD:
            for _ in range(GameBoard.SIZE):
                row.append(GameBoard.NON_MINE_MARKER)

        # lay mines according to the level chosen from LEVELS
        for row in GameBoard.MINES:
            for _ in range(GameBoard.SIZE):
                row.append(GameBoard.MINE_MARKER if random.random() <= GameBoard.LEVEL else self.NON_MINE_MARKER)


    def render_board(self, game_over=False):
        """
        Print the current state of the game board to the console
        """
        os.system('clear')
        print(f"\n{self.SIZE * '-'} Game Board {self.SIZE * '-'}\n")
        for row in self.USER_BOARD:
            print(row)

        if game_over:
            print(f"\n{self.SIZE * '-'} Mine Locations {self.SIZE * '-'}\n")
            for row in self.MINES:
                print(row)


    def is_valid_cell(self, target_row, target_col):
        """
        Check that the user input is a valid cell.
        """
        return ((target_row >= 0) and (target_row < self.SIZE) and (target_col >= 0) and (target_col < self.SIZE))


    def check_adjacent_cells(self, target_row, target_col):
        """
        Checks if any cells adjacent to target_cell contain mines and updates target_cell in USER_BOARD
        with the count of such cells
        """
        # positions of adjacent cells relative to target_cell
        adjacent_cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        mine_cnt = 0
        for adjacent_cell in adjacent_cells:
            row = target_row + adjacent_cell[0]
            col = target_col + adjacent_cell[1]
            
            if self.is_valid_cell(row, col) and self.MINES[row][col] == self.MINE_MARKER:
                mine_cnt += 1

        self.USER_BOARD[target_row][target_col] = str(mine_cnt)


    def is_mine(self, target_row, target_col):
        if self.MINES[target_row][target_col] == self.MINE_MARKER:
            self.USER_BOARD[target_row][target_col] = self.MINE_MARKER

            return True
        else:
            self.check_adjacent_cells(target_row, target_col)


    def is_winner(self):
        is_winner = True

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                # if we have any cell that isn't uncovered AND it's not a MINE then the game isn't over
                if (self.USER_BOARD[i][j] == self.NON_MINE_MARKER) and not (self.MINES[i][j] == self.MINE_MARKER):
                    is_winner = False

        return is_winner