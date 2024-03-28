import os


hanger = [
"""
┌┬──────┐
││      
││
││ 
││
││
││
││
││
││
││
╧╧═══════════ 
""",
"""
┌┬──────┐
││      
││    ╭───╮
││    │•_•│
││    ╰───╯
││
││ 
││
││
││
││     
╧╧═══════════ 
""",
"""
┌┬──────┐
││      
││    ╭───╮
││    │•_•│
││    ╰─┬─╯
││      ┼
││      
││       
││
││
││
╧╧═══════════ 
""",
"""
┌┬──────┐
││      
││    ╭───╮
││    │•_•│
││    ╰─┬─╯
││     ╭┼
││     │
││       
││
││
││
╧╧═══════════ 
""",
"""
┌┬──────┐
││      
││    ╭───╮
││    │•_•│
││    ╰─┬─╯
││     ╭┼╮
││     │ │
││       
││
││
││
╧╧═══════════ 
""",
"""
┌┬──────┐
││      
││    ╭───╮
││    │•_•│
││    ╰─┬─╯
││     ╭┼╮
││     │││
││      ┴ 
││     
││
││
╧╧═══════════ 
""",
"""
┌┬──────┐
││      
││    ╭───╮
││    │•_•│
││    ╰─┬─╯
││     ╭┼╮
││     │││
││     ╭┴ 
││     │ 
││
││
╧╧═══════════ 
""",
"""
┌┬──────┐
││      
││    ╭───╮
││    │•_•│
││    ╰─┬─╯
││     ╭┼╮
││     │││
││     ╭┴╮ 
││     │ │
││
││
╧╧═══════════ 
""",
"""
┌┬──────┐
││      │
││    ╭─┴─╮
││    │x_x│
││    ╰─┬─╯
││     ╭┼╮
││     │││
││     ╭┴╮ 
││     │ │
││
││
╧╧═══════════ 
""",
"""
┌┬──────┐
││      │
││
││
││    ╭───╮
││    │•‿•│
││    ╰─┬─╯
││     ╭┼╮
││     │││
││     ╭┴╮ 
││     │ │
╧╧═══════════ 
"""
]



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



def menu():
	print("[1] Play Hangman")
	print("[2] Exit")
	print("What do you want to do? ")
	choice = input()

	return choice


def play(word, secret):
	# os.system('cls' if os.name == 'nt' else 'clear')
	chance = 0 #max chance is 7
	letters_guessed = []
	guess = ""

	while True:
		if chance == 8:
			print(hanger[8])
			print("You loose!")
			break

		else:
			print(hanger[chance])
			updatePrompt(secret)
			print("Guess a letter: ",end="")
			guess = input().upper()
			print("\n======================")

			if len(guess) > 1 or not guess.isalpha():
				print("Invalid input!")
			else:
				if guess in letters_guessed:
					print("You already have guessed that letter!")
				else:
					letters_guessed.append(guess)
					if guess in word:
						indices = [i for i, x in enumerate(word) if x == guess]
						for i in indices:
							secret[i] = guess
					else:
						chance = chance + 1

				if "_" not in secret:
					print(hanger[9])
					print("You win!")
					break
			print("Letters guessed:")
			print(letters_guessed)
			


while True:

	choice = menu()
	if choice == "1":
		word = "rizz"
		secret = ["_"]*len(word)
		play(word.upper(),secret)
	elif choice == "2":
		print("Thanks for playing!")
		break
	else:
		print("Invalid input!")
	# os.system('cls' if os.name == 'nt' else 'clear')
