import colorama
from colorama import Fore, Style
import numpy as np

# color codes
VOID = 0
RED = 1
GREEN = 2
BLUE = 3
YELLOW = 4
WHITE = 5
ORANGE = 6

# colorama mapping
color_codes = {
    RED: Fore.RED,
    GREEN: Fore.GREEN,
    BLUE: Fore.BLUE,
    YELLOW: Fore.YELLOW,
    WHITE: Fore.WHITE,
    ORANGE: Fore.LIGHTMAGENTA_EX,
}


class Cube:
    _solved_top = np.full((3, 3), WHITE)
    _solved_bottom = np.full((3, 3), YELLOW)
    _solved_left = np.full((3, 3), GREEN)
    _solved_right = np.full((3, 3), BLUE)
    _solved_front = np.full((3, 3), RED)
    _solved_back = np.full((3, 3), ORANGE)
    move_functions = None

    def __init__(self):
        self.top = np.full((3, 3), WHITE)
        self.bottom = np.full((3, 3), YELLOW)
        self.left = np.full((3, 3), GREEN)
        self.right = np.full((3, 3), BLUE)
        self.front = np.full((3, 3), RED)
        self.back = np.full((3, 3), ORANGE)

    def get_moves(self):
        if self.move_functions is None:
            self.move_functions = {
                'R': self.r,
                'R\'': self.r_,
                '2R': self.r2,
                'L': self.l,
                'L\'': self.l_,
                'L2': self.l2,
                'U': self.u,
                'U\'': self.u_,
                'U2': self.u2,
                'D': self.d,
                'D\'': self.d_,
                'D2': self.d2,
                'F': self.f,
                'F\'': self.f_,
                'F2': self.f2,
                'B': self.b,
                'B\'': self.b_,
            }
        return self.move_functions

    def is_solved(self):
        return np.array_equal(self.top, self._solved_top) \
            and np.array_equal(self.bottom, self._solved_bottom) \
            and np.array_equal(self.left, self._solved_left) \
            and np.array_equal(self.right, self._solved_right) \
            and np.array_equal(self.front, self._solved_front) \
            and np.array_equal(self.back, self._solved_back)

    def move(self, moves: list[str]):
        cube_moves = self.get_moves()
        for move in moves:
            if move in cube_moves:
                cube_moves[move]()
            else:
                print(f'Invalid move {move}. Skipping it...')


    def r(self):
        # Rotate face
        self.right = np.rot90(self.right, -1)

        # Rotate edges
        tmp = self.top[:, 2].copy()
        self.top[:, 2] = self.front[:, 2]
        self.front[:, 2] = self.bottom[:, 2]
        self.bottom[:, 2] = self.back[:, 2]
        self.back[:, 2] = tmp

    def r_(self):
        # Rotate face
        self.right = np.rot90(self.right, 1)

        # Rotate edges
        tmp = self.top[:, 2].copy()
        self.top[:, 2] = self.back[:, 2]
        self.back[:, 2] = self.bottom[:, 2]
        self.bottom[:, 2] = self.front[:, 2]
        self.front[:, 2] = tmp

    def r2(self):
        self.r()
        self.r()

    def l(self):
        # Rotate face
        self.left = np.rot90(self.left, -1)

        # Rotate edges
        tmp = self.top[:, 0].copy()
        self.top[:, 0] = self.back[:, 0]
        self.back[:, 0] = self.bottom[:, 0]
        self.bottom[:, 0] = self.front[:, 0]
        self.front[:, 0] = tmp

    def l_(self):
        # Rotate face
        self.left = np.rot90(self.left, 1)

        # Rotate edges
        tmp = self.top[:, 0].copy()
        self.top[:, 0] = self.front[:, 0]
        self.front[:, 0] = self.bottom[:, 0]
        self.bottom[:, 0] = self.back[:, 0]
        self.back[:, 0] = tmp

    def l2(self):
        self.l()
        self.l()

    def u(self):
        # Rotate face
        self.top = np.rot90(self.top, -1)

        # [PUSH] Rotate back-face to make it easier to rotate edges
        self.back = np.rot90(self.back, 2)

        # Rotate edges
        tmp = self.left[0, :].copy()
        self.left[0, :] = self.front[0, :]
        self.front[0, :] = self.right[0, :]
        self.right[0, :] = self.back[0, :]
        self.back[0, :] = tmp

        # [POP] Rotate back-face back
        self.back = np.rot90(self.back, 2)

    def u_(self):
        # Rotate face
        self.top = np.rot90(self.top, 1)

        # Rotate back-face to make it easier to rotate edges
        self.back = np.rot90(self.back, 2)

        # Rotate edges
        tmp = self.left[0, :].copy()
        self.left[0, :] = self.back[0, :]
        self.back[0, :] = self.right[0, :]
        self.right[0, :] = self.front[0, :]
        self.front[0, :] = tmp

        # Rotate back-face back
        self.back = np.rot90(self.back, 2)

    def u2(self):
        self.u()
        self.u()

    def d(self):
        # Rotate face
        self.bottom = np.rot90(self.bottom, -1)

        # Rotate back-face to make it easier to rotate edges
        self.back = np.rot90(self.back, 2)

        # Rotate edges
        tmp = self.left[2, :].copy()
        self.left[2, :] = self.back[2, :]
        self.back[2, :] = self.right[2, :]
        self.right[2, :] = self.front[2, :]
        self.front[2, :] = tmp

        # Rotate back-face back
        self.back = np.rot90(self.back, 2)

    def d_(self):
        # Rotate face
        self.bottom = np.rot90(self.bottom, 1)

        # Rotate back-face to make it easier to rotate edges
        self.back = np.rot90(self.back, 2)

        # Rotate edges
        tmp = self.left[2, :].copy()
        self.left[2, :] = self.front[2, :]
        self.front[2, :] = self.right[2, :]
        self.right[2, :] = self.back[2, :]
        self.back[2, :] = tmp

        # Rotate back-face back
        self.back = np.rot90(self.back, 2)

    def d2(self):
        self.d()
        self.d()

    def f(self):
        # Rotate face
        self.front = np.rot90(self.front, -1)

        # Rotate edges
        for i in range(3):
            tmp = self.top[2, i].copy()
            self.top[2, i] = self.left[-i, 2]
            self.left[-i, 2] = self.bottom[0, -i]
            self.bottom[0, -i] = self.right[i, 0]
            self.right[i, 0] = tmp

    def f_(self):
        # Rotate face
        self.front = np.rot90(self.front, 1)

        # Rotate edges
        for i in range(3):
            tmp = self.top[2, i].copy()
            self.top[2, i] = self.right[i, 0]
            self.right[i, 0] = self.bottom[0, -i]
            self.bottom[0, -i] = self.left[-i, 2]
            self.left[-i, 2] = tmp

    def f2(self):
        self.f()
        self.f()

    def b(self):
        # Rotate face
        self.back = np.rot90(self.back, -1)

        # Rotate edges
        for i in range(3):
            tmp = self.top[0, i].copy()
            self.top[0, i] = self.right[-i, 2]
            self.right[-i, 2] = self.bottom[2, -i]
            self.bottom[2, -i] = self.left[i, 0]
            self.left[i, 0] = tmp

    def b_(self):
        # Rotate face
        self.back = np.rot90(self.back, 1)

        # Rotate edges
        for i in range(3):
            tmp = self.top[0, i].copy()
            self.top[0, i] = self.left[i, 0]
            self.left[i, 0] = self.bottom[2, -i]
            self.bottom[2, -i] = self.right[-i, 2]
            self.right[-i, 2] = tmp

    def b2(self):
        self.b()
        self.b()

    def print_cube(self):
        margin = 36 * ' '
        space = 5 * ' '

        # print the top face
        for i in range(3):
            row = [color_codes[self.top[i, j]] + '█' + Style.RESET_ALL for j in range(3)]
            print(f"{margin}{space} {' '.join(row)}")

        # print the left, front, and right faces
        for i in range(3):
            left_row = [color_codes[self.left[i, j]] + '█' + Style.RESET_ALL for j in range(3)]
            front_row = [color_codes[self.front[i, j]] + '█' + Style.RESET_ALL for j in range(3)]
            right_row = [color_codes[self.right[i, j]] + '█' + Style.RESET_ALL for j in range(3)]
            print(f"{margin}{' '.join(left_row)} {' '.join(front_row)} {' '.join(right_row)}")

        # print the bottom face
        for i in range(3):
            row = [color_codes[self.bottom[i, j]] + '█' + Style.RESET_ALL for j in range(3)]
            print(f"{margin}{space} {' '.join(row)}")

        # print the back face
        for i in range(3):
            row = [color_codes[self.back[i, j]] + '█' + Style.RESET_ALL for j in range(3)]
            print(f"{margin}{space} {' '.join(row)}")

    @classmethod
    def run_interactive(cls, cube):
        # define a dictionary that maps user input to cube methods
        move_functions = cube.get_moves()
        exit_command = 'exit'
        input_msg = f"Enter a move in [{', '.join(move_functions.keys())}] or '{exit_command}' to quit): "
        # loop until the user enters 'q' to quit
        while True:
            # print the current state of the cube
            cube.print_cube()

            # get user input
            moves = input(input_msg).split(' ')

            # check if user wants to exit
            if exit_command in moves:
                return

            # perform moves
            cube.move(moves)

            # check if solved
            if cube.is_solved():
                print("Solved!!")
