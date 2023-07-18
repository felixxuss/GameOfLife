import pygame
from manager import GameManager
from BoardGenerator import BoadGenerator
import numpy as np

# Constants for the grid size and box size
NUM_BOXES = 250
SCREEN_SIZE = (750, 750)
FPS=10

# Calculate the box size based on the screen size and number of boxes per axis
BOX_SIZE = SCREEN_SIZE[0] // NUM_BOXES

assert BOX_SIZE == SCREEN_SIZE[0] / NUM_BOXES, f"""
SCREEN_SIZE should be a multiple of NUM_BOXES. NUM_BOXES = {SCREEN_SIZE[0]//BOX_SIZE} would be the next bigger choice."""

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

# initialize the board
#board = bg.get_prob_board(GRID_SIZE, GRID_SIZE, p=0.15)
board = bg.get_horz_lines(1)


# Function to draw the grid based on the numpy array
def draw_grid(array):
    for y in range(NUM_BOXES):
        for x in range(NUM_BOXES):
            color = LIFE if array[y][x] == 1 else DEATH
            pygame.draw.rect(screen, color, (x * BOX_SIZE, y * BOX_SIZE, BOX_SIZE, BOX_SIZE))

def show_message_box(message):
    message_surface = font.render(message, True, RED)
    message_rect = message_surface.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))
    screen.blit(message_surface, message_rect)
    pygame.display.update()

# Main game loop
def game_loop():
    global board
    running = True
    is_paused = True
    is_start = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_paused = not is_paused

        if is_start:
            is_start = False
            print("Start")
            draw_grid(board)
            pygame.display.update()

        if not is_paused:
            # Get the numpy array from the arr_provider function
            board, empty = gm.step(board)

            # Fill the screen with black
            screen.fill(DEATH)

            # Draw the grid
            draw_grid(board)

            # Update the display
            pygame.display.update()

            # Control the frame rate to 1 FPS
            clock.tick(FPS)
            if empty:
                is_paused = True
                show_message_box("The game is over")

# Start the game loop
game_loop()

# Quit pygame
pygame.quit()