import pygame
import math

pygame.init()

class Gun:
    def __init__(self, screen, size_multiplier=2):
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.original_gun_img = pygame.image.load("images/gun.png").convert_alpha()
        original_width, original_height = self.original_gun_img.get_size()
        new_width = int(original_width * size_multiplier)
        new_height = int(original_height * size_multiplier)
        self.gun_img = pygame.transform.scale(self.original_gun_img, (new_width, new_height))
        self.gun_rect = self.gun_img.get_rect()
        self.gun_pos = pygame.Vector2(self.screen_width / 2, self.screen_height / 2)
        self.gun_distance = 32 
        self.speed = 300
        self.dt = 0
        self.angle = 0
        self.rotated_gun_img = self.gun_img
        self.gun_pivot = [16, 16]
        self.gun_offset = pygame.math.Vector2(self.gun_distance, 0)

    @staticmethod
    def rotate(surface, angle, pivot, offset):
        """Rotate the surface around the pivot point.

        Args:
            surface (pygame.Surface): The surface that is to be rotated.
            angle (float): Rotate by this angle.
            pivot (tuple, list, pygame.math.Vector2): The pivot point.
            offset (pygame.math.Vector2): This vector is added to the pivot.
        """
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)
        rotated_offset = offset.rotate(angle) 
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        return rotated_image, rect
    def move(self, player_pos: pygame.Vector2):
        mouse_pos = pygame.mouse.get_pos()
        
        direction = pygame.Vector2(mouse_pos) - player_pos  
        
        if direction.length() != 0:
            direction = direction.normalize()
        
        self.gun_pos = player_pos + direction * (self.gun_distance * 1.5)
        
        angle = math.degrees(math.atan2(direction.y, direction.x))
        
        if angle != self.angle:
            self.angle = angle
            self.rotated_gun_img, self.gun_rect = self.rotate(self.gun_img, self.angle, self.gun_pivot, self.gun_offset) 

        self.gun_rect.center = self.gun_pos

    def draw(self, screen):
        screen.blit(self.rotated_gun_img, self.gun_rect)