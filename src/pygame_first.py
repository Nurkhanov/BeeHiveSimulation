import pygame
import os


def first_run():
    pygame.init()
    
    logo = pygame.image.load(os.path.join( "media/img/251-3.jpg"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("First pygame run")
    image_1 = pygame.image.load(os.path.join( "media/img/drone_bee.jpg"))
    image_2 = pygame.image.load(os.path.join("media/img/queen_bee.jpg"))

    screen = pygame.display.set_mode((640,480))
    screen.blit(image_1,(20,20))
    screen.blit(image_2, (480,200))
    pygame.display.flip()
    
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

if __name__=='__main__':
    first_run()