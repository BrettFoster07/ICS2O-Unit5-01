import pygame
from pygame import Color, Rect
from pygame import draw
from pygame import display
SCREEN_SIZE = (500, 500)
pygame.init()
gameDisplay = display.set_mode(SCREEN_SIZE)
gameDisplay.fill(Color('lightblue'))
draw.rect(gameDisplay, Color('red'), Rect(100, 200, 300, 200))
draw.polygon(gameDisplay, Color('#964B00'), [(100, 200), (400, 200), (250, 50)])
draw.rect(gameDisplay, Color('red'), Rect(0, 400, 500, 100))
draw.circle(gameDisplay, Color('yellow'), (75, 75),25)
display.flip()