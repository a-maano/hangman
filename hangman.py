import os
import assets as a



def updatePrompt(word):
	word_length = len(word)

	for i in range(word_length+1):
		if i == 0:
			print("┌─",end="")
		elif i != word_length:
			print("┬─",end="")
		else:
			print("┐")

	for j in range(word_length):
		if j != word_length-1:
			print("│"+word[j],end="")
		else:
			print("│"+word[j]+"│")

	for i in range(word_length+1):
		if i == 0:
			print("└─",end="")
		elif i != word_length:
			print("┴─",end="")
		else:
			print("┘")

def menu(details):
	if details == "Congrats! You did it!":
		print(a.hanger[9])
		print(a.winner)
	elif details == "Better luck next time!":
		print(a.hanger[8])
		print(a.loser)
	print("[1] Play Hangman")
	print("[2] Exit\n")

	print(details)

	print("What do you want to do? ")
	choice = input()

	return choice

def updateLetters(secret, word, letter):
	indices = [i for i, x in enumerate(word) if x == letter]
	for i in indices:
		secret[i] = letter

	return secret

def resizeTerminal(row,col):
	print('\x1b[8;{0};{1}t'.format(row, col), end='', flush=True)

def play(word, secret):

	chance = 0 #max chance is 7
	letters_guessed = []
	guess = ""
	details = ""
	prev_guess = word[1]

	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		print(a.title)
		
		if chance == 8:
			return "Better luck next time!"

		else:
			print(a.hanger[chance])
			updatePrompt(secret)

			print("\nLetters guessed:")
			print(letters_guessed)

			print(details)

			print("\n\nGuess a letter: ",end="")
			guess = input().upper()
			prev_guess = guess
			

			if len(guess) > 1 or not guess.isalpha():
				details = "Please only enter a single letter character!"
			else:
				if guess in letters_guessed:
					details = "You already have guessed letter " + guess +"!"
				else:
					letters_guessed.append(guess)
					if guess in word:
						secret = updateLetters(secret, word, guess)
					else:
						chance = chance + 1
					details = ""

				if "_" not in secret:
					return "Congrats! You did it!"


details = ""
resizeTerminal(32,62) #row, col
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print(a.title)
	choice = menu(details)
	if choice == "1":
		word = "meat balls"
		secret = ["_"]*len(word)
		secret = updateLetters(secret, word, " ")
		details = play(word.upper(),secret)

	elif choice == "2":
		print("Thanks for playing!")
		break
	else:
		details = "Invalid Input!"

