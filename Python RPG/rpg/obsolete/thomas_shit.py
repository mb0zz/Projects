import pygame
pygame.init()

backgroundColor = (255,255,255)
(width, height) = (500,500)

class Particle:
	def __init__ (self, (x, y), size):
		self.x = x
		self.y = y
		self.size = size
		self.colour = (0,0,255)
		self.thickness = 1
	
	def display(self):
		pygame.draw.circle(window, self.colour, (self.x, self.y), self.size, self.thickness)


window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Test 1')
window.fill(backgroundColor)

my_first_particle = Particle((250, 250), 200)
my_first_particle.display()

pygame.display.flip()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False