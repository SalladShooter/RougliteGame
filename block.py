import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, tilesize, x, y, block_image, screen):
        super().__init__()
        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize
        self.screen = screen
        self.block_image = block_image
        self.block_image = pygame.image.load(self.block_image).convert_alpha()
        
        self.image = self.block_image
        self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, dt):
        self.draw(self.screen)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)