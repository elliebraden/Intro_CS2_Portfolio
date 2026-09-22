# Author: Ellen Braden
# GitHub username: elliebraden
# Date: 3/13/26
# Description: Unit Tests for the AnimalGame.py program


import unittest
from AnimalGame import *

class TestGetMethods(unittest.TestCase):
    """Tests for the get methods within the AnimalGame.py program file."""

    def setUp(self):
        """Creation of various piece objects to test the get methods"""
        self.pika1 = Pika('TP1', 'tan', 'a1')
        self.pika2 = Pika('TP2', 'tan', 'g1')
        self.pika3 = Pika('AP1', 'ame', 'a7')
        self.pika4 = Pika('AP2', 'ame', 'a7')
        self.trilobite1 = Trilobite('TT1', 'tan', 'b1')
        self.trilobite2 = Trilobite('TT2', 'tan', 'f1')
        self.trilobite3 = Trilobite('AT1', 'ame', 'b7')
        self.trilobite4 = Trilobite('AT2', 'ame', 'f7')
        self.wombat1 = Wombat('TW1', 'tan', 'c1')
        self.wombat2 = Wombat('TW2', 'tan', 'e1')
        self. wombat3 = Wombat('AW1', 'ame', 'c7')
        self. wombat4 = Wombat('AW2', 'ame', 'e7')
        self. beluga1 = Beluga('TB1', 'tan', 'd1')
        self.beluga2 = Beluga('AB1', 'ame', 'd7')

    def test_get_color(self):
        """"test the get_color method for each child piece type"""
        self.assertEqual(self.pika1.get_color(), 'tan')
        self.assertEqual(self.pika3.get_color(), 'ame')
        self.assertEqual(self.trilobite2.get_color(), 'tan')
        self.assertEqual(self.trilobite4.get_color(), 'ame')
        self.assertEqual(self.wombat1.get_color(), 'tan')
        self.assertEqual(self.wombat4.get_color(), 'ame')
        self.assertEqual(self.beluga1.get_color(), 'tan')

    def test_get_piece_id(self):
        """"test the get_piece_id method for each child piece type"""
        self.assertEqual(self.pika2.get_piece_id(), 'TP2')
        self.assertEqual(self.pika4.get_piece_id(), 'AP2')
        self.assertEqual(self.trilobite1.get_piece_id(), 'TT1')
        self.assertEqual(self.trilobite3.get_piece_id(), 'AT1')
        self.assertEqual(self.wombat2.get_piece_id(), 'TW2')
        self.assertEqual(self.wombat3.get_piece_id(), 'AW1')
        self.assertEqual(self.beluga2.get_piece_id(), 'AB1')

    def test_get_location(self):
        """"test the get_location method for each child piece type"""
        self.assertEqual(self.pika1.get_location(), 'a1')
        self.assertEqual(self.trilobite3.get_location(), 'b7')
        self.assertEqual(self.wombat1.get_location(), 'c1')
        self.assertEqual(self.beluga2.get_location(), 'd7' )
        self.assertEqual(self.wombat2.get_location(), 'e1')
        self.assertEqual(self.trilobite4.get_location(), 'f7')
        self.assertEqual(self.pika2.get_location(), 'g1')

    def test_set_location(self):
        """test the set_location method"""
        self.pika2.set_location('f3')
        self.assertEqual(self.pika2.get_location(), 'f3')
        self.beluga1.set_location('c7')
        self.assertEqual(self.beluga1.get_location(), 'c7')
        self.trilobite3.set_location('e2')
        self.assertEqual(self.trilobite3.get_location(), 'e2')
        self.wombat1.set_location('a4')
        self.assertEqual(self.wombat1.get_location(), 'a4')

    def test_get_locomotion(self):
        """test each get method for the child class """
        self.assertEqual(self.pika1.get_locomotion(), 'sliding')
        self.assertEqual(self.trilobite4.get_locomotion(), 'sliding')
        self.assertEqual(self.wombat3.get_locomotion(), 'jumping')
        self.assertEqual(self.beluga2.get_locomotion(), 'jumping')

    def test_get_direction(self):
        """test each get method for each child piece type"""
        self.assertEqual(self.pika3.get_direction(), 'orthogonal')
        self.assertEqual(self.wombat2.get_direction(), 'orthogonal')
        self.assertEqual(self.trilobite1.get_direction(), 'diagonal')
        self.assertEqual(self.beluga2.get_direction(), 'diagonal')

    def test_get_distance(self):
        """test each get method for each child piece type"""
        self.assertEqual(self.pika1.get_distance(), 4)
        self.assertEqual(self.trilobite4.get_distance(), 2)
        self.assertEqual(self.wombat2.get_distance(), 1)
        self.assertEqual(self.beluga2.get_distance(), 3)

    def test_get_whose_turn(self):
        """test the get_whose_turn method in AnimalGame class"""
        game = AnimalGame()
        self.assertEqual(game.get_whose_turn(), 'tan')

        game.make_move('c1', 'c2')
        self.assertEqual(game.get_whose_turn(), 'ame')

    def test_get_game_state(self):
        """test the _get_game_state method in AnimalGame class"""
        game = AnimalGame()
        self.assertEqual(game.get_game_state(), 'UNFINISHED')

        game.make_move('d1', 'g4')
        game.make_move('d7', 'a4')
        game.make_move('g4', 'd7')
        game.make_move('e7', 'd7')
        self.assertEqual(game.get_game_state(), 'AMETHYST_WON')

        game2 = AnimalGame()
        game2.make_move('d1', 'g4')
        game2.make_move('b7', 'd5')
        game2.make_move('g4', 'd7')
        self.assertEqual(game2.get_game_state(), 'TANGERINE_WON')


class TestAnimalGame(unittest.TestCase):
    """Tests for the AnimalGame class and functions it calls.
    Each test docstring will provide more information on aspects tested."""

    def setUp(self):
        """creation of a blank test board state"""
        self.test_board = {'a1': None,
                       'b1': None,
                       'c1': None,
                       'd1': None,
                       'e1': None,
                       'f1': None,
                       'g1': None,
                       'a2': None,
                       'b2': None,
                       'c2': None,
                       'd2': None,
                       'e2': None,
                       'f2': None,
                       'g2': None,
                       'a3': None,
                       'b3': None,
                       'c3': None,
                       'd3': None,
                       'e3': None,
                       'f3': None,
                       'g3': None,
                       'a4': None,
                       'b4': None,
                       'c4': None,
                       'd4': None,
                       'e4': None,
                       'f4': None,
                       'g4': None,
                       'a5': None,
                       'b5': None,
                       'c5': None,
                       'd5': None,
                       'e5': None,
                       'f5': None,
                       'g5': None,
                       'a6': None,
                       'b6': None,
                       'c6': None,
                       'd6': None,
                       'e6': None,
                       'f6': None,
                       'g6': None,
                       'a7': None,
                       'b7': None,
                       'c7': None,
                       'd7': None,
                       'e7': None,
                       'f7': None,
                       'g7': None,
                       }

    def test_AnimalGame_start_state(self):
        """ """
        game = AnimalGame()

        self.assertEqual(game.get_whose_turn(), 'tan')
        self.assertEqual(game.get_game_state(), 'UNFINISHED')
        self.assertEqual(len(game._piece_obj_list), 14)
        self.assertEqual(len(game._pieces_dict), 14)
        self.assertEqual(len(game._board_state), 49)

        current_piece_id = game._board_state['a1']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'a1')
        current_piece_id = game._board_state['b1']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'b1')
        current_piece_id = game._board_state['c1']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'c1')
        current_piece_id = game._board_state['d1']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'd1')
        current_piece_id = game._board_state['e1']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'e1')
        current_piece_id = game._board_state['f1']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'f1')
        current_piece_id = game._board_state['g1']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'g1')

        self.assertEqual(game._board_state['a2'], None)
        self.assertEqual(game._board_state['b2'], None)
        self.assertEqual(game._board_state['c2'], None)
        self.assertEqual(game._board_state['d2'], None)
        self.assertEqual(game._board_state['e2'], None)
        self.assertEqual(game._board_state['f2'], None)
        self.assertEqual(game._board_state['g2'], None)

        self.assertEqual(game._board_state['a3'], None)
        self.assertEqual(game._board_state['b3'], None)
        self.assertEqual(game._board_state['c3'], None)
        self.assertEqual(game._board_state['d3'], None)
        self.assertEqual(game._board_state['e3'], None)
        self.assertEqual(game._board_state['f3'], None)
        self.assertEqual(game._board_state['g3'], None)

        self.assertEqual(game._board_state['a4'], None)
        self.assertEqual(game._board_state['b4'], None)
        self.assertEqual(game._board_state['c4'], None)
        self.assertEqual(game._board_state['d4'], None)
        self.assertEqual(game._board_state['e4'], None)
        self.assertEqual(game._board_state['f4'], None)
        self.assertEqual(game._board_state['g4'], None)

        self.assertEqual(game._board_state['a5'], None)
        self.assertEqual(game._board_state['b5'], None)
        self.assertEqual(game._board_state['c5'], None)
        self.assertEqual(game._board_state['d5'], None)
        self.assertEqual(game._board_state['e5'], None)
        self.assertEqual(game._board_state['f5'], None)
        self.assertEqual(game._board_state['g5'], None)

        self.assertEqual(game._board_state['a6'], None)
        self.assertEqual(game._board_state['b6'], None)
        self.assertEqual(game._board_state['c6'], None)
        self.assertEqual(game._board_state['d6'], None)
        self.assertEqual(game._board_state['e6'], None)
        self.assertEqual(game._board_state['f6'], None)
        self.assertEqual(game._board_state['g6'], None)

        current_piece_id = game._board_state['a7']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'a7')
        current_piece_id = game._board_state['b7']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'b7')
        current_piece_id = game._board_state['c7']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'c7')
        current_piece_id = game._board_state['d7']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'd7')
        current_piece_id = game._board_state['e7']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'e7')
        current_piece_id = game._board_state['f7']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'f7')
        current_piece_id = game._board_state['g7']
        current_piece = game._pieces_dict[current_piece_id]
        self.assertEqual(current_piece.get_location(), 'g7')

    def test_valid_distance(self):
        """Tests to ensure the check_valid_pathway function will correctly
        determine if an attempted move is within the allowed distance."""

        #pika - sliding, orthogonal
        pikaT = Pika('TP1', 'tan', 'b2')
        pikaA = Pika('TA1', 'ame', 'f6')
        self.test_board['b2'] = pikaT
        self.test_board['f6'] = pikaA
        # over allowed
        self.assertEqual(pikaT.check_valid_pathway('b2', 'g2', self.test_board), False)
        self.assertEqual(pikaA.check_valid_pathway('f6', 'a6', self.test_board), False)
        # under allowed
        self.assertEqual(pikaT.check_valid_pathway('b2', 'b4', self.test_board), True)
        self.assertEqual(pikaT.check_valid_pathway('b2', 'd2', self.test_board), True)
        self.assertEqual(pikaA.check_valid_pathway('f6', 'f5', self.test_board), True)
        self.assertEqual(pikaA.check_valid_pathway('f6', 'f3', self.test_board), True)
        # exact amount
        self.assertEqual(pikaT.check_valid_pathway('b2', 'f2', self.test_board), True)
        self.assertEqual(pikaT.check_valid_pathway('b2', 'b6', self.test_board), True)
        self.assertEqual(pikaA.check_valid_pathway('f6', 'f2', self.test_board), True)
        self.assertEqual(pikaA.check_valid_pathway('f6', 'b6', self.test_board), True)

        #trilobite - sliding, diagonal
        trilobiteT = Trilobite('TT1', 'tan', 'b2')
        trilobiteA = Trilobite('TT1', 'ame', 'f6')
        self.test_board['b2'] = pikaT
        self.test_board['f6'] = pikaA
        # over allowed
        self.assertEqual(trilobiteT.check_valid_pathway('b2', 'e5', self.test_board), False)
        self.assertEqual(trilobiteA.check_valid_pathway('f6', 'a1', self.test_board), False)
        # under allowed
        self.assertEqual(trilobiteT.check_valid_pathway('b2', 'c3', self.test_board), True)
        self.assertEqual(trilobiteT.check_valid_pathway('b2', 'a1', self.test_board), True)
        self.assertEqual(trilobiteA.check_valid_pathway('f6', 'e7', self.test_board), True)
        self.assertEqual(trilobiteA.check_valid_pathway('f6', 'g5', self.test_board), True)
        # exact amount
        self.assertEqual(trilobiteT.check_valid_pathway('b2', 'd4', self.test_board), True)
        self.assertEqual(trilobiteA.check_valid_pathway('f6', 'd4', self.test_board), True)

        #wombat - jumping, 0rthogonal
        wombatT = Wombat('TW1', 'tan', 'b2')
        wombatA = Wombat('TW1', 'ame', 'f6')
        self.test_board['b2'] = pikaT
        self.test_board['f6'] = pikaA
        # over allowed
        self.assertEqual(wombatT.check_valid_pathway('b2', 'd4', self.test_board), False)
        self.assertEqual(wombatA.check_valid_pathway('f6', 'c3', self.test_board), False)
        # exact amount
        self.assertEqual(wombatT.check_valid_pathway('b2', 'a1', self.test_board), True)
        self.assertEqual(wombatT.check_valid_pathway('b2', 'c1', self.test_board), True)
        self.assertEqual(wombatA.check_valid_pathway('f6', 'g7', self.test_board), True)
        self.assertEqual(wombatA.check_valid_pathway('f6', 'e7', self.test_board), True)

        #beluga - jumping, diagonal
        belugaT = Beluga('TW1', 'tan', 'c2')
        belugaA = Beluga('TW1', 'ame', 'd4')
        self.test_board['c2'] = pikaT
        self.test_board['d4'] = pikaA
        # over allowed
        self.assertEqual(belugaT.check_valid_pathway('c2', 'g6', self.test_board), False)
        # under allowed
        self.assertEqual(belugaT.check_valid_pathway('c2', 'a4', self.test_board), False)
        self.assertEqual(belugaT.check_valid_pathway('c2', 'd3', self.test_board), False)
        self.assertEqual(belugaA.check_valid_pathway('d4', 'f2', self.test_board), False)
        self.assertEqual(belugaA.check_valid_pathway('d4', 'c3', self.test_board), False)
        # exact amount
        self.assertEqual(belugaT.check_valid_pathway('c2', 'f5', self.test_board), True)
        self.assertEqual(belugaA.check_valid_pathway('d4', 'a7', self.test_board), True)
        self.assertEqual(belugaA.check_valid_pathway('d4', 'a1', self.test_board), True)

    def test_sliding_blocked_pika(self):
        """ Tests to ensure the check_valid_pathway function will correctly
        determine if an attempted move when sliding into another piece is
        correctly handled."""

        pikaT = Pika('TP1', 'tan', 'b2')
        wombatT = Wombat('TW1', 'tan', 'd6')
        belugaT = Beluga('TB1', 'tan', 'd2')
        pikaA = Pika('TP1', 'ame', 'f6')
        wombatA = Wombat('TW1', 'ame', 'b4')
        trilobiteA = Trilobite('TT1', 'ame', 'f3')
        self.test_board['b2'] = pikaT
        self.test_board['d6'] = wombatT
        self.test_board['d2'] = belugaT
        self.test_board['f6'] = pikaA
        self.test_board['b4'] = wombatA
        self.test_board['f3'] = trilobiteA

        #own color piece in way
        self.assertEqual(pikaT.check_valid_pathway('d4', 'e2', self.test_board), False)
        self.assertEqual(pikaA.check_valid_pathway('f6', 'f2', self.test_board), False)
        #different color piece in way
        self.assertEqual(pikaT.check_valid_pathway('d4', 'b5', self.test_board), False)
        self.assertEqual(pikaA.check_valid_pathway('f6', 'c6', self.test_board), False)

    def test_sliding_blocked_trilobite(self):
        """ Tests to ensure the check_valid_pathway function will correctly
        determine if an attempted move when sliding into another piece is
        correctly handled and that a jumping piece is not blocked."""

        trilobiteT = Trilobite('TT1', 'tan', 'b2')
        wombatT = Wombat('TW1', 'tan', 'e6')
        belugaT = Beluga('TB1', 'tan', 'c2')
        trilobiteA = Trilobite('TT1', 'ame', 'f6')
        wombatA = Wombat('TW1', 'ame', 'b4')
        pikaA = Pika('TP1', 'ame', 'f4')
        trilobiteA2 = Trilobite('TT1', 'ame', 'e4')
        self.test_board['b2'] = trilobiteT
        self.test_board['e6'] = wombatT
        self.test_board['c2'] = belugaT
        self.test_board['f6'] = trilobiteA
        self.test_board['b4'] = wombatA
        self.test_board['f4'] = pikaA
        self.test_board['e4'] = trilobiteA2

        #own color piece in way
        self.assertEqual(trilobiteT.check_valid_pathway('d4', 'c2', self.test_board), False)
        self.assertEqual(trilobiteA.check_valid_pathway('f6', 'f4', self.test_board), False)

        #different color piece in way
        self.assertEqual(trilobiteT.check_valid_pathway('d4', 'b4', self.test_board), False)
        self.assertEqual(trilobiteA.check_valid_pathway('f6', 'd6', self.test_board), False)

        #jumping not blocked (beluga)
        self.assertEqual(belugaT.check_valid_pathway('c2', 'f5', self.test_board), True)

    def test_valid_direction(self):
        """Tests to ensure the check_valid_pathway function will correctly
        determine if an attempted move is within the allowed direction."""

        # pika - orthogonal, sliding
        pikaT = Pika('TP1', 'tan', 'd4')
        self.test_board['d4'] = pikaT
        # left
        self.assertEqual(pikaT.check_valid_pathway('d4', 'b4', self.test_board), True)
        # right
        self.assertEqual(pikaT.check_valid_pathway('d4', 'g4', self.test_board), True)
        # up
        self.assertEqual(pikaT.check_valid_pathway('d4', 'd1', self.test_board), True)
        # down
        self.assertEqual(pikaT.check_valid_pathway('d4', 'd6', self.test_board), True)
        # diagonal
        self.assertEqual(pikaT.check_valid_pathway('d4', 'e3', self.test_board), False)
        self.assertEqual(pikaT.check_valid_pathway('d4', 'b6', self.test_board), False)
        #not valid for either type
        self.assertEqual(pikaT.check_valid_pathway('d4', 'a3', self.test_board), False)

        # wombat - orthogonal, jumping
        wombatT = Wombat('TW1', 'tan', 'd4')
        self.test_board['d4'] = wombatT
        # left
        self.assertEqual(wombatT.check_valid_pathway('d4', 'c4', self.test_board), True)
        # right
        self.assertEqual(wombatT.check_valid_pathway('d4', 'e4', self.test_board), True)
        # up
        self.assertEqual(wombatT.check_valid_pathway('d4', 'd3', self.test_board), True)
        # down
        self.assertEqual(wombatT.check_valid_pathway('d4', 'd5', self.test_board), True)
        # diagonal
        self.assertEqual(wombatT.check_valid_pathway('d4', 'b2', self.test_board), False)
        self.assertEqual(wombatT.check_valid_pathway('d4', 'f6', self.test_board), False)
        # sliding 1 space opposite type
        self.assertEqual(wombatT.check_valid_pathway('d4', 'e3', self.test_board), True)
        self.assertEqual(wombatT.check_valid_pathway('d4', 'c5', self.test_board), True)


        # beluga - diagonal, jumping
        belugaT = Beluga('TB1', 'tan', 'd4')
        self.test_board['d4'] = belugaT
        # left/up
        self.assertEqual(belugaT.check_valid_pathway('d4', 'a1', self.test_board), True)
        # left/down
        self.assertEqual(belugaT.check_valid_pathway('d4', 'a7', self.test_board), True)
        # right/up
        self.assertEqual(belugaT.check_valid_pathway('d4', 'g1', self.test_board), True)
        # right/down
        self.assertEqual(belugaT.check_valid_pathway('d4', 'g7', self.test_board), True)
        # orthogonal more than one space
        self.assertEqual(belugaT.check_valid_pathway('d4', 'b4', self.test_board), False)
        self.assertEqual(belugaT.check_valid_pathway('d4', 'd6', self.test_board), False)
        # sliding 1 space opposite type
        self.assertEqual(belugaT.check_valid_pathway('d4', 'e4', self.test_board), True)
        self.assertEqual(belugaT.check_valid_pathway('d4', 'd5', self.test_board), True)

        # trilobite - sliding, diagonal
        trilobiteT = Trilobite('TT1', 'tan', 'd4')
        self.test_board['d4'] = trilobiteT
        # left/up
        self.assertEqual(trilobiteT.check_valid_pathway('d4', 'b2', self.test_board), True)
        # left/down
        self.assertEqual(trilobiteT.check_valid_pathway('d4', 'b6', self.test_board), True)
        # right/up
        self.assertEqual(trilobiteT.check_valid_pathway('d4', 'f2', self.test_board), True)
        # right/down
        self.assertEqual(trilobiteT.check_valid_pathway('d4', 'f6', self.test_board), True)
        # orthogonal
        self.assertEqual(trilobiteT.check_valid_pathway('d4', 'b4', self.test_board), False)
        self.assertEqual(trilobiteT.check_valid_pathway('d4', 'd6', self.test_board), False)

    def test_additional_make_move(self):
        """Above tests have ensured that the check_valid_pathway called by
        make_move handles various similar situation correctly."""
        game = AnimalGame()

        #sliding,diagonal: Valid, invalid, valid, invalid
        #start_piece checking done initially to ensure that the test is actually moving the pieces as written
        start_piece_id = game._board_state['b1']
        start_piece = game._pieces_dict[start_piece_id]
        self.assertEqual(game.make_move('b1','d3'), True)
        self.assertEqual(start_piece.get_location(), 'd3')
        start_piece_id = game._board_state['f7']
        start_piece = game._pieces_dict[start_piece_id]
        self.assertEqual(game.make_move('f7', 'c4'), False)
        self.assertEqual(start_piece.get_location(), 'f7')
        self.assertEqual(game.make_move('f7','e6'), True)
        self.assertEqual(game.make_move('f1', 'f4'), False)

        # sliding,orthogonal: Valid, invalid, valid, invalid
        self.assertEqual(game.make_move('g1','g3'), True)
        self.assertEqual(game.make_move('g7', 'e5'), False)
        self.assertEqual(game.make_move('g7','g5'), True)
        self.assertEqual(game.make_move('a1', 'a6'), False)

        #jumping,diagonal: Valid, invalid, valid, invalid
        self.assertEqual(game.make_move('d1','a4'), True)
        self.assertEqual(game.make_move('d7', 'd3'), False)
        self.assertEqual(game.make_move('d7','d6'), True)
        self.assertEqual(game.make_move('a4', 'c6'), False)

        #jumping,orthogonal: Valid, invalid, valid, invalid
        self.assertEqual(game.make_move('c1','c2'), True)
        self.assertEqual(game.make_move('e7', 'g7'), False)
        self.assertEqual(game.make_move('e7','f6'), True)
        self.assertEqual(game.make_move('e1', 'c3'), False)

        #sliding blocked own color
        start_piece_id = game._board_state['e6']
        start_piece = game._pieces_dict[start_piece_id]
        self.assertEqual(game.make_move('e6', 'g6'), False)
        self.assertEqual(start_piece.get_location(), 'e6')

        #sliding blocked other color
        start_piece_id = game._board_state['g3']
        start_piece = game._pieces_dict[start_piece_id]
        self.assertEqual(game.make_move('g3', 'g6'), False)
        self.assertEqual(start_piece.get_location(), 'g3')

    def test_turn_order(self):
        """ test it is updated
        test it won't let you move the wrong piece/not your turn (ex 2 tan moves in a row)"""
        game = AnimalGame()

        #tan takes turn
        game.make_move('b1', 'd3')
        self.assertEqual(game.get_whose_turn(), 'ame')

        #ame takes turn
        game.make_move('c7', 'c6')
        self.assertEqual(game.get_whose_turn(), 'tan')

        #ame try to take 2 turns in a row
        game.make_move('g7', 'g5')
        self.assertEqual(game.get_whose_turn(), 'tan')

        #tan takes turn
        game.make_move('d1', 'a4')
        self.assertEqual(game.get_whose_turn(), 'ame')

        #tan try to take 2 turns in a row
        game.make_move('a4', 'd7')
        self.assertEqual(game.get_whose_turn(), 'ame')


    def test_piece_capture(self):
        """Test that piece capturing/ a piece being on an endpoint is handled
        correctly.
        Note that beluga capturing is tested in test_get_game_status"""
        game = AnimalGame()
        #set up moves
        game.make_move('g1', 'g4')
        game.make_move('e7', 'e6')
        game.make_move('e1', 'd2')
        game.make_move('b7', 'c6')
        game.make_move('d2', 'e3')
        game.make_move('e6', 'e5')
        game.make_move('e3', 'e4')
        game.make_move('a7','a6')


        # tan onto tan (invalid)
        end_piece_id = game._board_state['b1']
        end_piece = game._pieces_dict[end_piece_id]
        start_piece_id = game._board_state['a1']
        start_piece = game._pieces_dict[start_piece_id]
        self.assertEqual(game.make_move('a1', 'b1'), False)
        self.assertEqual(start_piece.get_location(), 'a1')
        self.assertEqual(end_piece.get_location(), 'b1')

        # ame onto ame (invalid)
        end_piece_id = game._board_state['c6']
        end_piece = game._pieces_dict[end_piece_id]
        start_piece_id = game._board_state['c7']
        start_piece = game._pieces_dict[start_piece_id]
        self.assertEqual(game.make_move('c7', 'c6'), False)
        self.assertEqual(start_piece.get_location(), 'c7')
        self.assertEqual(end_piece.get_location(), 'c6')

        # tan onto ame (valid)
        end_piece_id = game._board_state['g7']
        end_piece = game._pieces_dict[end_piece_id]
        start_piece_id = game._board_state['g4']
        start_piece = game._pieces_dict[start_piece_id]
        self.assertEqual(game.make_move('g4', 'g7'), True)
        self.assertEqual(start_piece.get_location(), 'g7')
        self.assertEqual(end_piece.get_location(), 'captured')
        self.assertNotIn(end_piece.get_piece_id(), game.get_board_state())
        self.assertEqual(game.get_whose_turn(), 'ame')

        # ame onto tan (valid)
        end_piece_id = game._board_state['e4']
        end_piece = game._pieces_dict[end_piece_id]
        start_piece_id = game._board_state['e5']
        start_piece = game._pieces_dict[start_piece_id]
        self.assertEqual(game.make_move('e5', 'e4'), True)
        self.assertEqual(start_piece.get_location(), 'e4')
        self.assertEqual(end_piece.get_location(), 'captured')
        self.assertNotIn(end_piece.get_piece_id(), game.get_board_state())
        self.assertEqual(game.get_whose_turn(), 'tan')
