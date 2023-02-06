import pygame

from game.config import *
from game.controller import Controller
from game.model import Model
from game.view import View


class App:
    def __init__(self):
        self.game_run = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.model = Model()
        self.view = View()
        self.model.set_view(self.view)
        self.view.set_model(self.model)
        self.controller = Controller(self.model)

    def mainloop(self):
        self.model.set_up_start_params()
        while self.game_run:
            self.controller.handler_events()
            self.model.update()
            self.view.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.mainloop()
