import numpy as np

class BoadGenerator:
    def __init__(self, H, W) -> None:
        self.h = H
        self.w = W

    def get_random_board(self) -> np.array:
            return np.random.randint(2, size=(self.h, self.w))
    
    def get_prob_board(self, p: float = 0.5) -> np.array:
        return np.random.choice([0, 1], size=(self.h, self.w), p=[1-p, p])

    def get_grid_offset(self, factor=1):
        """
        Args:
            height (_type_): vertical number of boxes
            width (_type_): horizontal number of boxes
            factor (int, optional): number of lines. Horizontal and vertical. Defaults to 1.
        """
        board = np.zeros((self.h, self.w), dtype=int)
        div = 1/(factor+1)
        for i in range(1,factor+1):
            h = int(i * div * self.h)
            w = int(i * div * self.w)
            # horizontal
            board[h,:] = 1
            # vertical
            board[:,w] = 1
        return board
    
    def get_horz_lines(self, factor=1):
        board = np.zeros((self.h, self.w), dtype=int)
        div = 1/(factor+1)
        for i in range(1,factor+1):
            h = int(i * div * self.h)
            # horizontal
            board[h,:] = 1
        return board
    
    def get_vert_lines(self, factor=1):
        board = np.zeros((self.h, self.w), dtype=int)
        div = 1/(factor+1)
        for i in range(1,factor+1):
            w = int(i * div * self.w)
            # horizontal
            board[:,w] = 1
        return board
    
    def get_black_board(self):
        return np.zeros((self.h, self.w), dtype=int)