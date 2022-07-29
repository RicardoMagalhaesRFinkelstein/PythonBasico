#Abrir um arquivo mp3 e tocá-lo

import pygame

pygame.init()
pygame.mixer.music.load('iron.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()