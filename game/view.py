import pygame
from pygame import Surface

from config import *
from game.objects import TextSurface
from game.objects.view_objects.health import Health
from game.objects.view_objects.score import Score
from game.objects.view_objects.timer import Timer
from objects import Display, GameSurface


class View:
    def __init__(self):
        from model import Model
        self._model: Model | None = None
        self.display = Display(DISPLAY_SIZE)
        self.top_bar = GameSurface(TOP_BAR_SIZE, color=BLACK)
        self.bottom_bar = GameSurface(BOTTOM_BAR_SIZE, color=BLACK)
        self.game_board = GameSurface(GAME_BOARD_SIZE, color=BLACK)
        self.score = Score()
        self.timer = Timer()
        self.health = Health()
        self.win = TextSurface('YOU WIN', color=BLACK, bg=WHITE)
        self.game_over = TextSurface('GAME OVER', color=BLACK, bg=WHITE)

    def set_up_params(self):
        self.timer.set_clock(self._model.clock)
        self.top_bar.topleft = self.display.topleft
        self.game_board.top = self.top_bar.bottom
        self.bottom_bar.top = self.game_board.bottom

        self.score.title.topright = self.top_bar.into_topright
        self.score.value.topright = self.score.title.bottomright
        self.timer.title.topleft = self.top_bar.into_topleft
        self.timer.value.centerx = self.timer.title.centerx
        self.timer.value.top = self.timer.title.bottom

        self.health.title.topleft = self.bottom_bar.into_topleft
        self.health.value.top = self.health.title.into_bottom
        self.health.value.centerx = self.health.title.centerx

        self.win.center = self.game_board.into_center
        self.game_over.center = self.game_board.into_center

        self.top_bar.add_blit_tuple(self.score.get_blits())
        self.top_bar.add_blit_tuple(self.timer.get_blits())
        self.bottom_bar.add_blit_tuple(self.health.get_blits())

        self.game_board.add_blit_object(self._model.player)
        self.game_board.add_blit_object(self._model.player_projectiles)
        self.game_board.add_blit_object(self._model.alien_fleet)

        self.score.set_color(GREEN)
        self.timer.set_color(GREEN)
        self.health.set_color(GREEN)

    def set_model(self, model):
        self._model = model

    def draw(self):
        self.top_bar.draw(self.display.surface)
        self.bottom_bar.draw(self.display.surface)
        self.game_board.draw(self.display.surface)
        pygame.display.update()

    def on_draw_win(self):
        self.game_board.add_blit_object(self.win)

    def on_draw_game_over(self):
        self.game_board.add_blit_object(self.game_over)
