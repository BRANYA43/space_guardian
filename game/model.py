import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

from game.config import *
from game.objects import Alien
from objects import Projectile
from objects import Weapon
from objects import Ship
import images


def _calc_damage(projectile: Projectile | Sprite, ship: Ship | Alien | Sprite):
    ship.health -= projectile.damage
    if ship.health <= 0:
        ship.kill()
    projectile.kill()


class Model:
    def __init__(self):
        from view import View
        self._view: View | None = None
        self.score = 0

        # Groups
        self.player_projectiles = Group()
        self.alien_projectiles = Group()
        self.alien_fleet = Group()

        # Projectiles
        rail = Projectile(images.rail)
        plasma_ball = Projectile(images.plasma_ball)
        radioactive_wave = Projectile(images.radioactive_wave)
        rocket = Projectile(images.rocket)

        # Weapons
        railgun = Weapon(rail, self.player_projectiles)
        plasma_gun = Weapon(plasma_ball, self.player_projectiles)
        radioactive_gun = Weapon(radioactive_wave, self.player_projectiles)
        bazuka = Weapon(rocket, self.player_projectiles)

        # Ships
        self.player = Ship(images.ship, bazuka.get_copy())

        # Aliens
        self.aliens = (
            Alien(images.alien_1, railgun.get_copy()),
            Alien(images.alien_2, railgun.get_copy()),
            Alien(images.alien_3, railgun.get_copy()),
            Alien(images.alien_4, railgun.get_copy()),
        )

    def set_view(self, view):
        self._view = view

    def start_game(self):
        self.player.centerx = self._view.display_rect.centerx
        self.player.bottom = self._view.display_rect.bottom - 10
        self._create_fleet()
        self.alien_fleet.sprites()[0].set_global_moving_flag(RIGHT, True)

    def reset_game(self):
        self.alien_fleet.sprites()[0].set_global_moving_flag(LEFT, False)
        self.alien_fleet.sprites()[0].set_global_moving_flag(RIGHT, False)
        self._delete_fleet()
        self._delete_projectiles()
        self.start_game()

    def end_game(self):
        pygame.quit()

    def update(self):
        self.is_win()
        self.collide()
        self._update_player_projectiles()
        self._update_player()
        self._update_fleet()

    def update_player(self):
        ...

    def

    def _update_player(self):
        if self.player.right > self._view.display_rect.right:
            self.player.set_moving_flag(RIGHT, False)
            self.player.right = self._view.display_rect.right
        elif self.player.left < 0:
            self.player.set_moving_flag(LEFT, False)
            self.player.left = self._view.display_rect.left

        self.player.update()

    def _update_player_projectiles(self):
        for projectile in self.player_projectiles:
            self._kill_projectile_off_display(projectile)
            projectile.update()

    def _update_fleet(self):
        for alien in self.alien_fleet:
            alien.update()
        self._check_fleet_edge()

    def _kill_projectile_off_display(self, projectile: Sprite | Projectile):
        if 0 < projectile.centerx < self._view.display_rect.right \
                and 0 < projectile.centery < self._view.display_rect.bottom:
            return
        else:
            projectile.kill()

    def collide(self):
        self._collide_player_projectiles_with_alien()
        self._collide_player_with_alien()

    def _collide_player_projectiles_with_alien(self):
        collides = pygame.sprite.groupcollide(self.alien_fleet, self.player_projectiles, False, False)
        for aline, projectile in zip(collides.keys(), collides.values()):
            if collides:
                _calc_damage(projectile[0], aline)

    def _collide_player_with_alien(self):
        if pygame.sprite.spritecollide(self.player, self.alien_fleet, dokill=False):
            if self.player.health > 0:
                self.player.health -= 1

                pygame.time.wait(1000)
                self.reset_game()
            else:
                print('END GAME')
                pygame.time.wait(1000)
                self.end_game()

    def is_win(self):
        if len(self.alien_fleet.sprites()) == 0:
            print('YOU WIN')
            pygame.time.wait(1000)
            self.end_game()

    def _create_fleet(self):
        row = 0
        distance = 5
        for image in self.aliens:
            for column in range(10):
                alien = self.aliens[0].get_copy()
                alien.y = (16 + distance) * row
                alien.x = (16 + distance) * column
                self.alien_fleet.add(alien)
            row += 1

    def _delete_fleet(self):
        self.alien_fleet.empty()

    def _delete_projectiles(self):
        self.player_projectiles.empty()
        self.alien_projectiles.empty()

    def _check_fleet_edge(self):
        for alien in self.alien_fleet:
            alien: Alien
            if alien.right > self._view.display_rect.right:
                alien.set_global_moving_flag(RIGHT, False)
                alien.set_global_moving_flag(LEFT, True)
                self._drop_fleet()
                break
            elif alien.left < self._view.display_rect.left:
                alien.set_global_moving_flag(RIGHT, True)
                alien.set_global_moving_flag(LEFT, False)
                self._drop_fleet()
                break

    def _drop_fleet(self):
        for alien in self.alien_fleet:
            alien.drop()
