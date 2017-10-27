import pygame, pytmx, tiledtmxloader, os

pygame.init()
pygame.display.set_caption("The Last Ninja ")

#global cam_world_pos_x,cam_world_pos_y
cam_world_pos_x = 0
cam_world_pos_y = 0

##########
#--MENU--#
##########
global font
font = pygame.font.SysFont('Century Gothic Bold',32)
def menuOpen(menumap = []):
	global font
	global screen
	screenPause = pygame.Surface.copy(screen)
	screenRect = screenPause.get_rect()
	loop = True
	cWhite = (255,255,255)
	cYellow = (255,255,0)
	selection = [0,0]
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					selection[0] += 1
				if event.key == pygame.K_UP:
					selection[0] += -1
				if event.key == pygame.K_LEFT:
					selection[1] += -1
				if event.key == pygame.K_RIGHT:
					selection[1] += 1
				if event.key == pygame.K_RETURN:
					loop = False
				if event.key == pygame.K_ESCAPE:
					return None
		if loop == False:
			continue
		if selection[0] > len(menumap)-1:
			selection[0] = 0
		elif selection[0] < 0:
			selection[0] = len(menumap)-1
		if selection[1] > len(menumap[selection[0]])-1:
			selection[1] = 0
		elif selection[1] < 0:
			selection[1] = len(menumap[selection[0]])-1
		y=0
		screen.blit(pygame.image.load(os.getcwd() + "\\Pictures\\UI\\textbox.png"),(0,0))
		for obj in menumap:
			x=0
			for obj2 in obj:
				if [y,x] == selection:
					screen.blit(font.render(menumap[y][x],False,cYellow),(10+(256*x),10+(64*y)))
				else:
					screen.blit(font.render(menumap[y][x],False,cWhite),(10+(256*x),10+(64*y)))
				x+=1
			y+=1
		pygame.display.flip()
	screen.blit(screenPause,screenRect)
	pygame.display.flip()
	return menumap[selection[0]][selection[1]]

#---

def menuList(menumap = []):
	global font
	global screen
	screenPause = pygame.Surface.copy(screen)
	screenRect = screenPause.get_rect()
	loop = True
	cWhite = (255,255,255)
	cYellow = (255,255,0)
	selection = 0
	ref = 0
	def incr(selection,ref,mv):
		if mv == 1:
			if selection == len(menumap)-1:
				return selection,ref
			elif selection > 2 and overlap[1] == True:
				ref += mv
		elif mv == -1:
			if selection == 0:
				return selection,ref
			elif selection < len(menumap)-3 and overlap[0] == True:
				ref += mv
		selection += mv
		return selection,ref
	if len(menumap) > 6:
		overlap = [False,True]
	else:
		overlap = [False,False]
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					selection,ref = incr(selection,ref,1)
				if event.key == pygame.K_UP:
					selection,ref = incr(selection,ref,-1)
				if event.key == pygame.K_RETURN:
					loop = False
				if event.key == pygame.K_ESCAPE:
					return None
		if loop == False:
			continue
		if ref > 0:
			overlap[0] = True
		else:
			overlap[0] = False
		if ref+6 < len(menumap):
			overlap[1] = True
		else:
			overlap[1] = False
		i = 0
		screen.blit(pygame.image.load(os.getcwd() + "\\Pictures\\UI\\listbox.png"),(0,0))
		while i < 6:
			if i + ref == selection:
				screen.blit(font.render(menumap[ref+i],False,cYellow),(10,64+64*(i)))
			else:
				screen.blit(font.render(menumap[ref+i],False,cWhite),(10,64+64*(i)))
			i+=1
		if overlap[0] == True:
			screen.blit(font.render("...",False,cWhite),(10,14))
		if overlap[1] == True:
			screen.blit(font.render("...",False,cWhite),(10,438))
		pygame.display.flip()
	screen.blit(screenPause,screenRect)
	pygame.display.flip()
	return menumap[selection]

#---
def runMenu():
	menuopen = True
	while menuopen:
		menuOp = menuOpen([["Items","Stats","Skills","Quest"],["Map","Party","Return"]])
		if menuOp == "Items":
			menuList(["Item1","Item2","Item3","Item4","Item5","Item6","Item7","Item8","Item9","Item10","Item11"])
		elif menuOp == "Stats":
			do = None #Add code here later
		elif menuOp == "Skills":
			do = None #Add code here later
		elif menuOp == "Quest":
			do = None #Add code here later
		elif menuOp == "Map":
			do = None #Add code here later
		elif menuOp == "Party":
			do = None #Add code here later
		else:
			menuopen = False
##########
#--MENU--#
##########

def render(map_location):
	world_map = tiledtmxloader.tmxreader.TileMapParser().parse_decode(map_location)
	screen_width = min(1024, world_map.pixel_width)
	screen_height = min(768, world_map.pixel_height)
	global screen
	screen = pygame.display.set_mode((screen_width, screen_height))
	
	resources = tiledtmxloader.helperspygame.ResourceLoaderPygame()
	resources.load(world_map)
	#prepare map rendering
	assert world_map.orientation == "orthogonal"
	
	renderer = tiledtmxloader.helperspygame.RendererPygame()
	global cam_world_pos_x,cam_world_pos_y	
	#cam_world_pos_x = 0
	#cam_world_pos_y = 0
	#global cam_world_pos_x,cam_world_pos_y
	renderer.set_camera_position_and_size(cam_world_pos_x, cam_world_pos_y, screen_width, screen_height, "topleft")
	sprite_layers = tiledtmxloader.helperspygame.get_layers_from_map(resources)
	rend_clock = pygame.time.Clock()
	running = True
	while running == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
				elif event.key == pygame.K_UP:
					movement(0, -32, 4)#cam_world_pos_y -= world_map.tileheight
				elif event.key == pygame.K_DOWN:
					movement(0, 32, 4)#					cam_world_pos_y += world_map.tileheight
				elif event.key == pygame.K_RIGHT:
					movement(32, 0, 4)#					cam_world_pos_x += world_map.tilewidth
				elif event.key == pygame.K_LEFT:
					movement(-32, 0, 4)#					cam_world_pos_x -= world_map.tilewidth
				elif event.key == pygame.K_p:
					runMenu()
					
		renderer.set_camera_position(cam_world_pos_x, cam_world_pos_y, "topleft")
		screen.fill((0, 0, 0))
		for sprite_layer in sprite_layers:
			if sprite_layer.is_object_group:
				continue
			else:
				renderer.render_layer(screen, sprite_layer)
		pygame.display.flip()
		rend_clock.tick(30)
		
def movement(offset_x, offset_y, movement_nums):

	global cam_world_pos_x,cam_world_pos_y
	clock = pygame.time.Clock()
	while movement_nums > 0:
		if offset_x != 0:
			cam_world_pos_x += (offset_x/movement_nums)
		if offset_y != 0:
			cam_world_pos_y += (offset_y/movement_nums)
		movement_nums -= 1
		pygame.display.flip()
		clock.tick(30)
	
	
def game():
	clock = pygame.time.Clock()
	running = True
	while running:
		for event in pygame.event.get():
			action = pygame.key.get_pressed()
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				#if event.key == pygame.K_p:
					
			#if event.type == pygame.KEYUP:
				event = None

		pygame.display.update()
		clock.tick(30)	#FPS
render(os.getcwd() + "\\Pictures\\Maps\\MASSIVEMAP.tmx")
#game()












