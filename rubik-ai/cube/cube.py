import colorama
from colorama import Fore, Back, Style
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

    def __init__(self):
        self.top = np.full((3, 3), WHITE)
        self.bottom = np.full((3, 3), YELLOW)
        self.left = np.full((3, 3), GREEN)
        self.right = np.full((3, 3), BLUE)
        self.front = np.full((3, 3), RED)
        self.back = np.full((3, 3), ORANGE)
        self.cube = np.array([self.top, self.bottom, self.left, self.right, self.front, self.back])

    def update_cube(self):
        self.cube = np.array([self.top, self.bottom, self.left, self.right, self.front, self.back])

    def r(self, update=True):
        # Rotate face
        self.right = np.rot90(self.right, -1)

        # Rotate edges
        tmp = self.top[:, 2].copy()
        self.top[:, 2] = self.front[:, 2]
        self.front[:, 2] = self.bottom[:, 2]
        self.bottom[:, 2] = self.back[:, 2]
        self.back[:, 2] = tmp

        # Update cube
        if update:
            self.update_cube()

    def r_(self, update=True):
        # Rotate face
        self.right = np.rot90(self.right, 1)

        # Rotate edges
        tmp = self.top[:, 2].copy()
        self.top[:, 2] = self.back[:, 2]
        self.back[:, 2] = self.bottom[:, 2]
        self.bottom[:, 2] = self.front[:, 2]
        self.front[:, 2] = tmp

        # Update cube
        if update:
            self.update_cube()

    def l(self, update=True):
        # Rotate face
        self.left = np.rot90(self.left, -1)

        # Rotate edges
        tmp = self.top[:, 0].copy()
        self.top[:, 0] = self.back[:, 0]
        self.back[:, 0] = self.bottom[:, 0]
        self.bottom[:, 0] = self.front[:, 0]
        self.front[:, 0] = tmp

        # Update cube
        if update:
            self.update_cube()

    def l_(self, update=True):
        # Rotate face
        self.left = np.rot90(self.left, 1)

        # Rotate edges
        tmp = self.top[:, 0].copy()
        self.top[:, 0] = self.front[:, 0]
        self.front[:, 0] = self.bottom[:, 0]
        self.bottom[:, 0] = self.back[:, 0]
        self.back[:, 0] = tmp

        # Update cube
        if update:
            self.update_cube()

    def u(self, update=True):
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

        # Update cube
        if update:
            self.update_cube()

    def u_(self, update=True):
        # Rotate face
        self.top = np.rot90(self.top, 1)

        # Rotate back-face to make it easier to rotate edges
        self.back = np.rot90(self.back, 2)

        # Rotate edges
        self.top = np.rot90(self.top, 1)
        tmp = self.left[0, :].copy()
        self.left[0, :] = self.back[0, :]
        self.back[0, :] = self.right[0, :]
        self.right[0, :] = self.front[0, :]
        self.front[0, :] = tmp

        # Rotate back-face back
        self.back = np.rot90(self.back, 2)

        # Update cube
        if update:
            self.update_cube()

    def d(self, update=True):
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

        # Update cube
        if update:
            self.update_cube()

    def d_(self, update=True):
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

        # Update cube
        if update:
            self.update_cube()

    def f(self, update=True):
        # Rotate face
        self.front = np.rot90(self.front, -1)

        # Rotate edges
        for i in range(3):
            tmp = self.top[2, i].copy()
            self.top[2, i] = self.left[-i, 2]
            self.left[-i, 2] = self.bottom[0, -i]
            self.bottom[0, -i] = self.right[i, 0]
            self.right[i, 0] = tmp

        # Update cube
        if update:
            self.update_cube()

    def f_(self, update=True):
        # Rotate face
        self.front = np.rot90(self.front, 1)

        # Rotate edges
        for i in range(3):
            tmp = self.top[2, i].copy()
            self.top[2, i] = self.right[i, 0]
            self.right[i, 0] = self.bottom[0, -i]
            self.bottom[0, -i] = self.left[-i, 2]
            self.left[-i, 2] = tmp

        # Update cube
        if update:
            self.update_cube()

    def b(self, update=True):
        # Rotate face
        self.back = np.rot90(self.back, -1)

        # Rotate edges
        for i in range(3):
            tmp = self.top[0, i].copy()
            self.top[0, i] = self.right[-i, 2]
            self.right[-i, 2] = self.bottom[2, -i]
            self.bottom[2, -i] = self.left[i, 0]
            self.left[i, 0] = tmp

        # Update cube
        if update:
            self.update_cube()

    def b_(self, update=True):
        # Rotate face
        self.back = np.rot90(self.back, 1)

        # Rotate edges
        for i in range(3):
            tmp = self.top[0, i].copy()
            self.top[0, i] = self.left[i, 0]
            self.left[i, 0] = self.bottom[2, -i]
            self.bottom[2, -i] = self.right[-i, 2]
            self.right[-i, 2] = tmp

        # Update cube
        if update:
            self.update_cube()

    def print_cube(self):
        space = 5 * ' '

        # print the top face
        for i in range(3):
            row = [color_codes[self.top[i, j]] + '???' + Style.RESET_ALL for j in range(3)]
            print(f"{space} {' '.join(row)}")

        # print the left, front, and right faces
        for i in range(3):
            left_row = [color_codes[self.left[i, j]] + '???' + Style.RESET_ALL for j in range(3)]
            front_row = [color_codes[self.front[i, j]] + '???' + Style.RESET_ALL for j in range(3)]
            right_row = [color_codes[self.right[i, j]] + '???' + Style.RESET_ALL for j in range(3)]
            print(f"{' '.join(left_row)} {' '.join(front_row)} {' '.join(right_row)}")

        # print the bottom face
        for i in range(3):
            row = [color_codes[self.bottom[i, j]] + '???' + Style.RESET_ALL for j in range(3)]
            print(f"{space} {' '.join(row)}")

        # print the back face
        for i in range(3):
            row = [color_codes[self.back[i, j]] + '???' + Style.RESET_ALL for j in range(3)]
            print(f"{space} {' '.join(row)}")

    @classmethod
    def run_interactive(cls, cube):
        # define a dictionary that maps user input to cube methods
        moves = {
            'R': cube.r,
            'R\'': cube.r_,
            'L': cube.l,
            'L\'': cube.l_,
            'U': cube.u,
            'U\'': cube.u_,
            'D': cube.d,
            'D\'': cube.d_,
            'F': cube.f,
            'F\'': cube.f_,
            'B': cube.b,
            'B\'': cube.b_,
        }

        # loop until the user enters 'q' to quit
        while True:
            # print the current state of the cube
            cube.print_cube()

            # get user input
            move = input(f"Enter a move {moves.keys()} or 'q' to quit): ")

            # check if the user wants to quit
            if move == 'q':
                break

            # check if the move is valid
            if move not in moves:
                print("Invalid move!")
                continue

            # call the appropriate method to perform the move
            moves[move]()
