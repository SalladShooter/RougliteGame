import pygame
from player import Player
from gun import Gun

pygame.init()
screen = pygame.display.set_mode((480, 368))
pygame.display.set_caption('Rougelite Game')
clock = pygame.time.Clock()
running = True
dt = 0

player = Player(screen) 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    
    dt = clock.tick(60) / 1000
    
    player.move(dt)   
    player.draw(screen)

    pygame.display.flip()

pygame.quit()