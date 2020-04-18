# This will be my first game... 
#

import random
import sys
import os
import time

os.system('clear')
name = input("Please write your name: ")

# ***** GAME HELP MENU *****

def game_information():
	print(""" 

-------     Help Menu     ------- 

This information will help you for the rules. 
Game has 3 elements and 3 conditions.
Rock, Paper and Scissors.

Rock crushes Scissors
Scissors cuts Paper
Paper cover Rock.

Game will ask you to input your choice and result will be printed.
to choice an element press;

R for Rock
P for Paper
S for Scissors

-------     Good Luck     -------

""")
	time.sleep(3)

# ***** GAME MAIN MENU *****

def main_menu():
	print("\nHello, " + name + """\nWelcome to Rock, Paper, Scissors game.

----Main Menu---

Press 1 for Help.
Press 2 for Play.
Press 3 for Quit.

""")

	menu_selection_word = input("please select your option: \n")
	try:
		menu_selection_int = int(menu_selection_word)
		print("you have selected: ", menu_selection_int)
	except ValueError:
		print(" Invalid selection")
		main_menu()
	
	if menu_selection_int == 1:
		os.system('clear')
		game_information()
		main_menu()
	elif menu_selection_int == 2:
		play_game()
	elif menu_selection_int == 3:
		game_quit()
	else:
		print("Invaild selection \n")
		main_menu()

# ***** REPEAT GAME *****

def repeat_game():	
	repeat_game_selection = input("""
Please select 
1 - New game
2 - Quit \n""")
	try:
		repeat_game_select = int(repeat_game_selection)
	except ValueError:
		print(" Invalid selection")
		repeat_game()
	if repeat_game_select == 1:
		print("New Game begins \n")
		play_game()
	elif repeat_game_select == 2:
		game_quit()
	else:
		print("Invaild selection \n")
		repeat_game()

# ***** GAME QUIT *****

def game_quit():
	os.system('clear')
	sys.exit("Thank you for Playing. See you next time!")

# ***** Play GAME *****

def play_game():
	player_selection_input = input("Please Select your Element. \nR for Rock\nP for Paper\nS for scissors \n")
	
	if player_selection_input == "R" or player_selection_input == "r":
		print("You have selected Rock")
	elif player_selection_input == "S" or player_selection_input == "s":
		print("You have selected Scissors")

	elif player_selection_input == "P" or player_selection_input == "p":
		print("You have selected Paper")
	else:
		print("Invaild selection \n")
		play_game()

	comp_random = ["R", "r", "S", "s", "P", "p"]
	comp_selection = random.choice(comp_random)
	time.sleep(1)
	if comp_selection == "R" or comp_selection == "r":		
		print("Computer Selected: Rock")
	elif comp_selection == "P" or comp_selection == "p":		
		print("Computer Selected: Paper")
	else:		
		print("Computer Selected: Scissors")
	
	if player_selection_input == "R" or player_selection_input == "r":
		if comp_selection == "S" or comp_selection == "s":
			print("Your Rock crushed computer's scissors! You Won!")			
			time.sleep(2)
		elif comp_selection == "R" or comp_selection == "r":
			print("It is a tie!")
			time.sleep(2)
		else:
			print("Computer's Paper covered your Rock! You Lost!")			
			time.sleep(2)
	elif player_selection_input == "S" or player_selection_input == "s":
		if comp_selection == "S" or comp_selection == "s":
			print(" It is a tie!")
			time.sleep(2)
		elif comp_selection == "R" or comp_selection == "r":
			print("Computer's Rock crushed your Scissors. You Lost!")
			time.sleep(2)
		else:
			print("Your Scissors cut computer's Paper. You Won!")
			time.sleep(2)
	elif player_selection_input == "P" or player_selection_input == "p":
		if comp_selection == "R" or comp_selection == "r":
			print("Your Paper covered computer's Rock. You Won!")
			time.sleep(2)
		elif comp_selection == "S" or comp_selection == "s":
			print("Computer's Scissors cut your Paper. You Lost!")
			time.sleep(2)
		else:
			print(" It is a tie!")
			time.sleep(2)	
	return repeat_game()
main_menu()


