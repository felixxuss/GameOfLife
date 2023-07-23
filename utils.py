from BoardGenerator import BoadGenerator
import pygame

# Global Colors
LIFE = (79, 193, 255)
DEATH = (30, 30, 30)
RED = (255, 0, 0)


class Settings:
    def __init__(self) -> None:
        # Constants for the grid size and box size
        self.SCREEN_SIZE = (750, 750)

        # Load a font for the message box
        pygame.init()
        self.font = pygame.font.SysFont(None, 36)

    def set_parameters(self, args):
        self.resolution = args.resolution

        # Calculate the box size based on the screen size and number of boxes per axis
        self.BOX_SIZE = self.SCREEN_SIZE[0] // self.resolution

        assert self.BOX_SIZE == self.SCREEN_SIZE[0] / self.resolution, f"""
        SCREEN_SIZE should be a multiple of NUM_BOXES.
        NUM_BOXES = {self.SCREEN_SIZE[0] // self.BOX_SIZE} would be the next bigger choice.
        """

        # INITIALIZE BOARD
        bg = BoadGenerator(self.resolution, self.resolution)
        self.board = bg.get_board(args)
        ###
