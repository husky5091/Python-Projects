# for github projects
from random import randint
import time
minim = 1
maxim = 6
def singleplayer():
	print("[Ol' Bot]: You selected the singleplayer mode."), print("[Ol' Bot]: The game begins in 3 seconds !"), time.sleep(3), print("[Ol' Bot]: Type 'roll' when you are ready to roll the dice !")
	readyroll = input("[Player]: ")
	if (readyroll == "roll"):
		print("[Ol' Bot]: The player is rolling the dice..."), time.sleep(2), print("[Ol' Bot]: The player has rolled the dice. The dice value is:", randint(minim, maxim), "!\n")
	playagain = input("[Ol' Bot]: Would you like to play again ? (Y/N): ")
	print("\n")
	if(playagain == 'N' or playagain == 'n'):
		print("[Ol' Bot]: Sorry to hear that ! See you later !")
		quit()
def multiplayer():
	print("[Ol' Bot]: You selected the multiplayer mode.")
	players = input("[Ol' Bot]: How many players will play the game ? (1 (will redirect you to singleplayer)/2/3/4): ")
	if (players == "1"):
		singleplayer()
	elif (players == "2"):
		twoplayers()
	elif (players == "3"):
		threeplayers()
	elif (players == "4"):
		fourplayers()
def twoplayers():
	print("[Ol' Bot]: You selected 2 players. The game begins in 5 seconds !"), time.sleep(5), print("[Ol' Bot to Player 1:] Type 'roll' when you are ready to roll !")
	readyroll = input("[Player 1]: ")
	if (readyroll == "roll"):
		print("[Ol' Bot]: Player 1 is rolling the dice..."), time.sleep(2), print("[Ol' Bot]: Player 1 has rolled the dice. The dice value is:", randint(minim, maxim), "!\n"), print("[Ol' Bot to Player 2:] Type 'roll' when you are ready to roll the dice !")
	readyroll = input("[Player 2]: ")
	if (readyroll == "roll"):
		print("[Ol' Bot]: Player 2 is rolling the dice..."), time.sleep(2), print("[Ol' Bot]: Player 2 has rolled the dice. The dice value is:", randint(minim, maxim), "!\n"), print("[Ol' Bot]: The game is over !")
	playagain = input("[Ol' Bot]: Would you like to play again ? (Y/N): ")
	print("\n")
	if (playagain == 'N' or playagain == 'n'):
		print("[Ol' Bot]: Sorry to hear that ! See you later !")
		quit()
def threeplayers():
	print("[Ol' Bot]: You selected 3 players. The game begins in 5 seconds !"), time.sleep(5), print("[Ol' Bot to Player 1:] Type 'roll' when you are ready to roll !")
	readyroll = input("[Player 1]: ")
	if (readyroll == "roll"):
		print("[Ol' Bot]: Player 1 is rolling the dice..."), time.sleep(2), print("[Ol' Bot]: Player 1 has rolled the dice. The dice value is:", randint(minim, maxim), "!\n"), print("[Ol' Bot to Player 2:] Type 'roll' when you are ready to roll the dice !")
	readyroll = input("[Player 2]: ")
	if (readyroll == "roll"):
		print("[Ol' Bot]: Player 2 is rolling the dice..."), time.sleep(2), print("[Ol' Bot]: Player 2 has rolled the dice. The dice value is:", randint(minim, maxim), "!\n"), print("[Ol' Bot to Player 3:] Type 'roll when you are ready to roll the dice !")
	readyroll = input("[Player 3]: ")
	if (readyroll == "roll"):
		print("[Ol' Bot]: Player 3 is rolling the dice..."), time.sleep(2), print("[Ol' Bot]: Player 3 has rolled the dice. The dice value is:", randint(minim, maxim), "!\n"), print("[Ol Bot]: The match is over !")
	playagain = input("[Ol' Bot]: Would you like to play again ? (Y/N): ")
	print("\n")
	if (playagain == 'N' or playagain == 'n'):
		print("[Ol' Bot]: Sorry to hear that ! See you later !")
		quit()
def fourplayers():
	print("[Ol' Bot]: You selected 4 players. The game begins in 5 seconds !"), time.sleep(5), print("[Ol' Bot to Player 1:] Type 'roll' when you are ready to roll !")
	readyroll = input("[Player 1]: ")
	if (readyroll == "roll"):
		print("[Ol' Bot]: Player 1 is rolling the dice..."), time.sleep(2), print("[Ol' Bot]: Player 1 has rolled the dice. The dice value is:", randint(minim, maxim), "!\n"), print("[Ol' Bot to Player 2:] Type 'roll' when you are ready to roll the dice !")
	readyroll = input("[Player 2]: ")
	if (readyroll == "roll"):
		print("[Ol' Bot]: Player 2 is rolling the dice..."), time.sleep(2), print("[Ol' Bot]: Player 2 has rolled the dice. The dice value is:", randint(minim, maxim), "!\n"), print("[Ol' Bot to Player 3:] Type 'roll' when you are ready to roll the dice !")
	readyroll = input("[Player 3]: ")
	if (readyroll == "roll"):
		print("[Ol' Bot]: Player 3 is rolling the dice..."), time.sleep(2), print("[Ol' Bot]: Player 3 has rolled the dice. The dice value is:", randint(minim, maxim), "!\n"), print("[Ol Bot to Player 4:] Type 'roll' when you are ready to roll the dice !")
	readyroll = input("[Player 4]: ")
	if (readyroll == "roll"):
		print("[Ol' Bot]: Player 4 is rolling the dice..."), time.sleep(2), print("[Ol' Bot]: Player 4 has rolled the dice. The dice value is:", randint(minim, maxim), "!\n"), print("[Ol Bot]: The match is over !")
	playagain = input("[Ol' Bot]: Would you like to play again ? (Y/N): ")
	print("\n")
	if (playagain == 'N' or playagain == 'n'):
		print("[Ol' Bot]: Sorry to hear that ! See you later !")
		quit()
def main():
	print("[Ol' Bot]: Hi there ! My name is Ol'Bot and I am the administrator of Ol' Roll ! What is your name ?")
	name = input("[Player]: Hi, Ol' Bot ! My name is ")
	print("[Ol' Bot]: Nice to meet you,", name, "! Welcome to my game !")
	gamemode = input("[Ol' Bot]: Please select the game mode: 1 - singleplayer, 2 - multiplayer: ")
	if (gamemode == "1"):
		singleplayer()
	elif (gamemode == "2"):
		multiplayer()
	else:
		print("[Ol' Bot]: An error has occured ! ")
		playagain = input("[Ol' Bot]: Would you like to try again ?")
		if (playagain == 'N' or playagain == 'n'):
			print("[Ol' Bot]: Sorry to hear that ! See you later !")
			quit()
playagain = 'Y'
while(playagain == 'Y'):
	main()
