#This is the base code for the menus, can be copy pasted where it is needed in the final project or imported.
# if you want to use this by itself import pygame.  
#It doesn't here because the files that import this already import Pygame, and there's no reason to import it twice
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

def menuList(menumap = ["Item1","Item2","Item3","Item4","Item5","Item6","Item7","Item8","Item9","Item10","Item11"]):
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
	
	
#--

def runMenu():
	menuopen = True
	while menuopen:
		menuOp = menuOpen([["Items","Stats","Skills","Quest"],["Map","Party","Return"]])
		if menuOp == "Items":
			menuList(["Item1","Item2","Item3","Item4","Item5","Item6","Item7","Item8","Item9","Item10","Item11"])
		elif menuOp == "Stats":
			do = None #Add code here later
		else:
			menuopen = False