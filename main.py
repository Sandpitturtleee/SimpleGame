import pygame
from sys import exit

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1000, 750))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Pierwsza gra")

    game_font = pygame.font.Font('graphic/font/my_font.ttf',60)
    background = pygame.image.load('graphic/background/BG.png')
    ground1 = pygame.image.load('graphic/ground/1.png')
    ground2 = pygame.image.load('graphic/ground/2.png')
    ground3 = pygame.image.load('graphic/ground/3.png')

    text_surface = game_font.render("New game", False,'Red')

    #test_surface = pygame.Surface((500,500))
    #test_surface.fill('red')

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(background, (0, 0))
        screen.blit(ground1, (308, 600))
        screen.blit(ground2, (436, 600))
        screen.blit(ground3, (564, 600))

        screen.blit(text_surface, (430,300))
        #screen.blit(test_surface,(0,0))
        pygame.display.update()
        clock.tick(60)


