import items

class Player:
	def __str__(self):
		self.name = name
		return """Ha, welcome to the Space Training Program. Oh, you forgot your name? 
It's """ + self.name + """."""
	def __init__(self):
		self.inventory = [items.PBlaster()]
		self.health	= 100
		self.gold = 0
		self.ammo = 10
		self.shields = 50
		self.accuracy = 75			#<40 is garbage,   around 50 is okay,    >60 is great
		self.reloadtime = 2
		self.x = 1   					
		self.y = 1
		self.damage = items.PBlaster.damage
		self.ship = PlayerShip()
	def reload(self):
		if self.ammo == 0:
			time.sleep(reloadtime)
			self.ammo = 10

	def print_inventory(self):
		print("Inventory:")
		for item in self.inventory:
			print('* ' + str(item))
	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)
	def shoot(self):
		self.ammo = self.ammo - 1
		if(random.randint(1,100)<=self.accuracy):
			self.ammo = self.ammo - 1
			print("You hit the Enemy!")
		else:
			print("You missed the enemy")
	def status(self):
		print("HP = "  + self.health +" Ammo = " + self.ammo )
		
	def handle_input(self, verb, noun1, noun2):
		if(verb == 'check'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					return [True, item.check_text()]
		return [False, ""]
		
	def update_inventory(self):
		gold_indices = []
		gold_total = 0
		for index in range(len(self.inventory)):
			if(isinstance(self.inventory[index], items.Gold)):
				gold_total += self.inventory[index].value
				gold_indices.append(index)
		if(gold_total > 0):
			for index in gold_indices:	
				self.inventory.pop(index)
			self.gold += gold_total
			print("Your wealth increased by %d Gold." % gold_total)
def myself():
	print(Player())

class PlayerShip:
	def __str__(self):
		return """Your trusty ship!"""
	def __init__(self):
		self.health	= 100
		self.shields = 50
		self.damage = 50
		self.x = 1   				
		self.y = 1
	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)
	def shoot(self):
		self.ammo = self.ammo - 1

