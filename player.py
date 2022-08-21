import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 5
        
        elif keys[pygame.K_LEFT]:
            self.direction.x = -5 
        
        else:
            self.direction.x = 0

    def update(self):
        self.move()
        self.rect.x += self.direction.x