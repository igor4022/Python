import pygame

pygame.init()
pygame.mixer.music.load('Tudo_Que_Vai.mp3.mp3')
pygame.mixer.music.play()
input(pygame.event.wait())