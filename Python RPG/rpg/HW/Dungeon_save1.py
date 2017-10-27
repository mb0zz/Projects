import random,platform,os,time#importing some modules to make things easier
if platform.system() == "Windows":#just for clearing command line/terminal later on - logan showed me this
	clear_cmd = "cls"
else:
	clear_cmd = "clear"
os.system(clear_cmd)
class map():#Class with a bunch of functions.
	def __init__(self):#initializing class function
		super(map,self).__init__()#adding inheritance
		self.map_dimensions = ()#empty tuple for map x and y dimensions for map generation
		self.times_done = 0
		self.cycle = 0
		self.tiles = [
					" P_",
					" __",
					" __",
					" __"]#[" X|","  |","  |","  |"]#"Tiles"
	def map_size(self, size_choice1="wide", size_choice2="Width"):#function that lets the user set the map size_choice1
		os.system(clear_cmd)
		while self.times_done != 2:#function runs once then calls itself with different parameters
			m_size = input(("How {} would you like the map to be?\n(Range is 3-10 Tiles)\n({} must be an integer)\n>").format(size_choice1, size_choice2))
			try:#checking is user did bad input
				if int(m_size) >= 3 and int(m_size) <=10:
					self.times_done +=1
					self.map_dimensions += ((m_size),)
					if self.times_done == 2:
						self.map_width,self.map_height = self.map_dimensions
					elif size_choice1 == "wide":
						self.map_size("tall", "height")
			except:
				print("Invalid input.  Try again!\n(Hint: try a number, genius.)")#failsafe if user sucks at his job
		self.get_locations()
				
	def draw_map(self):#makes map
		global CELL_MAP#makes map global variable
		CELL_MAP = []
		for (tuple) in self.CELLS:#draws the map
			if tuple == self.player:
				CELL_MAP.append(self.tiles[0])
			elif tuple == self.monster:
				CELL_MAP.append(self.tiles[2])
			elif tuple == self.door:
				CELL_MAP.append(self.tiles[3])
			else:
				CELL_MAP.append(self.tiles[1])
		count_x = 1
		print_list = []
		for item in CELL_MAP:
			print_list.append(item)
			if count_x == self.map_width:
				for index in print_list:
					print(index, end="")
				print("\n")
				print_list = []
				count_x = 1
			else:
				count_x +=1
				
	def get_locations(self):
		self.CELLS = []
		self.map_width,self.map_height = int(self.map_width),int(self.map_height)
		self.map_dimensions = (self.map_width),(self.map_height)
		tilex,tiley = 0,0
		LIMIT = self.map_width*self.map_height

		while LIMIT+(self.map_width) >0:
			if tilex == self.map_width:
				tilex = 0
				tiley +=1
			elif tilex < (self.map_width):
				self.CELLS.append((tilex,tiley))
				tilex +=1
			LIMIT -=1
		if self.cycle == 0:
			self.monster = (self.monsterx,self.monstery) = random.choice(self.CELLS)
			self.door = (self.doorx,self.doory) = random.choice(self.CELLS)
			self.player = (self.playerx,self.playery) = random.choice(self.CELLS)
			if self.monster == self.door or self.monster == self.player or self.door == self.player:
				self.get_locations()
			else:
				self.cycle +=1	

	def move_player(self,move):
		if move == "LEFT":
			self.playerx -= 1
		elif move == "RIGHT":
			self.playerx += 1
		elif move == "UP":
			self.playery -= 1
		elif move == "DOWN":
			self.playery += 1
		
	def get_moves(self):
		MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
		if self.playerx == 0:
			MOVES.remove("LEFT")
		if self.playery == 0:
			MOVES.remove("UP")
		if self.playerx == player_map.map_width-1:
			MOVES.remove("RIGHT")
		if self.playery == player_map.map_height-1:
			MOVES.remove("DOWN")
		return MOVES
	def show_tiles(self):
		self.tiles = [
				" P_",
				" __",
				" M_",
				" D_"]
	def update(self):
		self.player = self.playerx,self.playery
		#self.monster = self.monsterx,self.monstery
player_map = map()
player_map.map_size()

def game():
	cycle = 0
	while True:
		os.system(clear_cmd)
		cycle += 1
		if cycle == 1:
			print("Welcome to the dungeon!\n")
		else:
			print("\n")
			
		try:
			player_map.update(),player_map.get_locations(),player_map.draw_map()
			
		except:
			player_map.get_locations(),player_map.draw_map()

		print("You can move {}".format(player_map.get_moves()),"\nEnter QUIT to quit\nEnter SHOW to cheat")
		
		if player_map.player == player_map.monster:
			ending("Lost")
		elif player_map.player == player_map.door:
			ending("Won")
		
		move = (input("> ")).upper()
		
		if move == 'QUIT':
			break
			
		elif move == "SHOW":
			player_map.show_tiles()
		
		elif move in player_map.get_moves():
			player_map.move_player(move)
		
		elif move not in player_map.get_moves():
			print("Error, you tried to walk through the dungeon's walls.  Try again.")
		
			
def ending(player_results):
	os.system(clear_cmd)
	player_map.show_tiles()
	if player_results == "Won":
		print("Congratulations, you have won!")
		animation("win")
		play_again = (input("Would you like to play again?\n(Y/N)")).lower()

	else:
		print("You have been eaten by the monster.")
		animation("lose")
		play_again = (input("Play again?\n(Y/N)"))
		
	if (play_again).startswith("y"):
		player_map = map()
		player_map.map_size()
		global player_map
		game()
	else:
		print("Thanks for playing.")
		exit()
		
def animation(type):
	if type == "win":
		try:
			os.system("color 2")
			time.sleep(1)
			os.system("color 9")
			time.sleep(1)
			os.system("color 2")
			time.sleep(1)
			os.system("color 7")
		except:
			None
	else:
		try:
			os.system("color 4")
			time.sleep(1)
			os.system("color C")
			time.sleep(1)
			os.system("color 4")
			time.sleep(1)
			os.system("color 7")
		except:
			None
game()
