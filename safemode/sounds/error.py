import pygame, sys

pygame.mixer.init()
pygame.mixer.music.load("sounds/error.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
sys.exit()
