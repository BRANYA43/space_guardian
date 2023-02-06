import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

from game.global_vairables import RIGHT, LEFT
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
        self.weapons = {
            'player': {
                'railgun': Weapon(self.projectiles['rail'], self.player_projectiles),
                'plasma_gun': Weapon(self.projectiles['plasma_ball'], self.player_projectiles),
                'radioactive_gun': Weapon(self.projectiles['radioactive_wave'], self.player_projectiles),
                'bazuka': Weapon(self.projectiles['rocket'], self.player_projectiles),
            },
            'alien': {
                'gun': Weapon(self.projectiles['plasma_ball'], self.alien_projectiles, 90)
            }
        }
        self.player = Ship(images.ship, self.weapons['player']['radioactive_gun'])
        self.aliens = (images.alien_1, images.alien_2, images.alien_3)
        self.flot = Group()

    def set_up_start_params(self):
        self.player.centerx = self._view.display_rect.centerx
        self.player.bottom = self._view.display_rect.bottom - 10
        self.create_flot()

    def set_view(self, view):
        self._view = view

    def update(self):
        self.collide()
        self.update_player_projectiles()
        self.update_player()

    def update_player(self):
        if self.player.right > self._view.display_rect.right:
            self.player.set_moving_flag(RIGHT, False)
            self.player.right = self._view.display_rect.right
        elif self.player.left < 0:
            self.player.set_moving_flag(LEFT, False)
            self.player.left = self._view.display_rect.left

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

    def collide(self):
        pygame.sprite.spritecollide(self.player, self.alien_projectiles, True)
        pygame.sprite.groupcollide(self.flot, self.player_projectiles, True, True)

    def create_flot(self):
        row = 0
        distance = 5
        for image in self.aliens:
            for column in range(10):
                alien = Ship(image, self.weapons['alien']['gun'])
                alien.y = (16 + distance) * row
                alien.x = (16 + distance) * column
                self.flot.add(alien)
            row += 1
