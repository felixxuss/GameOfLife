import pygame
from manager import GameManager
from BoardGenerator import BoadGenerator

# Constants for the grid size and box size
NUM_BOXES = 50
SCREEN_SIZE = (750, 750)
FPS = 2

# Calculate the box size based on the screen size and number of boxes per axis
BOX_SIZE = SCREEN_SIZE[0] // NUM_BOXES

assert BOX_SIZE == SCREEN_SIZE[0] / NUM_BOXES, f"""
SCREEN_SIZE should be a multiple of NUM_BOXES.
NUM_BOXES = {SCREEN_SIZE[0] // BOX_SIZE} would be the next bigger choice.
"""

# init the managers
gm = GameManager()
bg = BoadGenerator(NUM_BOXES, NUM_BOXES)

# Colors
LIFE = (79, 193, 255)
DEATH = (30, 30, 30)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# Load a font for the message box
font = pygame.font.SysFont(None, 36)

# INITIAL BOARD
board = bg.get_grid_offset(4)
###

# Function to draw the grid based on the numpy array


def draw_grid(array, mouse_pos, is_paused):
    for y in range(NUM_BOXES):
        for x in range(NUM_BOXES):
            color = LIFE if array[y][x] == 1 else DEATH
            rect = pygame.draw.rect(
                screen, color, (x * BOX_SIZE, y * BOX_SIZE, BOX_SIZE, BOX_SIZE))
            if rect.collidepoint(mouse_pos) and is_paused:
                if pygame.key.get_pressed()[pygame.K_h]:
                    board[y][x] = 1
                    pygame.draw.rect(
                        screen, LIFE, (x * BOX_SIZE, y * BOX_SIZE, BOX_SIZE, BOX_SIZE))
                if pygame.key.get_pressed()[pygame.K_g]:
                    board[y][x] = 0
                    pygame.draw.rect(
                        screen, DEATH, (x * BOX_SIZE, y * BOX_SIZE, BOX_SIZE, BOX_SIZE))


def show_message_box(message):
    message_surface = font.render(message, True, RED)
    message_rect = message_surface.get_rect(
        center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))
    screen.blit(message_surface, message_rect)
    pygame.display.update()

# Main game loop


def game_loop():
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    is_mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_mouse_pressed = False

        if is_start:
            is_start = False

        if not is_paused:
            # Get the numpy array from the arr_provider function
            board, empty = gm.step(board)

            # Fill the screen with black
            # screen.fill(DEATH)

            # Control the frame rate to 1 FPS
            clock.tick(FPS)
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
    # Start the game loop
    game_loop()

    # Quit pygame
    pygame.quit()
