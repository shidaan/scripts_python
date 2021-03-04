# desafio 21 -- tocar um arquivo mp3

import pygame

pygame.init()
pygame.mixer.music.load('exercicio21.mp3')
pygame.mixer.music.play()
pygame.mixer.wait()
# x = input('Digite algo para parar a música')