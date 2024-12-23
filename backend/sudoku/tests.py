from django.test import TestCase
from .models import Users
from .sudoku import Sudoku, KillerSudoku
from rest_framework.test import APITestCase
from .serializers import UsersSerializer, BoardSerializer
import json


class UserModelTests(TestCase):
    def test_add_single_user(self):
        # Adding a single user to the database
        user = Users.objects.create(
            id="testuser", pwd="testpassword", email="test@gmail.com"
        )
        self.assertIsNotNone(user.pk)
        user.delete()

    def test_delete_single_user(self):
        # Deleting a single user from the database
        user = Users.objects.create(
            id="deleteuser", pwd="password", email="delete@gmail.com"
        )
        user_id = user.pk
        user.delete()
        self.assertFalse(Users.objects.filter(pk=user_id).exists())

    def test_add_two_users(self):
        # Adding two users to the database
        Users.objects.create(id="user1", pwd="pass1", email="user1@gmail.com")
        Users.objects.create(id="user2", pwd="pass2", email="user2@gmail.com")
        self.assertEqual(Users.objects.count(), 2)

    def test_modify_user_password(self):
        # Modify a user's password
        Users.objects.create(id="modifyuser", pwd="oldpassword", email="mod@gmail.com")
        Users.objects.filter(id="modifyuser").update(pwd="newpassword")
        self.assertEqual(Users.objects.get(id="modifyuser").pwd, "newpassword")

    def test_modify_user_email(self):
        # Modify a user's email
        Users.objects.create(id="emailuser", pwd="password", email="old@gmail.com")
        Users.objects.filter(id="emailuser").update(email="new@gmail.com")
        self.assertEqual(Users.objects.get(id="emailuser").email, "new@gmail.com")


class SudokuAlgoTests(TestCase):
    def test_sudoku_status(self):
        # Check the sudoku_status for a completed board
        sudoku = Sudoku()
        completed_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]
        sudoku.board = completed_board
        self.assertTrue(sudoku.sudoku_status() == 100.0)

        # Check for an incomplete board
        incomplete_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 0, 7, 9],
        ]
        sudoku.board = incomplete_board
        self.assertFalse(sudoku.sudoku_status() == 100.0)

    def test_solve_sudoku(self):
        # Check that the solution is a valid
        sudoku = Sudoku()
        test_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
        sudoku.board = test_board
        self.assertTrue(sudoku.solve_sudoku())

    def test_valid_board_solution(self):
        # Check that each col and row has 9 nums (sets) ie unique
        sudoku = Sudoku()
        solution = sudoku.solve_sudoku()
        for i in range(9):
            row = solution[i]
            column = []
            for j in range(9):
                element = solution[j][i]
                column.append(element)
            self.assertTrue(len(set(row)) == 9)
            self.assertTrue(len(set(column)) == 9)

    def test_generated_board_solution_validity(self):
        # Test out creation and solution and see each part is a set
        sudoku = Sudoku("Easy")
        sudoku._generate_sudoku()
        solution = sudoku.solve_sudoku()
        for i in range(9):
            row = solution[i]
            column = []
            for j in range(9):
                element = solution[j][i]
                column.append(element)
            self.assertTrue(len(set(row)) == 9)
            self.assertTrue(len(set(column)) == 9)

    def test_difficulty_setting_initialization(self):
        # Test difficulty setting
        for difficulty in ["Easy", "Medium", "Hard"]:
            sudoku = Sudoku(difficulty=difficulty)
            self.assertEqual(sudoku.difficulty, difficulty)

    def test_board_initialization_easy(self):
        # Test easy with correct number of blanks
        sudoku = Sudoku("Easy")
        total_zeros = sum(cell == 0 for row in sudoku.board for cell in row)
        self.assertEqual(total_zeros, 41)

    def test_board_initialization_med(self):
        # Test med with correct number of blanks
        sudoku = Sudoku("Medium")
        total_zeros = sum(cell == 0 for row in sudoku.board for cell in row)
        self.assertEqual(total_zeros, 53)

    def test_board_initialization_hard(self):
        # Test hard with correct number of blanks
        sudoku = Sudoku("Easy")
        total_zeros = sum(cell == 0 for row in sudoku.board for cell in row)
        self.assertEqual(total_zeros, 41)

    def test_edge_case_solve(self):
        # Test solve on a nearly finished board
        sudoku = Sudoku()
        sudoku.solve_sudoku()
        solved = sudoku.board
        solved[0][0] = 0
        sudoku.board = solved
        sudoku.solve_sudoku()
        self.assertEqual(sudoku.solve_sudoku(), True)

    def test_status_edge_case(self):
        # test correct status when only one cell is empty
        sudoku = Sudoku()
        sudoku.solve_sudoku()
        solved = sudoku.board
        solved[0][0] = 0
        sudoku.board = solved
        self.assertTrue(sudoku.sudoku_status() > 98)

    def test_imposible_board(self):
        # Test an impossible board
        sudoku = Sudoku()
        sudoku.board[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        sudoku.board[1] = [2, 2, 2, 2, 2, 2, 2, 2, 2]
        self.assertFalse(sudoku.solve_sudoku())


class KillerSudokuAlgoTests(TestCase):
    def test_killer_sudoku_init(self):
        killer_sudoku = KillerSudoku("Easy")
        self.assertEqual(len(killer_sudoku.board), 9)
        self.assertEqual(killer_sudoku.difficulty, "Easy")

    def test_killer_sudoku_status(self):
        killer_sudoku = KillerSudoku("Easy")
        status = killer_sudoku.sudoku_status()
        self.assertTrue(0 <= status <= 100)

    def test_solve_killer_sudoku(self):
        killer_sudoku = KillerSudoku("Easy")
        result = killer_sudoku.solve_sudoku()
        self.assertTrue(result)

    def test_is_cage_valid(self):
        killer_sudoku = KillerSudoku("Easy")
        for cage_id in killer_sudoku.cages:
            self.assertTrue(killer_sudoku._is_cage_valid(cage_id))

    def test_generate_killer_sudoku(self):
        killer_sudoku = KillerSudoku("Easy")
        killer_sudoku._generate_sudoku()
        self.assertEqual(len(killer_sudoku.board), 9)

    def test_difficulty_setting_initialization(self):
        for difficulty in ["Easy", "Medium", "Hard"]:
            killer_sudoku = KillerSudoku(difficulty=difficulty)
            self.assertEqual(killer_sudoku.difficulty, difficulty)

    def test_cage_composition(self):
        killer_sudoku = KillerSudoku("Medium")
        all_cells = set()
        for cage in killer_sudoku.cages.values():
            cage_cells = set(cage["cells"])
            self.assertTrue(all_cells.isdisjoint(cage_cells))
            all_cells.update(cage_cells)

    def test_cage_sum_integrity(self):
        killer_sudoku = KillerSudoku("Medium")
        for cage_id, cage in killer_sudoku.cages.items():
            expected_sum = cage["sum"]
            actual_sum = sum(
                killer_sudoku.solved_board[row][col] for row, col in cage["cells"]
            )
            self.assertEqual(expected_sum, actual_sum)

    def test_serialization(self):
        killer_sudoku = KillerSudoku("Medium")
        serialized = json.dumps(killer_sudoku.board)
        deserialized = json.loads(serialized)
        self.assertEqual(killer_sudoku.board, deserialized)

    def test_status_over_time(self):
        killer_sudoku = KillerSudoku("Easy")
        status_old = killer_sudoku.sudoku_status()
        killer_sudoku.solve_sudoku()
        self.assertFalse(status_old == killer_sudoku.sudoku_status())

    def test_killer_sudoku_solution(self):
        killer_sudoku = KillerSudoku("Easy")
        killer_sudoku.board = [
            [1, 1, 1, 9, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 4, 0, 0, 0, 0],
            [6, 0, 0, 0, 0, 1, 0, 5, 0],
            [0, 0, 0, 0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 7, 0, 9],
            [0, 0, 0, 0, 1, 0, 0, 2, 6],
            [0, 0, 0, 2, 0, 0, 0, 3, 0],
            [2, 0, 0, 0, 0, 0, 0, 9, 0],
            [0, 0, 0, 0, 0, 5, 0, 0, 4],
        ]
        self.assertFalse(killer_sudoku.solve_sudoku())

    def test_rules_enforcement_within_cages(self):
        killer_sudoku = KillerSudoku("Easy")
        cage_change = killer_sudoku.cages
        set_add = (0, 0)
        cage_change[1]["cells"].append(set_add)
        killer_sudoku.cages = cage_change
        self.assertFalse(killer_sudoku._is_cage_valid(1))


class UsersSerializerTest(APITestCase):
    def setUp(self):
        self.user_attributes = {
            "id": "testuser",
            "pwd": "testpassword",
            "email": "test@gmail.com",
        }
        self.serializer = UsersSerializer(data=self.user_attributes)

    def test_serializer(self):
        self.assertTrue(self.serializer.is_valid())
        user = self.serializer.save()
        self.assertEqual(user.id, self.user_attributes["id"])
        self.assertEqual(user.email, self.user_attributes["email"])


class BoardSerializerTest(APITestCase):
    def setUp(self):
        self.user_attributes = {
            "id": "testuser",
            "pwd": "testpassword",
            "email": "test@gmail.com",
        }
        self.user = Users.objects.create(**self.user_attributes)
        self.board_attributes = {
            "id": 1,
            "state": "state",
            "answer": "answer",
            "initial": "initial",
            "difficulty": "Easy",
            "style": "Classic",
            "user": self.user.id,
            "isFinished": False,
        }
        self.serializer = BoardSerializer(data=self.board_attributes)

    def test_serializer(self):
        self.assertTrue(self.serializer.is_valid())
        board = self.serializer.save()
        self.assertEqual(board.id, self.board_attributes["id"])
        self.assertEqual(board.state, self.board_attributes["state"])
        self.assertEqual(board.answer, self.board_attributes["answer"])
        self.assertEqual(board.initial, self.board_attributes["initial"])
        self.assertEqual(board.difficulty, self.board_attributes["difficulty"])
        self.assertEqual(board.style, self.board_attributes["style"])
        self.assertEqual(board.user, self.user_attributes["id"])
        self.assertEqual(board.isFinished, self.board_attributes["isFinished"])
