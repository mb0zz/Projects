import pygame, sys, pytmx, os, random
from pytmx import load_pygame

pygame.init() #initilizing the pygame window

colors = {#My color dictionary
	"WHITE": [255, 255, 255],
	"BLACK": [0, 0, 0],
	"BLUE": [24, 74, 142],
	"RED": [155, 30, 35],
	"GREEN": [65, 167, 72]
}

xwindow = (800)#window x and y dimensions.   Don't have to define them separately
ywindow = (640)
window = pygame.display.set_mode((xwindow, ywindow))#Setting the window with the x and y dimensions
pygame.display.set_caption("Ninja RPG")#naming the window

active = True #keeping the while loop going until not active
clock = pygame.time.Clock()#in order to set fps with clock.tick(fps)

#ninja image that I made
imagelocation = (str(os.getcwd()) + "\Pictures")
musiclocation = (str(os.getcwd()) +  "\Music")
ninjaImg = pygame.image.load(str(imagelocation) + "\\ninja32px.png")#importing a local image
ninx = xwindow/2#where the image will be placed
niny = ywindow/2

#Fonts + text + text size
myfont = pygame.font.Font('freesansbold.ttf', 32)#using fonts and text
fontsurface = myfont.render("Hello world!", True, colors["GREEN"])#(Text to write, ?,Text color, surface.)
fontrect = fontsurface.get_rect()#Get rectangle to place font surface on?
fontrect.center = (ninx, 50)#don't know.  Just include this

#music
pygame.mixer.music.load(musiclocation +"\Crusade.mp3")
pygame.mixer.music.play(-1, 0.0)#Plays infinite times starting at 0.0

#object.play(), and object.stop() to start and stop sounds

#tmxdata = load_pygame("tiledstuff1.tmx")
#image = tmxdata.get_tile_image(0, 0, 0)
#tmxdata = pytmx.TiledMap("tiledstuff1.tmx")
def place_tiles(filename, xwindow, ywindow):#add x and y offset here too.
	#when placex equals screen size restart placex and add 32 to placey
	tmxdata = load_pygame("{}\{}".format(imagelocation, filename))
	tilex = 0#the tile being placed
	tiley = 0
	placex = 0#the location where the tile is being placed
	placey = 0
	tiles = True
	while tiles:#while there are still tiles
		image = (tmxdata.get_tile_image(tilex, tiley, 0))
		window.blit(image, [placex, placey])
		if placey == (ywindow-32) and placex == (xwindow-32):
			tiles = False
		elif placex == (xwindow-32):
			placey += 32
			tilex = 0
			tiley += 1
			placex = 0
		else:
			tilex += 1
			placex += 32
	return_rects = []
	for rect in (pytmx.util_pygame.build_rects(tmxdata, "Collision layer", tileset = None, real_gid=None)):
		return_rects.append(rect)
	return(return_rects)

#
#ENEMY CLASS
#ENEMY CLASS
#
class map_tile(pygame.sprite.Sprite):
	def __init__(self, rectangle):
		super(map_tile, self).__init__()
		pygame.sprite.Sprite.__init__(self)
		self.rect = rectangle
	def rect(self):
		return(self.rect)

class Enemy(pygame.sprite.Sprite):

	def __init__(self, xwindow, ywindow):#self, image using for sprite, xstartlocation and y start location
		super(Enemy, self).__init__()
		pygame.sprite.Sprite.__init__(self)  #pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((32,32))
		self.image.fill(colors["WHITE"])
		self.set_properties()
		self.vspeed = 0
		self.hspeed = 0
		#self.set_position(characterxpos, characterypos)
	def set_properties(self):
		self.rect = self.image.get_rect()
		self.origin_x = self.rect.centerx
		self.origin_y = self.rect.centery
		
	def set_image(self, imagelocation, filename):
		self.image = pygame.image.load("{}\{}".format(imagelocation, filename))
		self.set_properties()
		
	def change_speed(self,hchange,vchange):
		self.hspeed += hchange
		self.vspeed += vchange
	'''def movement_choice(self, play_x, play_y):
		self.get_to_x = play_x/32
		self.get_to_y = play_y/32
		self.block_x = self.rect.x
	def AI(self, playerposx, playerposy):
			pass'''
	def set_position(self,x,y):
		self.rect.x = x #- self.origin_x
		self.rect.y = y #- self.origin_y
		
	def update(self):
		
		self.rect.x += self.hspeed
		self.rect.y += self.vspeed
		window.blit(self.image, self.rect)
#
#ENEMY CLASS
#ENEMY CLASS
#

class Player(pygame.sprite.Sprite):

	def __init__(self, xwindow, ywindow):#self, image using for sprite, xstartlocation and y start location
		super(Player, self).__init__()
		pygame.sprite.Sprite.__init__(self)  #pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((32,32))
		self.image.fill(colors["WHITE"])
		self.set_properties()
		self.vspeed = 0
		self.hspeed = 0
		self.moveblock = 0
		#self.set_position(characterxpos, characterypos)
	def set_properties(self):
		self.rect = self.image.get_rect()
		self.origin_x = self.rect.centerx
		self.origin_y = self.rect.centery
		
	def set_image(self, imagelocation, filename):
		self.image = pygame.image.load("{}\{}".format(imagelocation, filename))
		self.set_properties()
		#14:05
	def change_speed(self,hchange,vchange):
		self.hspeed += hchange
		self.vspeed += vchange
		#if self.hspeed or self.vspeed !=0:
		#	self.moveblock += 8
	
	def set_position(self,x,y):
		self.rect.x = x
		self.rect.y = y
		
	def update(self, collidable):
		self.rect.x += self.hspeed
		collision_list = pygame.sprite.spritecollide(self, collidable, False)
		for collided_object in collision_list:
			if self.hspeed > 0:
				self.rect.right = collided_object.rect.left
			elif self.hspeed < 0:
				self.rect.left = collided_object.rect.right
		self.rect.y += self.vspeed
		collision_list = pygame.sprite.spritecollide(self, collidable, False)
		for collided_object in collision_list:
			if self.vspeed > 0:
				self.rect.bottom = collided_object.rect.top
			elif self.vspeed < 0:
				self.rect.top = collided_object.rect.bottom

	#	self.rect.x += self.hspeed
	#	self.rect.y += self.vspeed
		window.blit(self.image, self.rect)

xloc = 0
yloc = 0
enemyxloc = 64*4
enemyyloc = 64*4
MAP = "tiledstuff1.tmx"
map_collisions = place_tiles("tiledstuff1.tmx", xwindow, ywindow)
ninja = Player(xwindow, ywindow)#(self, filename, xloc, yloc)
ninja.set_image(imagelocation,"ninja32px.png")
ninja.set_position(0,0)

first_enemy = Enemy(xwindow, ywindow)
first_enemy.set_image(imagelocation, "redenemy.png")
first_enemy.set_position(64,64)

second_enemy = Enemy(xwindow, ywindow)
second_enemy.set_image(imagelocation, "redenemy.png")
second_enemy.set_position(128,128)


collidable_objects = pygame.sprite.Group()
collidable_objects.add(first_enemy,second_enemy)
for item in map_collisions:
	add_collision = map_tile(item)#class that does map collisions, haven't expanded it yet.
	collidable_objects.add(add_collision)#add the rectangles made in the above function into collision layer


while active:
	chance_move = 9
#filename, xwindow, ywindow, xposition, yposition, replace_tiles
	for event in pygame.event.get():
		action = pygame.key.get_pressed()
		if event.type == pygame.QUIT:
			pygame.quit()
		#pygame.time.delay(120)
		if event.type == pygame.KEYDOWN:#change_speed(self,hchange,vchange)
			if event.key == pygame.K_w:
				ninja.change_speed(0,-4)
				chance_move = random.randint(0, 9)
			if event.key == pygame.K_s:
				ninja.change_speed(0,4)
				chance_move = random.randint(0, 9)
			if event.key == pygame.K_a:
				ninja.change_speed(-4,0)
				chance_move = random.randint(0, 9)
			if event.key == pygame.K_d:
				ninja.change_speed(4,0)
				chance_move = random.randint(0, 9)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				ninja.change_speed(0,4)
				chance_move = random.randint(0, 9)
			if event.key == pygame.K_s:
				ninja.change_speed(0,-4)
				chance_move = random.randint(0, 9)
			if event.key == pygame.K_a:
				ninja.change_speed(4,0)
				chance_move = random.randint(0, 9)
			if event.key == pygame.K_d:
				ninja.change_speed(-4,0)
				chance_move = random.randint(0, 9)
		event = None
	#window.blit(ninja.image, ninja.rect)
	#pygame.mixer.music.stop()	
	place_tiles("tiledstuff1.tmx", xwindow, ywindow)#Placing background with pytmx + tiled
	#window.blit(fontsurface, fontrect)
	ninja.update(collidable_objects)
	first_enemy.update()
	second_enemy.update()

	pygame.display.update()
	clock.tick(40)	#FPS
	
	
	
	
