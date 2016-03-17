from pygame import font
font.init()

# Colors
white = (255, 255, 255)
black = (0, 0,  0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
dark_gray = (30, 34, 42)
light_gray = (100, 100, 100)

# Display variables
display_width = 800
display_height = 600
title = "My Game"
FPS = 60

# Player variables
player_acc = 1
player_friction = -0.2
player_grav = 0.8

# Font variables
font_file = "fonts/8-Bit-Madness.ttf"
smallfont = font.Font(font_file, 25)
medfont = font.Font(font_file, 50)
largefont = font.Font(font_file, 75)
hugefont = font.Font(font_file, 150)
