import pygame
import math

class Gun(pygame.sprite.Sprite):
    def __init__(self, screen, size_multiplier, x, y):
        super().__init__()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.original_gun_img = pygame.image.load("images/gun.png").convert_alpha()
        original_width, original_height = self.original_gun_img.get_size()
        new_width = int(original_width * size_multiplier)
        new_height = int(original_height * size_multiplier)
        self.gun_img = pygame.transform.scale(self.original_gun_img, (new_width, new_height))
        
        self.image = self.gun_img
        self.rect = self.image.get_rect()
        self.gun_pos = pygame.Vector2(x, y)
        self.gun_distance = 16
        self.gun_pivot = pygame.Vector2(self.gun_img.get_width() / 2, self.gun_img.get_height() / 2)
        self.gun_distance_multiply = 1.5
        self.angle = 0

    @staticmethod
    def rotate(surface, angle, pivot, offset):
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)
        rotated_offset = offset.rotate(angle)
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        return rotated_image, rect 

    def move(self, player_pos: pygame.Vector2):
        mouse_pos = pygame.mouse.get_pos()
        direction = pygame.Vector2(mouse_pos) - player_pos
        
        if direction.length() != 0:
            direction = direction.normalize()

        angle = math.degrees(math.atan2(direction.y, direction.x))

        self.gun_pos = player_pos + direction * self.gun_distance_multiply * self.gun_distance

        if angle != self.angle:
            self.angle = angle
            self.rotated_gun_img, self.rect = self.rotate(self.gun_img, self.angle, self.gun_pos, pygame.Vector2(self.gun_pivot.x, self.gun_pivot.y))

        self.rect.center = self.gun_pos

    def draw(self, screen):
        screen.blit(self.rotated_gun_img, self.rect)
