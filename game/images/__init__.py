import os

from pygame.image import load

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# aliens
alien_1 = load('alien_1.png')
alien_2 = load('alien_2.png')
alien_3 = load('alien_3.png')

# projectiles
rail = load('rail.png')
plasma_ball = load('plasma_ball.png')
radioactive_wave = load('radioactive_wave.png')
rocket = load('rocket.png')

#
ship = load('ship_1.png')
