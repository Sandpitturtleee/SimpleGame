import pygame
from sys import exit

import getpass
if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1000, 750))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Pierwsza gra")

    game_font = pygame.font.Font('graphic/font/my_font.ttf',60)
    background = pygame.image.load('graphic/background/BG.png').convert_alpha()

    ground = pygame.image.load('graphic/ground/ground.png').convert_alpha()

    zombie = pygame.image.load('graphic/characters/zombie/zombie_walk1.png').convert_alpha()
    zombie_rect = zombie.get_rect(topleft=(700, 430))

    player = pygame.image.load('graphic/characters/player/adventurer_walk1.png').convert_alpha()
    player_rect = player.get_rect(topleft=(100,430))

    text_surface = game_font.render(f"{getpass.getuser()} ! Witaj w grze", False,'Red')

    #test_surface = pygame.Surface((500,500))
    #test_surface.fill('red')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        zombie_rect.x -= 3
        if zombie_rect.x <= -100:
            zombie_rect.x = 1110

        screen.blit(background, (0, 0))
        screen.blit(ground, (0,540))

        screen.blit(player,(player_rect))
        screen.blit(zombie, (zombie_rect))

        screen.blit(text_surface, (300,100))
        #screen.blit(test_surface,(0,0))
        pygame.display.update()
        clock.tick(60)


