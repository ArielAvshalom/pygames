from random import randint
from string import digits

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print("Hello Mortal I am Py")

def num_pick(pos):
	return randint(0,pos)

def checker(num_chosen, num_target):

	if num_chosen == num_target:
		print(f"{bcolors.OKGREEN}you got it bro!\n{bcolors.ENDC}")
		return 1
	if num_chosen < num_target:
		print(f"{bcolors.WARNING}Try a higher number\n{bcolors.ENDC}")
		return 0
	if num_chosen > num_target:
		print(f"{bcolors.OKBLUE}Try a lower number\n{bcolors.ENDC}")
		return 0

def main():

#correct stands fo user input. If the user input is numeric it'll be 1.
	play = 1
	while play == 1:
		value = 0
		target_power = randint(0,20)
		print("upper limit is ", 2**target_power)
		target = num_pick(2**target_power)
		while value == 0:
			correct = 1
			chosen = input("Choose a number:\n")
			if chosen is not '':
				for pos in chosen:
					if correct == -1:
						continue
					if pos not in digits:
						correct = -1
						chosen = -1
						print("Choose a number not other weird things")
				chosen = int(chosen)
			else:
				correct = -1
			if correct != -1:
				value = checker(chosen, target)

		play_again = input("Would you like to play again? \t [y/n]")
		if play_again == 'y':
			play = 1
		else:
			play = 0
			print("exiting")


if __name__ == "__main__":

	main()
