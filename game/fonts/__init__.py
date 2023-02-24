import os

import pygame

from game.config import FONT_SIZE

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.font.init()

bionicle = pygame.font.Font('bionicle.ttf', FONT_SIZE)

