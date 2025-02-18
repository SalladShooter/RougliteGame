import pygame
from gun import Gun

pygame.init()

class Player:
    def __init__(self, screen, size_multiplier=2):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.player_img = pygame.image.load("images/player.png").convert_alpha()
        original_width, original_height = self.player_img.get_size()
        new_width = int(original_width * size_multiplier)
        new_height = int(original_height * size_multiplier)
        self.player_img = pygame.transform.scale(self.player_img, (new_width, new_height))
        self.player_rect = self.player_img.get_rect()
        self.player_pos = pygame.Vector2(self.screen_width / 2, self.screen_height / 2)
        self.speed = 300
        self.dt = 0
        self.gun = Gun(screen)
        
    def move(self, dt):
        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_w]:
            if self.player_pos.y - self.player_rect.height / 2 > 0:
                self.player_pos.y -= self.speed * dt

        if self.keys[pygame.K_s]:
            if self.player_pos.y + self.player_rect.height / 2 < self.screen_height:
                self.player_pos.y += self.speed * dt

        if self.keys[pygame.K_a]:
            if self.player_pos.x - self.player_rect.width / 2 > 0:
                self.player_pos.x -= self.speed * dt

        if self.keys[pygame.K_d]:
            if self.player_pos.x + self.player_rect.width / 2 < self.screen_width:
                self.player_pos.x += self.speed * dt
            
    def draw(self, screen):
        self.player_rect.center = (self.player_pos.x, self.player_pos.y)
        screen.blit(self.player_img, self.player_rect)
        self.gun.move(self.player_pos)
        self.gun.draw(screen)
