import pygame
from player import Player
from gun import Gun
from block import Block

pygame.init()
screen = pygame.display.set_mode((480, 368))
pygame.display.set_caption('Rougelite Game')
clock = pygame.time.Clock()
running = True
dt = 0

TILESIZE = 16

tilemap = [
    '111111111111111111111111111111',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '10000000000000P000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '100000000000000000000000000001',
    '111111111111111111111111111111',
]

# Create sprite groups
all_sprites = pygame.sprite.Group()
block_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

def createTilemap():
    for i, row in enumerate(tilemap):
        for j, column in enumerate(row):
            if column == '1':
                block = Block(TILESIZE, j, i, "images/wall.png", screen)
                block_group.add(block)
                all_sprites.add(block)
            if column == '0':
                block = Block(TILESIZE, j, i, "images/grass.png", screen)
                block_group.add(block)
                all_sprites.add(block)
            if column == 'P':
                block = Block(TILESIZE, j, i, "images/grass.png", screen)
                block_group.add(block)
                all_sprites.add(block)
                player = Player(screen, player_group, 1, j, i)
                player_group.add(player)
                all_sprites.add(player)         

createTilemap()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Update
    dt = clock.tick(60) / 1000
    all_sprites.update(dt)

    block_group.draw(screen)

    player_group.draw(screen)

    pygame.display.flip()

pygame.quit()