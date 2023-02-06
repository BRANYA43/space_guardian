from pygame.sprite import Sprite
from pygame.sprite import Group

from objects import Projectile
from objects import Weapon
from objects import Ship
import images


class Model:
    def __init__(self):
        from view import View
        self._view: View | None = None
        self.player_projectiles = Group()
        self.alien_projectiles = Group()
        self.projectiles = {
            'rail': Projectile(images.rail),
            'plasma_ball': Projectile(images.plasma_ball),
            'radioactive_wave': Projectile(images.radioactive_wave),
            'rocket': Projectile(images.rocket),
        }
        self.weapons = {'player': {
            'railgun': Weapon(self.projectiles['rail'], self.player_projectiles),
            'plasma_gun': Weapon(self.projectiles['plasma_ball'], self.player_projectiles),
            'radioactive_gun': Weapon(self.projectiles['radioactive_wave'], self.player_projectiles),
            'bazuka': Weapon(self.projectiles['rocket'], self.player_projectiles),
        }}
        self.player = Ship(images.ship, self.weapons['player']['railgun'])
        self.alien = None

    def set_up_start_params(self):
        self.player.centerx = self._view.display_rect.centerx
        self.player.bottom = self._view.display_rect.bottom - 10

    def set_view(self, view):
        self._view = view

    def update(self):
        self.update_player_projectiles()
        self.update_player()

    def update_player(self):
        self.player.update()

    def update_player_projectiles(self):
        for projectile in self.player_projectiles:
            self.kill_projectile_off_display(projectile)
            projectile.update()

    def kill_projectile_off_display(self, projectile: Sprite | Projectile):
        if 0 < projectile.centerx < self._view.display_rect.right \
                and 0 < projectile.centery < self._view.display_rect.bottom:
            return
        else:
            projectile.kill()
