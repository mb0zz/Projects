import pygame, sys, pytmx, os, random, math, pdb
from pytmx import load_pygame

pygame.init() #initilizing the pygame window

colors = {#My color dictionary
	"WHITE": [255, 255, 255],
	"BLACK": [0, 0, 0],
	"BLUE": [24, 74, 142],
	"RED": [155, 30, 35],
	"GREEN": [65, 167, 72]
}

l_view = 255#left and top need to be 1 pixel smalle
r_view = 544
t_view = 223
b_view = 416



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

#
#ENEMY CLASS
#ENEMY CLASS
#
class map(pygame.sprite.Sprite):

	def __init__(self, map_file_location, map_to_load, player_object):
		super(map, self).__init__()
		pygame.sprite.Sprite.__init__(self)
		#ONLY LOADS bottom layer right now
		self.locate,self.map_load = map_file_location,map_to_load
		self.tmxdata = load_pygame("{}\{}".format(map_file_location, map_to_load))
		
		self.player_object = player_object
		
		self.x_moved = 0
		self.y_moved = 0
		
		self.placex = 0
		self.placey = 0
		
		self.xtilestart = 0#where the map starts generating based on tiles.  limit x is 0-600
		self.ytilestart = 0#where the map starts generating based on y.  Limit is 0-480
		self.xtile_placeholder = self.xtilestart
		self.ytile_placeholder = self.ytilestart
		
		self.loop_times = 0
	def set_viewbox(self, top, bottom, left, right):
		self.left_viewbox = left
		self.right_viewbox = right
		self.top_viewbox = top
		self.bottom_viewbox = bottom
		
	def load_entire_map(self, map_tile_width, map_tile_height, surface):
		tilex,tiley,placex,placey = 0,0,0,0#the tile being placed, and where it's being placed
		self.map_tile_width = map_tile_width
		self.map_tile_height = map_tile_height
		self.surface = surface
		tiles = True
		#self.all_tiles = []
		while tiles:#while there are still tiles
			curr_tile = (self.tmxdata.get_tile_image(tilex, tiley, self.surface))
			window.blit(curr_tile,[placex,placey])
			if tilex == map_tile_width - 1 and tiley == map_tile_height - 1:
				tiles = False
			elif tilex == map_tile_width - 1:
				placey += 32
				tilex = 0
				tiley += 1
				placex = 0
			else:
				tilex +=1
				placex += 32

		
	def collision_layer(self):
		return_rects = []
		for rect in (pytmx.util_pygame.build_rects(self.tmxdata, "Collision Layer", tileset = None, real_gid=None)):
			return_rects.append(rect)
		return(return_rects)		

	def load_player_section(self):#this will load the player's area based on what
		self.loop_times +=1
		if self.loop_times == 1:
			for item in collidable_layer:
				item.rect.x += self.xtilestart*32
				item.rect.y += self.ytilestart*32
				
		if self.ytilestart > 0 and self.ytilestart < map_y -20:
			self.top_viewbox.set_position(t_view)
			self.bottom_viewbox.set_position(b_view)
			self.top_viewbox.update()
			self.bottom_viewbox.update()
			
		elif self.ytilestart == 0:
			self.top_viewbox.set_position(-1)
			self.bottom_viewbox.set_position(b_view)
			self.top_viewbox.update()
			self.bottom_viewbox.update()
			
		elif self.ytilestart == map_y - 20 :
			self.top_viewbox.set_position(t_view)
			self.bottom_viewbox.set_position(ywindow)
			self.top_viewbox.update()
			self.bottom_viewbox.update()
			
		if self.xtilestart > 0 and self.xtilestart < map_x -25:
			self.right_viewbox.set_position(r_view)
			self.left_viewbox.set_position(l_view)
			self.left_viewbox.update()
			self.right_viewbox.update()
			
		elif self.xtilestart == 0:
			self.left_viewbox.set_position(-1)
			self.right_viewbox.set_position(r_view)
			self.left_viewbox.update()
			self.right_viewbox.update()
			
		elif self.xtilestart == map_x - 25:
			self.left_viewbox.set_position(l_view)
			self.right_viewbox.set_position(xwindow)
			self.left_viewbox.update()
			self.right_viewbox.update()

			
		for collision in empty_list:
			if collision == "top":
				if self.ytilestart >0:
					self.ytilestart -=1
					for item in character_objects:
						item.rect.y +=32
					for item in collidable_layer:
						item.rect.y +=32
			elif collision == "bottom":
				if self.ytilestart < map_y-20:
					self.ytilestart +=1
					for item in character_objects:
						item.rect.y -=32
					for item in collidable_layer:
						item.rect.y -=32
			elif collision == "left":
				if self.xtilestart >0:
					self.xtilestart -=1
					for item in character_objects:
						item.rect.x +=32
					for item in collidable_layer:
						item.rect.x +=32
			elif collision == "right":
				if self.xtilestart < map_x -25:
					self.xtilestart +=1
					for item in character_objects:
						item.rect.x -=32
					for item in collidable_layer:
						item.rect.x -=32
		tilex = self.xtilestart
		tiley = self.ytilestart
		self.placex,self.placey = 0,0
		tiles = True
		while tiles:#while there are still tiles
			#print(tilex, self.xtilestart, tiley, self.ytilestart)
			#pdb.set_trace()
			image = (self.tmxdata.get_tile_image(tilex, tiley, 0))
			window.blit(image, [self.placex, self.placey])
			if self.placey == (ywindow-32) and self.placex == (xwindow-32):
				tiles = False
			elif self.placex == (xwindow-32):
				self.placey += 32
				tilex = self.xtilestart
				tiley += 1
				self.placex = 0
			else:
				tilex += 1
				self.placex += 32
		#self.xtilestart = self.xtile_placeholder#This gets changed a lot throughout the class, make sure to change it back
		#self.ytilestart = self.ytile_placeholder
		
		for item in collidable_objects:
			item.rect.x -= self.x_moved
			item.rect.y -= self.y_moved

class map_tile(pygame.sprite.Sprite):#returns 
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
class Viewbox(pygame.sprite.Sprite):
	def __init__(self, direction):#Direction should be top, bottom, right, or left.  Position should be the x/y pixel location
		super(Viewbox, self).__init__()
		pygame.sprite.Sprite.__init__(self)
		self.direction = direction
		if direction == "top" or direction == "bottom":
			self.image = pygame.Surface((xwindow,1))
		elif direction == "left" or direction == "right":
			self.image = pygame.Surface((1,ywindow))
		self.image.fill(colors["WHITE"])
		self.rect = self.image.get_rect()
		
			
	def set_position(self, integer):
		if self.direction == "top":
			self.rect.y = integer
			self.rect.x = 0
		elif self.direction == "bottom":
			self.rect.y = integer
			self.rect.x = 0
		elif self.direction == "left":
			self.rect.x = integer
			self.rect.y = 0
		elif self.direction == "right":
			self.rect.x = integer
			self.rect.y = 0
	def update(self):
		self.rect.x = self.rect.x
		self.rect.y = self.rect.y
		window.blit(self.image, self.rect)
		
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
	def change_speed(self,hchange,vchange):
		self.hspeed += hchange
		self.vspeed += vchange
		#if self.hspeed or self.vspeed !=0:
		#	self.moveblock += 8
	
	def set_position(self,x,y):
		self.rect.x = x
		self.rect.y = y
	
	def change_picture(self):
		#Check for direction
		#when not moving picture should be facing last direction user was facing
		#Make 
		
	def update(self, collidable, viewbox_empty):
		self.viewbox_collision = viewbox_empty
		self.rect.x += self.hspeed
		move = True
		collision_list = pygame.sprite.spritecollide(self, collidable, False)
		for object in collision_list:
			if object in collidable_layer:
				move = False
		for collided_object in collision_list:
			if collided_object == left_viewbox:
				#for object in collision
				if not move == False:
					self.viewbox_collision.append("left")
			elif collided_object == right_viewbox:
				if not move == False:
					self.viewbox_collision.append("right")
				#self.rect.right = (collided_object.rect.left-32)
			if self.hspeed > 0:
				self.rect.right = collided_object.rect.left
				if collided_object != right_viewbox:
					if "right" in self.viewbox_collision:
						self.viewbox_collision.remove("right")
			elif self.hspeed < 0:
				self.rect.left = collided_object.rect.right
				if collided_object != left_viewbox:
					if "left" in self.viewbox_collision:
						self.viewbox_collision.remove("left")
					
		self.rect.y += self.vspeed
		collision_list = pygame.sprite.spritecollide(self, collidable, False)
		move = True
		for object in collision_list:
			if object in collidable_layer:
				move = False
		for collided_object in collision_list:
		
			if collided_object == top_viewbox:
				if not move == False:#self.rect.top = (collided_object.rect.bottom+32)
					self.viewbox_collision.append("top")
			elif collided_object == bottom_viewbox:
				if not move == False:
					self.viewbox_collision.append("bottom")
				
			if self.vspeed > 0:
				self.rect.bottom = collided_object.rect.top
				if collided_object != bottom_viewbox:
					if "bottom" in self.viewbox_collision:
						self.viewbox_collision.remove("bottom")
						
			elif self.vspeed < 0:
				self.rect.top = collided_object.rect.bottom
				if collided_object != top_viewbox:
					if "top" in self.viewbox_collision:
							self.viewbox_collision.remove("top")
	#	self.rect.x += self.hspeed
	#	self.rect.y += self.vspeed
		window.blit(self.image, self.rect)

xloc = 416
yloc = 320
enemyxloc = 64*4
enemyyloc = 64*4

MAP = "tiledstuff1.tmx"
big_map = "MASSIVEMAP.tmx"
little_map = "25x20test.tmx"
m25x40 = "20x40.tmx"
m50x20 = "50x20.tmx"

map_x = 600
map_y = 480


#map_collisions = place_tiles("tiledstuff1.tmx", xwindow, ywindow)

ninja = Player(xwindow, ywindow)#(self, filename, xloc, yloc)
ninja.set_image(imagelocation,"ninja32px.png")
ninja.set_position(xloc,yloc)

overworld = map(imagelocation, big_map, ninja)
#overworld.load_entire_map(map_x,map_y,0)#do one less than map size?
overworld_collisions = overworld.collision_layer()

first_enemy = Enemy(xwindow, ywindow)
first_enemy.set_image(imagelocation, "redenemy.png")
first_enemy.set_position(64,64)

second_enemy = Enemy(xwindow, ywindow)
second_enemy.set_image(imagelocation, "redenemy.png")
second_enemy.set_position(128,128)


collidable_objects = pygame.sprite.Group()
character_objects = pygame.sprite.Group()
collidable_layer = pygame.sprite.Group()

top_viewbox = Viewbox("top")
bottom_viewbox = Viewbox("bottom")
right_viewbox = Viewbox("right")
left_viewbox = Viewbox("left")

top_viewbox.set_position(t_view)
bottom_viewbox.set_position(b_view)
left_viewbox.set_position(l_view)
right_viewbox.set_position(r_view)
overworld.set_viewbox(top_viewbox, bottom_viewbox, left_viewbox, right_viewbox)
#set_viewbox(self, top, bottom, left, right):

for item in overworld_collisions:
	add_collision = map_tile(item)#class that does map collisions, haven't expanded it yet.
	collidable_layer.add(add_collision)#add the rectangles made in the above function into collision layer
	
character_objects.add(first_enemy, second_enemy)
collidable_objects.add(first_enemy,second_enemy,top_viewbox,bottom_viewbox,left_viewbox,right_viewbox, collidable_layer)



#xloc = xloc/32
#yloc = yloc/32
xloc = 0
yloc = 0
empty_list = []
frame_counter = 0
while active:
#filename, xwindow, ywindow, xposition, yposition, replace_tiles
	for event in pygame.event.get():
		action = pygame.key.get_pressed()
		if event.type == pygame.QUIT:
			pygame.quit()
		#pygame.time.delay(120)
		if event.type == pygame.KEYDOWN:#change_speed(self,hchange,vchange)
			if event.key == pygame.K_w:
				ninja.change_speed(0,-32)

				
			if event.key == pygame.K_s:
				ninja.change_speed(0,32)

				
			if event.key == pygame.K_a:
				ninja.change_speed(-32,0)

				
			if event.key == pygame.K_d:
				ninja.change_speed(32,0)

				
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				ninja.change_speed(0,32)

			if event.key == pygame.K_s:
				ninja.change_speed(0,-32)

			if event.key == pygame.K_a:
				ninja.change_speed(32,0)

			if event.key == pygame.K_d:
				ninja.change_speed(-32,0)

		event = None
	overworld.load_player_section()
	top_viewbox.update()
	bottom_viewbox.update()
	left_viewbox.update()
	right_viewbox.update()
	empty_list = []
	ninja.update(collidable_objects, empty_list)
	first_enemy.update()
	second_enemy.update()

	pygame.display.update()
	clock.tick(30)	#FPS
	
	
	
	
