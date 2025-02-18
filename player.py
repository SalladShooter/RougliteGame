import pygame
from gun import Gun

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, player_group, size_multiplier, player_x, player_y):
        super().__init__()
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.player_img = pygame.image.load("images/player.png").convert_alpha()
        original_width, original_height = self.player_img.get_size()
        new_width = int(original_width * size_multiplier)
        new_height = int(original_height * size_multiplier)
        self.player_img = pygame.transform.scale(self.player_img, (new_width, new_height))

        self.image = self.player_img
        self.rect = self.image.get_rect()

        self.player_pos = pygame.Vector2(player_x * 16, player_y * 16)
        self.rect.center = (self.player_pos.x, self.player_pos.y)

        self.speed = 300

        self.gun = Gun(screen, 1, self.rect.centerx, self.rect.centery)
        player_group.add(self.gun)

    def move(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.player_pos.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.player_pos.y += self.speed * dt
        if keys[pygame.K_a]:
            self.player_pos.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.player_pos.x += self.speed * dt

        self.rect.center = (self.player_pos.x, self.player_pos.y)

    def update(self, dt):
        self.move(dt)
        self.gun.move(self.player_pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.gun.draw(screen)
