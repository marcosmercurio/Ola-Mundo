# -*- coding: utf-8 -*-

import time

import pygame

pygame.__init__()

screen = pygame.display.set_mode([640, 480])

pygame.display.set_caption('Olá mundo')

screen.fill([0, 0, 0])

pygame.display.flip()

time.sleep(5)