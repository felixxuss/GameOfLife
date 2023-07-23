import pygame
import argparse

from manager import GameManager
from utils import Settings, LIFE, DEATH, RED


def draw_grid(array, mouse_pos, is_paused):
    """Function to draw the grid based on the numpy array

    Args:
        array: the current board
        mouse_pos: position of the mouse
        is_paused: whether the game was paused (SPACE)
    """
    for y in range(settings.resolution):
        for x in range(settings.resolution):
            color = LIFE if array[y][x] == 1 else DEATH
            rect = pygame.draw.rect(
                screen, color, (x * settings.BOX_SIZE, y * settings.BOX_SIZE, settings.BOX_SIZE, settings.BOX_SIZE))
            if rect.collidepoint(mouse_pos) and is_paused:
                if pygame.key.get_pressed()[pygame.K_h]:
                    board[y][x] = 1
                    pygame.draw.rect(
                        screen, LIFE, (x * settings.BOX_SIZE, y * settings.BOX_SIZE, settings.BOX_SIZE, settings.BOX_SIZE))
                if pygame.key.get_pressed()[pygame.K_g]:
                    board[y][x] = 0
                    pygame.draw.rect(
                        screen, DEATH, (x * settings.BOX_SIZE, y * settings.BOX_SIZE, settings.BOX_SIZE, settings.BOX_SIZE))


def show_message_box(message):
    message_surface = settings.font.render(message, True, RED)
    message_rect = message_surface.get_rect(
        center=(settings.SCREEN_SIZE[0] // 2, settings.SCREEN_SIZE[1] // 2))
    screen.blit(message_surface, message_rect)
    pygame.display.update()


def game_loop(args):
    """The main game loop

    Args:
        args: CL arguments from the user
    """
    global board
    running = True
    is_paused = True
    is_start = True
    mouse_pos = (0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_paused = not is_paused

        if is_start:
            is_start = False

        if not is_paused:
            # Get the numpy array from the ahrr_provider function
            board, empty = gm.step(board)

            # Control the frame rate to 1 FPS
            clock.tick(args.fps)
            if empty:
                is_paused = True
                show_message_box("The game is over")

        # Update the mouse position
        mouse_pos = pygame.mouse.get_pos()
        # Draw the grid
        draw_grid(board, mouse_pos, is_paused)
        # Update the display
        pygame.display.update()


if __name__ == "__main__":
    # build argparser
    argparse = argparse.ArgumentParser()

    argparse.add_argument('--fps', type=int, default=2)

    # board settings
    argparse.add_argument('--resolution', type=int, default=250)
    argparse.add_argument('--board_type', type=str, default='black')
    argparse.add_argument('--prob', type=float, default=0.1)
    argparse.add_argument('--grid_factor', type=int, default=1)

    args = argparse.parse_args()

    # initialize the game manager
    gm = GameManager()

    # set parameters in utils.py
    settings = Settings()
    settings.set_parameters(args)
    board = settings.board

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode(settings.SCREEN_SIZE)
    clock = pygame.time.Clock()

    # Start the game loop
    game_loop(args)

    # Quit pygame
    pygame.quit()
