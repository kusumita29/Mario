import pygame
from tiles import Tile
from settings import tile_size, screen_width
from player import Player

class Level:
    def __init__(self, map, surface):
        self.display_surface = surface 
        self.setup_level(map)
        self.world_speed = 0

    def setup_level(self, X_map):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_idx, row in enumerate(X_map):
            for col_idx, cell in enumerate(row):
                x = col_idx * tile_size
                y = row_idx * tile_size

                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

                if cell == 'P':
                    place_player = Player((x, y))
                    self.player.add(place_player)

    def scroll_level(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width * 0.25 and direction_x < 0:
            self.world_speed = 8
            player.speed = 0

        elif player_x > screen_width * 0.75 and direction_x > 0:
            self.world_speed = -8
            player.speed = 0

        else:
            self.world_speed = 0
            player.speed = 8

    def scroll_x(self):
        player = self.player.sprite
        player.rect.x += (player.direction.x * player.speed)

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0: 
                    player.rect.left = sprite.rect.right
					# player.on_left = True
					# self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
					# player.on_right = True
					# self.current_x = player.rect.right

    def scroll_y(self):
        player = self.player.sprite
        player.add_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
					# player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
					# player.on_ceiling = True

    def run(self):
        # tile movement
        self.tiles.update(self.world_speed)
        self.tiles.draw(self.display_surface)
        self.scroll_level()

        # player movement
        self.player.update()
        self.scroll_x()
        self.scroll_y()
        self.player.draw(self.display_surface)
        