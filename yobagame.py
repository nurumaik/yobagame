import pygame
import sys
from pygame.locals import *

screen = pygame.display.set_mode((1000,1000), DOUBLEBUF)
clock = pygame.time.Clock()
x = 100
y = 100
xs = 0
ys = 0

while True:
	clock.tick(60)
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if not hasattr(event,'key'): continue
		if event.key == K_ESCAPE: sys.exit(0)
	keys = pygame.key.get_pressed()
    if (keys[K_w] or keys[K_KP8]): xs, ys = 0, -5
	if (keys[K_s] or keys[K_KP2]): xs, ys = 0, +5
	if (keys[K_a] or keys[K_KP4]): xs, ys = -5, 0
	if (keys[K_d] or keys[K_KP6]): xs, ys = +5, 0
	if (keys[K_KP1]): xs, ys = -5, +5
	if (keys[K_KP3]): xs, ys = +5, +5
	if (keys[K_KP7]): xs, ys = -5, -5
	if (keys[K_KP9]): xs, ys = +5, -5
	x += xs
	y += ys
	c = pygame.Surface((50, 50))
	pygame.draw.circle(c, (255, 255, 255), (25, 25), 25, 0)
	rect = c.get_rect()
	rect.center = (x, y);
	screen.blit(c, rect)
	pygame.display.flip()