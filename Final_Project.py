#Sobczak - Final Project: Pokemon Battle 

#User and computer take turns selecting moves to use against each other. Both players start out with 100 health and can choose between three moves

#Attack ranges: Big attack = -10 hp, small attack = -5 hp, heal = +3hp. 

#After each move, print out what move the user did and how much health the user and computer have.

#Game ends when a player reaches 0 health.

#When someone wins, make sure the game prints out that their health is 0, not a negative number

#Extra goals: 1) add blocking move 2) include mana usage and regen 3)First move deals medium damage (between 5 and 10).Second move deals high or low damage (10 - 35). Third move heals a moderate amount (between 5-10).

#Initial character input/rules
print "Welcome to the PokeGym!"
player = raw_input("Which Pokemon do you choose?")
print "You have chosen", player, "!\n"
print "In order to defeat your enemy, command", player, "to either attack for a \n small amount, attack for a high amount, \n or heal yourself for a moderate amount.\n When you or your enemy reach 0 health the game is over!"
print "Good luck,", player + "." + " " + "Let the game begin!\n You have 100 health.\n"


#class of character, describes how hp changes depending on attack or heal. describes condition in which the player is alive.)
class Character(object):
	STARTING_HP = 100
	SMALL_ATTACK_HP_LOSS = 5
	BIG_ATTACK_HP_LOSS = 10
	HEAL_HP_GAIN = 3
	def __init__(self, player):
		self.player = player
		self.hp = self.STARTING_HP
	def small_attack(self, other_player):
		other_player.hp -= self.SMALL_ATTACK_HP_LOSS
	def big_attack(self, other_player):
		other_player.hp -= self.BIG_ATTACK_HP_LOSS
	def heal(self):
		self.hp += self.HEAL_HP_GAIN
	def alive(self):
		return self.hp > 0
	def dead(self):
		return self.hp <= 0

player = Character('Player 1')
computer = Character('Computer')


#identifying who's turn it is/who goes first

import random
turn = random.randint(1,2) 
if turn == 1:
	player_turn = True
	computer_turn = False 
	print "\n Player 1 will go first."
else:
	player_turn = False
	computer_turn = True
	print "\n Computer will go first."

player_1_health = player.hp
computer_health = computer.hp


while player.alive() and computer.alive():
	if player_turn:
		player_move = raw_input("\nPlease select a move: \n 1. Large Attack (Deal 10 damage)\n 2. Small Attack (Deal 5 damage)\n 3. Heal (Restore 3 health to your Pokemon\n")
		if player_move == "1":
			player_move = player.big_attack(computer)
			#print "You used Big Attack and dealt 10 damage to your enemy.\n"
		elif player_move == "2":
			player_move = player.small_attack(computer)
			print "You used Small Attack and dealt 5 damage to your enemy.\n"
			#print "Enemy now has", computer_health + "health."
		elif player_move == "3":
			player_move = player.heal()
			print "You used Heal and restored 3 health to your Pokemon."
			#print "You have", player_1_health + "health."
		else:
			print "Not a valid move. Please try again."
	else: #computer turn
		if computer.hp >= 25 and player.hp > 50:
			move = computer.big_attack(player)
			print "\n The Computer used Big Attack. It dealt 10 damage."	
		elif computer.hp >= 25 and player.hp <= 25:
			move = computer.small_attack(player)
			print "\n The computer used Small Attack. It dealt 5 damage." 
		elif computer.hp < 25 and player.hp >= 15:
			move = computer.heal() 
			print "\n The computer restored 3 health to it's Pokemon."
		else:
			move = computer.big_attack(player)
			print "\n The computer used Big Attack. It dealt 10 damage."
	print "\nPlayer 1 has:", player.hp, "\nComputer has:", computer.hp, "\n"
	player_turn = not player_turn
	computer_turn = not computer_turn

#player.big_attack(computer) - how you actually change the players' health using the class / methods done above

def get_winner_message():
	if player.dead() and computer.alive():
		return "Oh bollocks, you have been defeated!"
	elif computer.dead() and player.alive():
		return "Congratulations!\nYou win!"
	else:
		return "Player 1 Heath:", player_1_health, "Computer Health:", computer_health
print get_winner_message()








