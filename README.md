# Game of Life

## Usage
After when the game is running everything is paused. The game can be **started and paused with the SPACE-key**. 

When the game is in pause mode:
- the player can press and hold the H-key to bring new squares to LIFE at the current mouse position
- the player can press and hold the G-key to bring new squares to DEATH at the current mouse position

## Command Line Arguments:
- --fps
  - Sets the FPS of the game
  - default = 2
- --board_type 
  - Sets the type of the board
    - default = black
      - available:
          - random (random positioning with p=0.5)
          - prob
          - grid
          - horz
          - vert
          - black
- --grid_factor
  - Sets the number of lines per direction. Used for board_types: grid, horz and vert
  - default = 1
- --prob
  - Sets the probability of LIFE squares on the board. Applies only for board_type=prob
  - default = 0.1
