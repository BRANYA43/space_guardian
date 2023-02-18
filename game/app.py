import pygame

from game.config import *
from game.controller import Controller
from game.model import Model
from game.view import View


class App:
    def __init__(self):
        self.game_run = True
        self.clock = pygame.time.Clock()
        self.model = Model()
        self.view = View()
        self.controller = Controller(self.model)

        self.model.set_view(self.view)
        self.view.set_model(self.model)

    def mainloop(self):
        while self.game_run:
            self.controller.handler_events()
            self.model.update()
            self.view.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.mainloop()
