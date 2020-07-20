import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000, 900), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('C:/Users/Anna/PycharmProjects/sandBox/python_practice/my_projects/exploringPygame/downloaded/cat.png')
sounds = ['C:/Users/Anna/PycharmProjects/sandBox/python_practice/my_projects/exploringPygame/downloaded/Meowing-cat-sound.mp3',
          'C:/Users/Anna/PycharmProjects/sandBox/python_practice/my_projects/exploringPygame/downloaded/human_footstep_snow_002.mp3']
catx = 10
caty = 10
direction = 'right'

while True:
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 880:
            pygame.mixer.music.load(sounds[0])
            pygame.mixer.music.play()
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 820:
            pygame.mixer.music.load(sounds[0])
            pygame.mixer.music.play()
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            pygame.mixer.music.load(sounds[0])
            pygame.mixer.music.play()
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            pygame.mixer.music.load(sounds[0])
            pygame.mixer.music.play()
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
