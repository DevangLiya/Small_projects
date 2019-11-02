#!/usr/bin/env python3

#A silly terminal based game where user tries to add two numbers
#Tested only on Linux
#Author : Devang Liya
#Date   : 02/11/2019
#License: GPLv3

import signal
import random
import pandas as pd
import os

samay = 5	#Time for each answer

def alarm_handler(signum, frame):
    raise TypeError

def input_with_timeout(prompt, timeout):
    # set signal handler
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout) # produce SIGALRM in `timeout` seconds

    try:
        return input(prompt)
    finally:
        signal.alarm(0) # cancel alarm

def check_hs(u_name, u_score):
	prev_hs = pd.read_csv('leaderboard')	#Read the leaderboard file
	prev_hs = prev_hs.sort_values(by='score', ascending=False)	#Safety measure in case HS file is not sorted
	prev_hs = prev_hs.reset_index(drop = True)	#Reset index so that we can drop last score later

	if u_score > min(prev_hs['score']):
		if len(prev_hs['score']) == 10:
			#Drop least score if more than 10 high scores
			prev_hs = prev_hs.drop([9], axis=0)
		prev_hs = prev_hs.append(pd.DataFrame([[u_name, u_score]], columns=['name', 'score']), ignore_index=True)	#do we need ignore_index?
		
		new_hs = prev_hs.sort_values(by='score', ascending=False)
		new_hs = new_hs.reset_index(drop = True)
		
		print("Congratulations! You have made it to the leaderboard.")
		print(new_hs)
		
		new_hs.to_csv('leaderboard', index=False)
	return 1

def clear_hs():
	'''
	Clears the leaderboard
	'''
	with open('leaderboard','w') as f:
		f.write("name,score\nGod,0")

def main():
	print("  _____                           _____ _   ")
	print(" / ____|                         |_   _| |  ")
	print("| (___  _   _ _ __ ___  _ __ ___   | | | |_ ")
	print(" \\___ \\| | | | '_ ` _ \\| '_ ` _ \\  | | | __|")
	print(" ____) | |_| | | | | | | | | | | |_| |_| |_ ")
	print("|_____/ \\__,_|_| |_| |_|_| |_| |_|_____|\\__|")
	print("\n")
	u_score = 0
	print("You have {} seconds to guess the sum of the numbers appearing below.".format(samay))
	u_name = input("Please input your name and press enter when ready: ")
	print("\n")

	if u_name == 'G0d':
		clear_hs()

	while True:
		numbers = [random.randint(1,100) for i in range(2)]
		print(numbers)
		try:
			answer = int(input_with_timeout("What is your answer? ", samay))
		except TypeError:
			print("\nSorry, times up")
			break
		if answer == sum(numbers):
			print("Correct!\n")
			u_score = u_score + 1
		else:
			print("Hatt re!\n")
			break

	print("\n{}, your score was {}.".format(u_name, u_score))
	print("Game over")
	check_hs(u_name, u_score)

if __name__ == "__main__":
	again = ''
	while again != 'q':
		os.system('clear')
		main()
		again = input("Press any key to play again. Press `q` to exit.\n").lower()