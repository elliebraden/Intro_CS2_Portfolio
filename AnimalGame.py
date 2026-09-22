# Author: Ellen Braden
# GitHub username: elliebraden
# Date: 3/13/26
# Description: Creates a program with multiple classes to allow for the creation
#   of the initial state and game play of a chess-like game with board size and piece
#   movement described in the docstrings.


class Piece:
    """ Represents a Piece object with the following attributes. Is a parent class.
    Attributes:
        _color(str): color used to indicate which player it belongs to.
        _piece_id: unique to each piece
        _location(str): initiated to the pieces starting location on the board,
        will indicate if piece is captured
        Each child class will have a _locomotion, _distance, and _direction attribute
        as well with more detail in their docstrings.
    """

    def __init__(self, piece_id, color, location):
        """Creates a Piece object with the above defined attributes."""
        self._piece_id = piece_id
        self._color = color
        self._location = location

    def get_piece_id(self):
        """Returns the piece_id of the object in the form of a string."""
        return self._piece_id

    def get_color(self):
        """Returns the color of the object in the form of a string."""
        return self._color

    def get_location(self):
        """Returns the _location of the object in the form of a string."""
        return self._location

    def set_location(self, board_space):
        """will update the Piece's _location to the provided board_space
        string. Provided board_space should follow the lowercase letter (a-g)
        then number format (1-7)"""
        self._location = board_space

    def combine_and_check_space(self, letter, num, end_space, current_board):
        """Helper method to the check_pathway methods to recombine the space letter and num,
        and check is a space contains another piece or is the endpoint."""
        current_space = letter + num
        if current_space == end_space:
            return True
        if current_board[current_space] is not None:
            return False
        return None


class Pika(Piece):
    """Represents a sPike piece object with the following attributes and
    those inherited from the Piece parent class.
        Attributes:
            Inherits from Piece class
            _locomotion(str): the piece's movement type; sliding
            _distance(int): how far a piece can move; 4
            _direction(str): the piece's directional movement; orthogonal
    """

    def __init__(self,piece_id, color, location):
        """Creates a Pika obj.
        Will initiate the attributes described above and those described in the
        Piece parent class"""
        super().__init__(piece_id, color, location)
        self._locomotion = 'sliding'
        self._distance = 4
        self._direction = 'orthogonal'

    def get_locomotion(self):
        """Will return the string indicating the pieces move locomotion."""
        return self._locomotion

    def get_distance(self):
        """Will return the integer indicating how far the piece can move"""
        return self._distance

    def get_direction(self):
        """Will return the string indicating the pieces move direction."""
        return self._direction

    def check_valid_pathway(self, start, end, current_board):
        """Checks if the pathway is valid meaning it does not have another piece
         in the path,endpoint is an exception, and it follows the piece's
         specified direction, distance, and locomotion specifications.
        Will be called by make_move method.
        Will return True if it is a valid move and false if it is invalid.
        """
        #split start into start_letter and start_num
        start_split = list(start)
        start_letter = start_split[0]
        start_num = start_split[1]

        # split end into end_letter and end_num
        end_split = list(end)
        end_letter = end_split[0]
        end_num = end_split[1]

        # set up other variables
        change_by = 0
        next_num = start_num
        next_letter = start_letter.lower()
        valid = None

        #check for up/down movement
        start_letter = start_letter.lower()
        end_letter = end_letter.lower()
        if start_letter == end_letter:
            if start_num < end_num:         # moving down
                change_by = 1
            if start_num > end_num:         # moving up
                change_by = -1
        # check for piece obstruction in determined direction
            for space in range(self._distance):
                next_num = str(int(next_num) + change_by)
                valid = self.combine_and_check_space(start_letter, next_num, end, current_board)
                if valid is not None:
                    return valid

        #check for left/right movement
        if start_num == end_num:
            if start_letter < end_letter:           # moving right
                change_by = 1
            if start_letter > end_letter:           # moving left
                change_by = -1

        # check for piece obstruction in determined direction
            for space in range(self._distance):
                next_letter = chr(ord(next_letter) + change_by)
                valid = self.combine_and_check_space(next_letter, start_num, end, current_board)
                if valid is not None:
                    return valid


        valid = False                                #if not returned by this point not a valis movement, wrong direction or distance
        return valid


class Trilobite(Piece):
    """Represents a Trilobite piece object with the following attributes
    and those inherited from the Piece parent class.
        Attributes:
            Inherits from Piece class
            _locomotion(str): the piece's movement type; sliding
            _distance(int): how far a piece can move; 2
            _direction(str): the piece's directional movement; diagonal
    """

    def __init__(self, piece_id, color, location):
        """Creates a Trilobite obj.
        Will initiate the attributes described above and those described in the
        Piece parent class"""
        super().__init__( piece_id, color, location)
        self._locomotion = 'sliding'
        self._distance = 2
        self._direction = 'diagonal'

    def get_locomotion(self):
        """Will return the string indicating the pieces move locomotion."""
        return self._locomotion

    def get_distance(self):
        """Will return the integer indicating how far the piece can move"""
        return self._distance

    def get_direction(self):
        """Will return the string indicating the pieces move direction."""
        return self._direction

    def check_valid_pathway(self, start, end, current_board):
        """Checks if the pathway is valid meaning it does not have another piece
        in the path, endpoint is an exception, and it follows the piece's specified
        direction, distance, and locomotion.
        Will be called by make_move method.
        Will return True if it is a valid move and false if it is invalid.
        """

        # split start into start_letter and start_num
        start_split = list(start)
        start_letter = start_split[0]
        start_num = start_split[1]

        # split end into end_letter and end_num
        end_split = list(end)
        end_letter = end_split[0]
        end_num = end_split[1]

        # set up other variables
        letter_change_by = 0
        num_change_by = 0
        next_num = start_num
        next_letter = start_letter.lower()
        valid = None

        #check for orthogonal movement
        if start_num == end_num:
            return False
        if start_letter == end_letter:
            return False

        #find up/down direction
        if start_num < end_num:                 # moving down
            num_change_by = 1
        if start_num > end_num:                 # moving up
            num_change_by = -1

        #find left/right direction
        start_letter = start_letter.lower()
        end_letter = end_letter.lower()
        if start_letter < end_letter:           # moving right
            letter_change_by = 1
        if start_letter > end_letter:           # moving left
            letter_change_by = -1

        # check for piece obstruction in determined diagonal direction
        for space in range(self._distance):
            next_num = str(int(next_num) + num_change_by)
            next_letter = chr(ord(next_letter) + letter_change_by)
            valid = self.combine_and_check_space(next_letter, next_num, end, current_board)
            if valid is not None:
                return valid

        return False


class Wombat(Piece):
    """Represents a Trilobite piece object with the following attributes
    and those inherited from the Piece parent class.
        Attributes:
             Inherits from Piece class
            _locomotion(str): the piece's movement type; jumping
            _distance(int): how far a piece can move; 1
            _direction(str): the piece's directional movement; orthogonal
    """


    def __init__(self,piece_id, color, location):
        """Creates a Wombat obj.
        Will initiate the attributes described above and those described in the
        Piece parent class"""
        super().__init__( piece_id, color, location)
        self._locomotion = 'jumping'
        self._distance = 1
        self._direction = 'orthogonal'

    def get_locomotion(self):
        """Will return the string indicating the pieces move locomotion."""
        return self._locomotion

    def get_distance(self):
        """Will return the integer indicating how far the piece can move"""
        return self._distance

    def get_direction(self):
        """Will return the string indicating the pieces move direction."""
        return self._direction

    def check_valid_pathway(self, start, end, current_board):
        """Checks if a requested move would be a valid endpoint for the piece.
        Valid being on the board and following the piece's specified direction,
        distance, and locomotion.
        For jumping valid distance and direction includes 1 space in the
        opposite direction type.
        Will be called by make_move method.
        Will return True if it is a valid move and false if it is invalid.
        """
        # split start into start_letter and start_num
        start_split = list(start)
        start_letter = start_split[0]
        start_num = start_split[1]

        # split end into end_letter and end_num
        end_split = list(end)
        end_letter = end_split[0]
        end_num = end_split[1]

        #set up other variables
        change_by = self._distance
        next_num = start_num
        next_letter = start_letter.lower()
        valid = None

        # check for up/down movement
        start_letter = start_letter.lower()
        end_letter = end_letter.lower()
        if start_letter == end_letter:
            if start_num > end_num:             # moving up
                change_by *= -1                 # else assume moving down, no change to the change_by

        # check for valid down/up jumping movement
            next_num = str(int(start_num) + change_by)
            valid = self.combine_and_check_space(start_letter, next_num, end, current_board)
            if valid is True:
                return valid

        #check for left/right movement
        if start_num == end_num:
            if start_letter > end_letter:       # moving left
                change_by *= -1                 # else assume moving right, no change to the change_by

        # check for valid left/right jumping movement
            next_letter = chr(ord(next_letter) + change_by)
            if next_letter.isalpha() is True:
                valid = self.combine_and_check_space(next_letter, start_num, end, current_board)
                if valid is True:
                   return valid

        #check if moving one space diagonally
        #check right and down/up 1
        if int(start_num) + 1 == int(end_num):
            if (ord(start_letter) + 1) == ord(end_letter):
                return True
            if (ord(start_letter) - 1) == ord(end_letter):
                return True
        # check left and down/up 1
        if int(start_num) - 1 == int(end_num):
            if (ord(start_letter) + 1) == ord(end_letter):
                return True
            if (ord(start_letter) - 1) == ord(end_letter):
                return True

        return False

class Beluga(Piece):
    """Represents a Beluga piece object with the following attributes
    and those inherited from the Piece parent class.
        Attributes:
             Inherits from Piece class
            _locomotion(str): the piece's movement type; jumping
            _distance(int): how far a piece can move; 3
            _direction(str): the piece's directional movement; diagonal
    """

    def __init__(self, piece_id, color, location):
        """Creates a Beluga obj.
        Will initiate the attributes described above and those described in the
        Piece parent class"""
        super().__init__(piece_id, color, location)
        self._locomotion = 'jumping'
        self._distance = 3
        self._direction = 'diagonal'

    def get_locomotion(self):
        """Will return the string indicating the pieces move locomotion."""
        return self._locomotion

    def get_distance(self):
        """Will return the integer indicating how far the piece can move"""
        return self._distance

    def get_direction(self):
        """Will return the string indicating the pieces move direction."""
        return self._direction

    def check_valid_pathway(self, start, end,current_board):
        """Checks if a requested move would be a valid endpoint for the piece.
        Valid being on the board and following the piece's specified direction,
        distance, and locomotion.
        For jumping valid distance and direction includes 1 space in the
        opposite direction type.
        Will be called by make_move method.
        Will return True if it is a valid move and false if it is invalid.
        """
        # split start into start_letter and start_num
        start_split = list(start)
        start_letter = start_split[0]
        start_num = start_split[1]

        # split end into end_letter and end_num
        end_split = list(end)
        end_letter = end_split[0]
        end_num = end_split[1]

        # set up other variables
        letter_change_by = self._distance
        num_change_by = self._distance
        start_letter = start_letter.lower()
        end_letter = end_letter.lower()
        next_num = start_num
        next_letter = start_letter

        valid = None

        #find up/down direction
        if start_num > end_num:                 # moving up
            num_change_by *= -1                 # else assume down, no change to change by

        #find left/right direction
        if start_letter > end_letter:           # moving left
            letter_change_by *= -1              # else assume right, no change to change by

        # check for valid diagonal jumping movement/landing at end space
        next_num = str(int(next_num) + num_change_by)
        next_letter = chr(ord(start_letter) + letter_change_by)
        if next_letter.isalpha() is True:
            valid = self.combine_and_check_space(next_letter, next_num, end, current_board)
            if valid is True:
                return valid

        #check if moving 1 in the orthogonal
        #check down/up
        if start_letter == end_letter:
            if int(start_num) + 1 == int(end_num):
                return True
            if int(start_num) - 1 == int(end_num):
                return True
        #check left/right
        if start_num == end_num:
            if (ord(start_letter) + 1) == ord(end_letter):
                return True
            if (ord(start_letter) - 1) == ord(end_letter):
                return True

        return False



class AnimalGame:
    """Represent and allows for the initiation and manipulation of an
    AnimalGame object
    Attributes:
        _game_state (str): represents the status of the game they are
            'UNFINISHED', 'TANGERINE_WON', and 'AMETHYST_WON'.
        _whose_turn (str): color of whose turn it is, initiated to 'tan'
        _piece_obj_list (list): list for intal piece object creation, helper to
            _piece_dict creation
        _pieces_dict (dict): dictionary containing all pieces
            (KEY: name/id, VALUE: corresponding piece object
        _board_state (dict): KEY: str of board space (letter#) VALUE: piece object
            at the space or None if empty
    """

    def __init__(self):
        """Creation of a new AnimalGame object.
        Initiates attributes described above
        Will call the _initiate_piece_obj_list, _initiate_pieces_dict, and
         _initiate_board_state methods.
        """
        self._game_state = 'UNFINISHED'
        self._whose_turn = 'tan'
        self._piece_obj_list = self._initiate_piece_obj_list()
        self._pieces_dict = self._initiate_pieces_dict()
        self._board_state = self._initiate_board_state()

    def _initiate_piece_obj_list(self):
        """Method called by __init__ which will create required pieces objects
        and add then to a list.
        Pieces must be created with their start position as the location.
        Piece_id naming convention with be A/T for color, P/W/T/B for piece type,
        and 1 or 2 differentiate same types in that order."""
        piece_list = []
        # tangerine/tan pieces
        piece_list.append(Pika('TP1', 'tan', 'a1'))
        piece_list.append(Trilobite('TT1', 'tan', 'b1'))
        piece_list.append(Wombat('TW1', 'tan', 'c1'))
        piece_list.append(Beluga('TB1', 'tan', 'd1'))
        piece_list.append( Wombat('TW2', 'tan', 'e1'))
        piece_list.append(Trilobite('TT2', 'tan', 'f1'))
        piece_list.append( Pika('TP2', 'tan', 'g1'))

        # amethyst/ame pieces
        piece_list.append(Pika('AP1', 'ame', 'a7'))
        piece_list.append(Trilobite('AT1', 'ame', 'b7'))
        piece_list.append( Wombat('AW1', 'ame', 'c7'))
        piece_list.append(Beluga('AB1', 'ame', 'd7'))
        piece_list.append(Wombat('AW2', 'ame', 'e7'))
        piece_list.append(Trilobite('AT2', 'ame', 'f7'))
        piece_list.append(Pika('AP2', 'ame', 'g7'))

        return piece_list

    def _initiate_pieces_dict(self):
        """Method called by __init__ which will create the _piece_dict using the
        _piece_obj_list."""

        piece_dict = {}
        for piece in self._piece_obj_list:
            piece_dict[piece.get_piece_id()] = piece

        return piece_dict

    def _initiate_board_state(self):
        """Method called by __init__ which will create the _board_state dictionary
        including placing pieces in their appropriate start spaces. """
        start_board = {'a1': None,
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

        for piece_obj in self._piece_obj_list:
            space = piece_obj.get_location()
            start_board[space] = piece_obj.get_piece_id()
        return start_board

    def get_whose_turn(self):
        """Will return the color of whose turn it is"""
        return self._whose_turn

    def get_game_state(self):
        """Returns the string indicating the state of the AnimalGame object"""
        return self._game_state

    def get_board_state(self):
        """Returns the _board_state dictionary."""
        return self._board_state

    def make_move(self, start, end):
        """ Will attempt to make the provided move given start and end space
        in the form of a two digit string compiled of lowercase letter than
        number.
            Will call/use various methods including get_color, set_location,
        and check_valid_pathway to aid in the validation of an attempted move and
        updating various attributes as indicated.
            Will update _board_state, _whose_turn, a piece object's location
        (both of moved and of any captured), and the _game_state if indicated
        once a move has been validated.
            Will return True if a move is valid.
            Will return None if a move is not valid or the one of the players
        has won the game.
        """

        #check game state
        if self._game_state == 'TANGERINE_WON':
            return False
        if self._game_state == 'AMETHYST_WON':
            return False
        if self._game_state != 'UNFINISHED':         #this is a double check that a rouge state/misspelling was not inserted
            return False

        #verify both start and end spaces are spaces on the board
        #also acts to verify lower case letters were passed
        if start not in self._board_state:
            return False
        if end not in self._board_state:
            return False

        # verify there is a piece at start space
        start_piece_id = self._board_state[start]
        if start_piece_id is None:
            return False

        start_piece_obj = self._pieces_dict[start_piece_id]
        #verify start piece color match to whose turn it is
        if start_piece_obj.get_color() != self._whose_turn:
            return False

        #verify start piece is supposed to be on the board
        if start_piece_obj.get_location() != start:
            return None

        #reset captured
        captured = False
        #chekc if endpoint is occupied/would be captured and that end piece is supposed to be on the board
        end_piece_id = self._board_state[end]
        if end_piece_id is not None:
            end_piece_obj = self._pieces_dict[end_piece_id]
            if end_piece_obj.get_color() == self._whose_turn:
                return False
            if end_piece_obj.get_location() != end:
                return None
            captured = True

        #check valid move/pathway
        valid_move = start_piece_obj.check_valid_pathway(start, end, self._board_state)
        if valid_move is False:
            return False

        # update _board_state
        # update captured
        if captured is True:
            end_piece_obj.set_location('captured')
            if 'B' in end_piece_id:
                if end_piece_obj.get_color() == 'tan':
                    self._game_state = 'AMETHYST_WON'
                if end_piece_obj.get_color() == 'ame':
                    self._game_state = 'TANGERINE_WON'
        #update start/end spaces and start piece location
        self._board_state[start] = None
        self._board_state[end] = start_piece_id
        start_piece_obj.set_location(end)

        # update _whose_turn
        if self._whose_turn == 'tan':
            self._whose_turn = 'ame'
        else:
            self._whose_turn = 'tan'

        return True

    def print_board(self):
        """Will return the board visually by iterating through the array and
        printing a space or piece. Will create new line as appropriate.
        Will be printed from amethyst player's perspective."""

        for space in self._board_state:
            if 'a' in space:
                print()
            string = self._board_state[space]
            if string is not None:
                #string += " "
                print(f"{string},", end=" ")
            else:
                print(f" - ,", end=" ")




def main():
    game = AnimalGame()
    game.print_board()

    print()
    print(game.make_move('',''))
    game.print_board()


if __name__ == '__main__':
    main()
