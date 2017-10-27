import random
#CELLS = []
CELL_MAP = []
class map():
	def __init__(self):
		super(map,self).__init__()
		self.map_dimensions = ()
		self.times_done = 0
		
	def map_size(self, size_choice1="wide", size_choice2="Width"):
		while self.times_done != 2:
			m_size = input(("How {} would you like the map to be?\n(Range is 3-10 Tiles)\n({} must be an integer)\n>").format(size_choice1, size_choice2))
			try:
				if int(m_size) >= 3:
					self.times_done +=1
					self.map_dimensions += ((m_size),)
					if self.times_done == 2:
						self.map_width,self.map_height = self.map_dimensions
					elif size_choice1 == "wide":
						self.map_size("tall", "height")
					#else:
					#	self.map_width,self.map_height = self.map_dimensions
					#	self.get_locations()
						#self.draw_map()
						#return("Yes")
			except:
				print("Invalid input.  Try again!\n(Hint: try a number, genius.)")
		self.get_locations()
				
	def draw_map(self):
		self.tiles = [
			"|X|",
			"| |"]
		for (tuple) in self.CELLS:
			if tuple == self.player:
				CELL_MAP.append(self.tiles[0])
			else:
				CELL_MAP.append(self.tiles[1])
		count_x = 0
		print(CELL_MAP)
	def get_locations(self):
		self.CELLS = []
		self.map_width,self.map_height = int(self.map_width),int(self.map_height)
		self.map_dimensions = (self.map_width),(self.map_height)
		tiles = (int(self.map_width)*int(self.map_height))
		tilex,tiley = 0,0
		while tiles != 0:
			#if tilex == self.map_width and tiley == self.map_height-1:
			if tilex == self.map_width:
				tilex = 0
				tiley +=1
			elif tilex < (self.map_width):
				self.CELLS.append((tilex,tiley))
				tilex +=1
			tiles -=1
		self.monster = self.monsterx, self.monstery = random.choice(self.CELLS)
		self.door = self.doorx, self.doory = random.choice(self.CELLS)
		self.player = self.playerx, self.playery = random.choice(self.CELLS)
		if self.monster == self.door or self.monster == self.player or self.door == self.player:
			self.get_locations()
		else:
			self.draw_map()		

	def move_player(self,move):
		if move == "LEFT":
			self.playerx -= 1
		elif move == "RIGHT":
			self.playerx += 1
		elif move == "UP":
			self.playery -= 1
		elif move == "DOWN":
			self.playery += 1
		#return player
		
	def get_moves(self):
		MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
		if playery == 0:
			MOVES.remove("LEFT")
		if playerx == 0:
			MOVES.remove("UP")
		if playery == player_map.map_height-1:
			MOVES.remove("RIGHT")
		if playerx == player_map.map_width-1:
			MOVES.remove("DOWN")
		return MOVES
		
player_map = map()
player_map.map_size()

cycle = 0
while True:
	cycle += 1
	if cycle == 1:
		print("Welcome to the dungeon!")
	
	#print("You're currently in room {}".format(str(player_map.player))) # fill in with player position
	print("You can move {}".format(player_map.get_moves(player))) # fill in with available moves
	print("Enter QUIT to quit")

	move = (input("> ")).upper()

	if move == 'QUIT':
		break
	elif moves in player_map.get_moves():
		player_map.move_player()
	elif moves not in player_map.get_moves():
		print("Error, you tried to walk through the dungeon's walls.  Try again.")

# If it's a good move, change the player's position
# If it's a bad move, don't change anything
# If the new player position is the door, they win!
# If the new player position is the monster, they lose!
# Otherwise, continue