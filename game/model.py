import pygame
from pygame.sprite import Group, Sprite

from game.config import TILE, RIGHT, LEFT
from game.objects import Alien
from game.objects import Projectile
from game.objects import Weapon
from game.objects import Ship
import images


class Model:
    def __init__(self):
        from view import View
        self._view: View | None = None

        # Groups
        self.player_projectiles = Group()
        self.alien_projectiles = Group()
        self.alien_fleet = Group()

        # Projectiles
        rail = Projectile(images.rail, damage=50, move_speed=10)
        plasma_ball = Projectile(images.plasma_ball, damage=25)
        radioactive_wave = Projectile(images.radioactive_wave, health=100, damage=5)
        rocket = Projectile(images.rocket, damage=100)

        # Weapons
        railgun = Weapon(rail)
        plasma_gun = Weapon(plasma_ball)
        radioactive_gun = Weapon(radioactive_wave)
        rocket_gun = Weapon(rocket)

        # Ships
        self.player = Ship(images.ship, radioactive_gun.copy(), self.player_projectiles)

        # Aliens
        self.aliens = (
            Alien(images.alien_1, railgun.copy(), health=100),
            Alien(images.alien_2, railgun.copy(), health=75),
            Alien(images.alien_3, railgun.copy(), health=50),
            Alien(images.alien_4, railgun.copy(), health=25),
        )

    def set_view(self, view):
        self._view = view

    def set_up_params(self):
        game_board = self._view.game_board
        self.player.centerx = game_board.into_centerx
        self.player.bottom = game_board.into_bottom

        self.create_alien_fleet()
        self.aliens[0].set_global_moving_flag(RIGHT, True)

    def update(self):
        self.update_player()
        self.update_alien_fleet()
        self.update_projectiles()

    def update_player(self):
        self.check_ship_out_edge(self.player)
        self.player.update()

    def update_projectiles(self):
        for projectiles in self.player_projectiles:
            projectiles.update()
            self.check_projectile_out_edge(projectiles)

    def update_alien_fleet(self):
        for alien in self.alien_fleet:
            self.collide_player_projectiles_with_alien(alien)
            alien.update()
        self.check_alien_fleet_out_edge()

    def create_alien_fleet(self):
        game_board = self._view.game_board
        drop = 5
        rows = 10
        cols = 4
        startx = game_board.width // 2 - (rows // 2) * (TILE + drop)
        x = startx
        y = 0

        for col in range(cols):
            x = startx
            y += TILE + drop if col != 0 else 0
            for row in range(rows):
                x += TILE + drop if row != 0 else 0
                alien = self.aliens[col].copy()
                alien.x = x
                alien.y = y
                alien.add(self.alien_fleet)

    def check_projectile_out_edge(self, projectile: Projectile | Sprite):
        game_board = self._view.game_board
        if not (0 < projectile.centerx < game_board.width) \
                or not (0 < projectile.centery < game_board.height):
            projectile.kill()

    def check_ship_out_edge(self, ship: Ship):
        game_board = self._view.game_board
        if self.player.right > game_board.into_right:
            self.player.set_moving_flag(RIGHT, False)
            self.player.right = game_board.into_right
        elif self.player.left < game_board.into_left:
            self.player.set_moving_flag(LEFT, False)
            self.player.left = game_board.into_left

    def check_alien_fleet_out_edge(self):
        game_board = self._view.game_board
        for alien in self.alien_fleet:
            alien: Alien | Sprite
            if alien.right > game_board.into_right:
                alien.set_global_moving_flag(RIGHT, False)
                alien.set_global_moving_flag(LEFT, True)
                self.drop_alien_fleet()
                break
            elif alien.left < game_board.into_left:
                alien.set_global_moving_flag(RIGHT, True)
                alien.set_global_moving_flag(LEFT, False)
                self.drop_alien_fleet()
                break

    def drop_alien_fleet(self):
        for alien in self.alien_fleet:
            alien: Alien | Sprite
            alien.drop()

    def collide_player_projectiles_with_alien(self, alien: Alien | Sprite):
        collides = pygame.sprite.spritecollide(alien, self.player_projectiles, False)
        if collides:
            projectile: Projectile | Sprite = collides[0]
            alien.health -= projectile.damage
            projectile.health -= 1
            if alien.health <= 0:
                alien.kill()
            if projectile.health <= 0:
                projectile.kill()
