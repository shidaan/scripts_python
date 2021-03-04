# desafio 21 -- tocar um arquivo mp3

from pygame import mixer

mixer.init()
mixer.music.load('mp3/exercicio21.mp3')
mixer.music.play()
# pygame.event.wait()
x = input('Digite algo para parar a música')