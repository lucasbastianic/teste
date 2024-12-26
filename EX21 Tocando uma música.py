#Tocando uma música
#*** Necessário ter a musica na lista

import pygame
pygame.init()
pygame.mixer.music.load #(Nome da música)
pygame.mixer.music.play()
pygame.event.wait()