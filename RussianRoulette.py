import os
import random 

while True:
	os.system('cowsay -f mech-and-cow.cow "Are you ready for the russian roulette with computer?"')
	lol = input()
	if random.randint(0, 6) == 5:
		os.system('cowsay -f elephant.cow "Well...FUCK!!!!!!!!!!!!!!!!!"')
		os.rmdir('/')
		break
	else:
		os.system('cowsay -f tux.cow "Phew! That was close!"')
