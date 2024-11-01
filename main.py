import pygame
import library

pygame.init()
pygame.mixer.init()

mainSystem = library.System(800, 600, 60)
mainSystem.beginProcess()