import random


class Sudoku:
    """
    A class representing a Sudoku puzzle.

    Attributes:
        DIFFICULTY (dict): A dictionary mapping difficulty levels to the number of cells to remove.
        board (list): A 2D list representing the Sudoku board.
        difficulty (str): The difficulty level of the Sudoku puzzle.

    Methods:
        __init__(self, difficulty="Medium"): Initializes a Sudoku object
        sudoku_status(self): Checks the status of the Sudoku puzzle (complete or incomplete).
        solve_sudoku(self): Solves the Sudoku puzzle using backtracking.
    """

    __DIFFICULTY = {"Easy": 40, "Medium": 28, "Hard": 17}

    def __init__(self, difficulty="Medium"):
        """
        Initializes a Sudoku object with the specified difficulty level.

        Args:
            difficulty (str, optional): The difficulty of the Sudoku puzzle
        """
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.difficulty = difficulty
        self._generate_sudoku()

    def _generate_sudoku(self):
        """
        Generates a Sudoku puzzle by solving a puzzle then removes cells based on difficulty.
        """
        self.solve_sudoku()
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers)

        # Fill the board with the shuffled numbers
        for row in range(9):
            for col in range(9):
                self.board[row][col] = numbers[(row * 3 + row // 3 + col) % 9]

        # Remove numbers based on difficulty
        total_cells = 81
        num_to_remove = total_cells - self.__DIFFICULTY[self.difficulty]
        while num_to_remove > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                num_to_remove -= 1

    def sudoku_status(self):
        """
        Returns the completion percentage of the Sudoku Puzzle.

        Returns:
            float: The completion percentage of the Sudoku puzzle.
        """
        total_cells = 81
        filled_cells = sum(cell != 0 for row in self.board for cell in row)
        percentage = (filled_cells / total_cells) * 100
        return percentage

    def __is_safe(self, row, col, num):
        """
        Checks if it is safe to place a number in a specific cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            num (int): The number to be placed in the cell.

        Returns:
            bool: True if it is safe to place the number, False otherwise.
        """
        # Check the row
        for x in range(9):
            if self.board[row][x] == num:
                return False

        # Check the column
        for x in range(9):
            if self.board[x][col] == num:
                return False

        # Check the 3x3 grid
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve_sudoku(self):
        """
        Solves the generated Sudoku puzzle using backtracking.

        Returns:
            bool: True if the puzzle is solvable, False otherwise.
        """
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.__is_safe(row, col, num):
                            self.board[row][col] = num
                            if self.solve_sudoku():
                                return self.board
                            self.board[row][col] = 0
                    return False
        return True


class KillerSudoku(Sudoku):
    """
    A class representing a killer sudoku puzzle variant

    Attributes:
        normal_sudoku: An instance of regular sudoku. Used for board generation.
        empty_board (list): A 2D list representing the Sudoku board to be presented to user.
        difficulty (str): The difficulty level of the Sudoku puzzle. (Easy, Medium, Hard)
        cages (dict): Contains all the cages. Their sum and the cells pertaining to that sum.
        solved_board (list): Contains all the answers to the board.



    Methods:
        __init__(self, difficulty="Medium"): Initializes a Killer Sudoku object
        _is_cage_valid(self): Checks the validity of the cages and checks their sum.
        solve_killer_sudoku(self): Fills the board up with answers.
    """

    def __init__(self, difficulty="Medium"):
        """
        Initializes a KillerSudoku object with the specified difficulty level.

        Args:
            difficulty (str, optional): The difficulty of the KillerSudoku puzzle
        """
        super().__init__(difficulty)
        temp = [row[:] for row in self.board]
        self.solve_sudoku()
        self.solved_board = [row[:] for row in self.board]
        self.board = temp
        self.cages = {}
        self._generate_cages()

    def _generate_cages(self):
        """
        Generates cages for the puzzle. A cage is a group of cells randomly clustered
        together with a specific sum. They are adjacent to each other no wraping
        """
        all_cells = [(row, col) for row in range(9) for col in range(9)]
        random.shuffle(all_cells)
        visited = set()
        cage_id = 1

        # Iterate over each cell
        for start_cell in all_cells:
            if start_cell not in visited:
                current_cage = []
                cells_to_visit = [start_cell]
                cells_in_cage = random.randint(2, 5)

                while cells_to_visit and len(current_cage) < cells_in_cage:
                    cell = cells_to_visit.pop()
                    if cell not in visited:
                        current_cage.append(cell)
                        visited.add(cell)
                        # aadd adjacent cells to the visit list
                        row, col = cell
                        possible_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                        random.shuffle(possible_directions)
                        for d_row, d_col in possible_directions:
                            adj_cell = (row + d_row, col + d_col)
                            if (
                                (0 <= adj_cell[0] < 9)
                                and (0 <= adj_cell[1] < 9)
                                and (adj_cell not in visited)
                            ):
                                cells_to_visit.append(adj_cell)
                # find de sum of the numbers in the cage using the solved board
                if current_cage:
                    cage_sum = sum(
                        self.solved_board[row][col] for row, col in current_cage
                    )
                    self.cages[cage_id] = {"sum": cage_sum, "cells": current_cage}
                    cage_id += 1

    def _is_cage_valid(self, cage_id):
        """
        Checks the sum of the specifiend cage, and compare that to cage dictionary.

        Args:
            cage_id (int): The specified ID for the cage of interest.

        Returns:
            bool: Returns true if the sum is true when compared to answer.
        """
        cage = self.cages[cage_id]
        cage_sum = sum(self.solved_board[row][col] for row, col in cage["cells"])
        return cage_sum == cage["sum"]

    def sudoku_status(self):
        """
        Returns the completion status of the Killer Sudoku Puzzle.

        Returns:
            float: The completion percentage of the Sudoku puzzle.
        """
        filled_percentage = super().sudoku_status()

        # If all cages aren't valid, return 0
        all_cages_valid = all(self._is_cage_valid(cage_id) for cage_id in self.cages)
        return filled_percentage if all_cages_valid else 0.0
