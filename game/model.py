from objects import Ship
import images


class Model:
    def __init__(self):
        from view import View
        self._view: View | None = None
        self.player = Ship(images.ship)

    def set_up_start_params(self):
        self.player.centerx = self._view.display_rect.centerx
        self.player.bottom = self._view.display_rect.bottom - 10

    def set_view(self, view):
        self._view = view

    def update(self):
        self.update_player()

    def update_player(self):
        self.player.update()
