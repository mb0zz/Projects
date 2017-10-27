#.update() - pass keys and values to create or update a key or value in a list in one step
import pygame
pygame.init()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
GRASS = (89, 168, 53)
NBLUE = (1, 43, 85)

class Block( pygame.sprite.Sprite ):
	def __init__( self, color = BLUE, width = 64, height = 64):
	
		super( Block, self).__init__()
		
		self.image = pygame.Surface( ( width, height) )
		
		self.image.fill(color)
		
		self.rect = self.image.get_rect()


x = 400
y = 300
z = 1
radius = 100
thick = 10
color_list = [BLACK, WHITE, GREEN, RED, NBLUE]
size = [800, 600]
yaccel = 0
xaccel = 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Title of pygame thing")
done = False
clock = pygame.time.Clock()
while not done:
	clock.tick(20)
	block_group = pygame.sprite.Group()
	a_block = Block()
	block_group.add( a_block )
	block_group.draw( size )
#Clear the screen and set the screen background
	screen.fill(GRASS)
	pygame.draw.circle(screen, color_list[z], [x + xaccel, y + yaccel], radius, thick)
	pygame.draw.line(screen, BLACK, [0, 0], [800,0], 5)
	pygame.draw.line(screen, BLACK, [800, 0], [800,600], 5)
	pygame.draw.line(screen, BLACK, [0, 0], [0,600], 5)
	pygame.draw.line(screen, BLACK, [0, 600], [800,600], 5)
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done=True # FlaSg that we are done so we exit this loop
		elif event.type == pygame.KEYDOWN:
			move = event.key
			if move == pygame.K_s:
				y = y + 10
				yaccel += 1

			elif move == pygame.K_a:
				x = x - 10
				xaccel -= 1

			elif move == pygame.K_w:
				y = y - 10
			elif move == pygame.K_d:
				x = x + 10
				
			elif move == pygame.K_r:
				radius = radius + 30
				
			elif move == pygame.K_f:
				radius = radius - 15
				
			elif move == pygame.K_t:
				thick = thick + 1
				
			elif move == pygame.K_g:
				thick = thick - 1
			elif move == pygame.K_p:
				try:
					color_list[z + 1]
					z = z + 1	
				except:
					break
			elif move == pygame.K_l:
				try:
					color_list[z - 1]
					z = z - 1
				except:
					break

	pygame.display.flip()
	
# Be IDLE friendly
pygame.quit()