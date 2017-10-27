import pygame, sys, pytmx, os, random, math, pdb
from pytmx import load_pygame
#in this version I'm shooting to make movement more realistic + accurate.
#Next will be player mechanics
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
#ninjaImg = pygame.image.load(str(imagelocation) + "\\ninja32px.png")#importing a local image
ninx = xwindow/2#where the image will be placed
niny = ywindow/2

#Fonts + text + text size
myfont = pygame.font.Font('freesansbold.ttf', 32)#using fonts and text
fontsurface = myfont.render("Hello world!", True, colors["GREEN"])#(Text to write, ?,Text color, surface.)
fontrect = fontsurface.get_rect()#Get rectangle to place font surface on?
fontrect.center = (ninx, 50)#don't know.  Just include this

#music
#pygame.mixer.music.load(musiclocation +"\Crusade.mp3")
#pygame.mixer.music.play(-1, 0.0)#Plays infinite times starting at 0.0

#object.play(), and object.stop() to start and stop sounds

#tmxdata = load_pygame("tiledstuff1.tmx")
#image = tmxdata.get_tile_image(0, 0, 0)
#tmxdata = pytmx.TiledMap("tiledstuff1.tmx")


#set_viewbox(self, top, bottom, left, right):
def set_cursor():
	cursor_strings = (#Really bad ninja star.
	"           XX           ",
	"          X..X          ",
	"         X.X..X         ",
	"         X.XX.X         ",
	"         X.XX.X         ",
	"        X.X..X.X        ",
	"        X.X..X.X        ",
	"        X.X..X.X        ",
	"     XXX.X....X.XXX     ",
	"   XX...XX....XX...XX   ",
	"  X..XXX..X..X..XXX..X  ",
	" X.XX......XX......XX.X ",
	" X..X......XX......X..X ",
	"  X..XXX..X..X..XXX..X  ",
	"   XX...XX....XX...XX   ",
	"     XXX.X....X.XXX     ",
	"        X.X..X.X        ",
	"        X.X..X.X        ",
	"        X.X..X.X        ",
	"         X.XX.X         ",
	"         X.XX.X         ",
	"         X.X..X         ",
	"          X..X          ",
	"           XX           ")
	cursor_ninja_star =(
 	"           X            ",
	"           XX           ",
	"           XX           ",
	"           XX           ",
	"          XXXX          ",
	"          XXXX          ",
	"          XXXX          ",
	"         XXXXXX         ",
	"         XXXXXX         ",
	"       XXXXXXXXXX       ",
	"    XXXXXXXXXXXXXXXX    ",
	"XXXXXXXXXXXXXXXXXXXXXXXX",
	" XXXXXXXXXXXXXXXXXXXXXX ",
	"    XXXXXXXXXXXXXXXX    ",
	"       XXXXXXXXXX       ",
	"         XXXXXX         ",
	"         XXXXXX         ",
	"          XXXX          ",
	"          XXXX          ",
	"          XXXX          ",
	"           XX           ",
	"           XX           ",
	"           XX           ",
 	"           X            ")
	
	ninja_star, mask = pygame.cursors.compile(cursor_ninja_star, black="X", white=".", xor="o")
	pygame.mouse.set_cursor((24,24), (0,0), ninja_star, mask)

class Menu_sprites(pygame.sprite.Sprite):
	def __init__(self, pic_path, pic_name):
		super(Menu_sprites, self).__init__()
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load((pic_path + "\\Menu crap\\" + pic_name))
		self.rect = self.image.get_rect()
		#self.center_x = self.rect.centerx + startpos[0]
		#self.center_y = self.rect.centery + startpos[1]
	
	def animation(self, startpos, endpos, animation_time):
		#def animation(self, startpos, ))
		#startpos and endpos are the starting and ending x and y positions
		#animation_time is how long you want the animation to take to occu in milliseconds
		self.animation_time = animation_time
		self.startpos = (startpos[0] - self.rect.centerx), (startpos[1] - self.rect.centery)
		self.endpos = (endpos[0] - self.rect.centerx), (endpos[1] - self.rect.centery)
		
		self.center_x = self.rect.centerx + startpos[0]
		self.center_y = self.rect.centery + startpos[1]
		
		self.start_x,self.start_y = self.startpos
		self.end_x, self.end_y = endpos
		
		if self.start_x != self.end_x:#if start_x is to the left, move it right
			self.x_diff = self.end_x - self.start_x
			self.x_change = round(((self.x_diff)/self.animation_time))

				
		if self.start_y != self.end_y:#if start_y is above, move it down
			self.y_diff = self.end_y - self.start_y
			self.y_change = round(((self.y_diff)/self.animation_time))


	def update(self):
		self.animation_time -= 1
		self.startpos = self.x_change,self.y_change
		#if self.
		if self.animation_time > 0:
			if (self.center_x + self.x_change > self.endpos[0]
				and self.center_x - self.x_change < self.endpos[0]):
				self.center_x = self.endpos[0]
			elif self.center_x != self.endpos[0]:
				self.center_x += self.y_change
			
			if (self.center_y + self.y_change > self.endpos[1]
				and self.center_y - self.y_change < self.endpos[1]):
				self.center_y = self.endpos[1]
			elif self.center_y != self.endpos[1]:
				self.center_y += self.y_change
				self.center_y += self.y_change
		self.startpos = self.x_change,self.y_change
		window.blit(self.image, (self.center_x,self.center_y))
			

class Menu():
	
	def __init__(self, imagelocation):
	
		self.image_location = imagelocation
		self.menu_background = pygame.Surface((800,640))
		self.menu_background_pic = pygame.image.load("{}\{}".format(self.image_location, "\Menu crap\mselect.png"))
		self.menu_main_background = pygame.image.load("{}\{}".format(self.image_location, "\Menu crap\mbackground_pic.png"))
		#self.menu_background.rect = self.menu_background.get_rect()
		
		self.font = pygame.font.SysFont("ariblk.ttf", 32)#self.font = pygame.font.Font("ariblk.ttf", 32)#pygame.font.match_font("font name") - to get the font
		self.font_surface = self.font.render("The Last Ninja", True, colors["BLACK"])
		self.font_rect = self.font_surface.get_rect()
		
		self.font_y = 640

		self.font_width = self.font_surface.get_width()

	def Main_menu(self):
		self.menu_x = 250
		self.menu_y = 640

	def update(self, object):
					
		window.blit(self.menu_main_background,(-200,0))
		window.blit(self.menu_background_pic, (self.menu_x,self.menu_y))
		self.mouse_x,self.mouse_y = pygame.mouse.get_pos()

start_menu = Menu(imagelocation)
start_menu.Main_menu()
set_cursor()
first_sprite = Menu_sprites(imagelocation, "mselect.png")
first_sprite.animation((0,0), (xwindow/2,ywindow/2),1000)#this is 4 seconds.  Don't ask how or why.
#((xwindow/2 - first_sprite.rect.centerx),(ywindow/2- first_sprite.rect.centery)), 400)
def main_menu():
	while active:
		for event in pygame.event.get():
			action = pygame.key.get_pressed()
			if event.type == pygame.QUIT:
				pygame.quit()
			#pygame.time.delay(120)
			if event.type == pygame.KEYDOWN:#change_speed(self,hchange,vchange)
				if event.key == pygame.K_UP:
					newsprite = Menu_sprites(imagelocation, "mselect.png")
					newsprite.animation((0,0), (xwindow, ywindow), 400)
			#if event.type == pygame.KEYUP:
				event = None
		start_menu.update("Main_menu")
		#first_sprite.animation((0,0), (200,200), 200)	
		first_sprite.update()
		try:
			newsprite.update()
		except:
			None
		pygame.display.update()
		clock.tick(30)	#FPS
main_menu()
	
	
'''
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
		window.blit(self.image, self.rect)'''
