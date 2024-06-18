import pygame, sys
from pygame.locals import QUIT
from classes import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Jacks World!')


while True:
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
      elif event.type == pygame.KEYDOWN:
          player1.move(event)

  player1.draw()
  pygame.display.update()
