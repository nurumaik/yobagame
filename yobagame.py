import pygame
import sys as sas
import math
from pygame.locals import *

screen = pygame.display.set_mode((1000,1000), DOUBLEBUF)
clock = pygame.time.Clock()
everything = pygame.sprite.Group()
empty = pygame.Surface((1000, 1000))

class Player(pygame.sprite.Sprite):
	def __init__(self):
		self.xs = 0
		self.ys = 0
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10, 10))
		pygame.draw.circle(self.image, (255, 255, 255), (5, 5), 5, 0)
		self.rect = self.image.get_rect()
		self.rect.center = 50, 50
		self.add(everything)

	def update(self):	
		if keys[K_s] or keys[K_KP2]: self.xs, self.ys =  0, +5
		if keys[K_w] or keys[K_KP8]: self.xs, self.ys =  0, -5
		if keys[K_a] or keys[K_KP4]: self.xs, self.ys = -5,  0
		if keys[K_d] or keys[K_KP6]: self.xs, self.ys = +5,  0
		if              keys[K_KP1]: self.xs, self.ys = -5.0 / math.sqrt(2), +5.0 / math.sqrt(2)
		if              keys[K_KP3]: self.xs, self.ys = +5.0 / math.sqrt(2), +5.0 / math.sqrt(2)
		if              keys[K_KP7]: self.xs, self.ys = -5.0 / math.sqrt(2), -5.0 / math.sqrt(2)
		if              keys[K_KP9]: self.xs, self.ys = +5.0 / math.sqrt(2), -5.0 / math.sqrt(2)
		self.rect.move_ip(self.xs, self.ys)

player = Player()

while True:
	clock.tick(60)
	screen.fill((0, 0, 0))
	pygame.event.clear() #fk events
	
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]:  sas.exit(0)

	everything.clear(screen, empty)
	everything.update()
	everything.draw(screen)
	
	pygame.display.flip()