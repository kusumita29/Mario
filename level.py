import pygame
from tiles import Tile
from settings import tile_size
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
    def run(self):
        self.tiles.update(self.world_speed)
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.player.draw(self.display_surface)