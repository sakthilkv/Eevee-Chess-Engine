import unittest
from ..core import board
from ..core import move 

class TestChessMoves(unittest.TestCase):

    def test_rook_moves(self):
        # Test 1: Rook at starting position
        board = board.load_fen("initial")
        self.assertEqual(move.rook_moves((7, 0), board), [])  # Rook can't move at initial position

        # Test 2: Rook with clear path
        board = [
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "R", "", "", "", ""],  # Rook at center (4, 3)
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
        ]
        expected_moves = {(3, 3), (2, 3), (1, 3), (0, 3),  # Upwards
                          (5, 3), (6, 3), (7, 3),         # Downwards
                          (4, 2), (4, 1), (4, 0),         # Left
                          (4, 4), (4, 5), (4, 6), (4, 7)} # Right
        self.assertEqual(set(move.rook_moves((4, 3), board)), expected_moves)

        # Test 3: Rook blocked by same-color pieces
        board = [
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "P", "", "", "", ""],  # Same color pawn blocking up
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "R", "", "", "", ""],  # Rook at center (4, 3)
            ["", "", "", "P", "", "", "", ""],  # Same color pawn blocking down
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
        ]
        expected_moves = {(4, 2), (4, 1), (4, 0), (4, 4), (4, 5), (4, 6), (4, 7)}
        self.assertEqual(set(move.rook_moves((4, 3), board)), expected_moves)

        # Test 4: Rook can capture opponent's pieces
        board = [
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "p", "", "", "", ""],  # Opponent pawn blocking up
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "R", "", "", "", ""],  # Rook at center (4, 3)
            ["", "", "", "p", "", "", "", ""],  # Opponent pawn blocking down
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
        ]
        expected_moves = {(1, 3), (4, 2), (4, 1), (4, 0), (4, 4), (4, 5), (4, 6), (4, 7), (5, 3)}
        self.assertEqual(set(move.rook_moves((4, 3), board)), expected_moves)

    def test_bishop_moves(self):
        # Test 1: Bishop at starting position
        board = board.load_fen("initial")
        self.assertEqual(bishop_moves((7, 2), board), [])  # Bishop can't move at initial position

        # Test 2: Bishop with clear path
        board = [
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "B", "", "", "", ""],  # Bishop at center (4, 3)
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
        ]
        expected_moves = {(3, 2), (2, 1), (1, 0),  # NW
                          (5, 2), (6, 1), (7, 0),  # SW
                          (3, 4), (2, 5), (1, 6), (0, 7),  # NE
                          (5, 4), (6, 5), (7, 6)}  # SE
        self.assertEqual(set(bishop_moves((4, 3), board)), expected_moves)

        # Test 3: Bishop blocked by same-color pieces
        board = [
            ["", "", "", "", "", "", "", ""],
            ["", "", "P", "", "", "", "", ""],  # Same color pawn blocking NW
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "B", "", "", "", ""],  # Bishop at center (4, 3)
            ["", "", "", "", "", "", "", ""],
            ["", "", "P", "", "", "", "", ""],  # Same color pawn blocking SW
            ["", "", "", "", "", "", "", ""],
        ]
        expected_moves = {(3, 4), (2, 5), (1, 6), (0, 7), (5, 4), (6, 5), (7, 6)}
        self.assertEqual(set(bishop_moves((4, 3), board)), expected_moves)

        # Test 4: Bishop can capture opponent's pieces
        board = [
            ["", "", "p", "", "", "", "", ""],  # Opponent pawn blocking NW
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "B", "", "", "", ""],  # Bishop at center (4, 3)
            ["", "", "", "", "", "", "", ""],
            ["", "", "p", "", "", "", "", ""],  # Opponent pawn blocking SW
            ["", "", "", "", "", "", "", ""],
        ]
        expected_moves = {(1, 0), (5, 2), (6, 1), (7, 0), (3, 4), (2, 5), (1, 6), (0, 7), (5, 4)}
        self.assertEqual(set(bishop_moves((4, 3), board)), expected_moves)

if __name__ == '__main__':
    unittest.main()
