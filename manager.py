import numpy as np
from scipy.signal import convolve2d

"""
Rule 1: Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.

Rule 2: Any live cell with two or three live neighbours lives on to the next generation.

Rule 3: Any live cell with more than three live neighbours dies, as if by overpopulation.

Rule 4: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
class GameManager:
    def __init__(self) -> None:
        self.filter = np.array([
                                    [1,1,1],
                                    [1,0,1],
                                    [1,1,1]
                                ])

    def _convolve(self, state):
        return convolve2d(state, self.filter, mode='same', boundary='fill', fillvalue=0)
    
    def _apply_rules(self, state: int, neighbours: int):
        if state == 1:
            return self._life_rule(neighbours)
        else:
            return self._birth_rule(neighbours)

    def _life_rule(self, neighbours: int):
        if neighbours < 2 or neighbours > 3:
            return 0
        else:
            return 1
    
    def _birth_rule(self, neighbours: int):
        if neighbours == 3:
            return 1
        else:
            return 0

    def step(self, board: np.array) -> np.array:
        convolved = self._convolve(board)
        is_empty = np.all(convolved == 0)
        return np.vectorize(self._apply_rules)(board, convolved), is_empty
