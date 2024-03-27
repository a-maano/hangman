
hanger = [
"""
┌┬──────┐
││      │
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
"""
"""
┌┬──────┐
││      │
││    ╭─┴─╮
││    │•_•│
││    ╰─┬─╯
││
││ 
││
││
││
││     
╧╧═══════════ 
"""
"""
┌┬──────┐
││      │
││    ╭─┴─╮
││    │•_•│
││    ╰─┬─╯
││      ┼
││      │
││      ┴ 
││
││
││
╧╧═══════════ 
"""
"""
┌┬──────┐
││      │
││    ╭─┴─╮
││    │•_•│
││    ╰─┬─╯
││     ╭┼
││     ││
││      ┴ 
││
││
││
╧╧═══════════ 
"""
"""
┌┬──────┐
││      │
││    ╭─┴─╮
││    │•_•│
││    ╰─┬─╯
││     ╭┼╮
││     │││
││      ┴ 
││
││
││
╧╧═══════════ 
"""
"""
┌┬──────┐
││      │
││    ╭─┴─╮
││    │•_•│
││    ╰─┬─╯
││     ╭┼╮
││     │││
││     ╭┴ 
││     │ 
││
││
╧╧═══════════ 
"""
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
"""
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
# print(hanger[0])


def updatePrompt(word):
	word_length = len(word)
	print(word_length)
	word = word.upper()

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


updatePrompt("aaron")

# ┌─┬─┬─┬─┬─┬─┬─┐
# │_│_│_│_│_│_│_│
# └─┴─┴─┴─┴─┴─┴─┘
# ┌─┬─┬─┬─┬─┬─┬─┐
# │A│A│A│A│A│A│A│
# └─┴─┴─┴─┴─┴─┴─┘

# ┤┤

# ┼ ┼

# ┴┴

# └ ┘




# def menu():
# 	print("[0] Play Hangman")
# 	print("[1] Exit")
# 	print("What do you want to do? ")
# 	choice = input()

# 	return choice

# def play(word):

# 	while 

# while True:

# 	choice = menu()
# 	if choice == "0":
# 		word = ""
# 		play(word)
# 	else if choice == "1":
# 		print("Thanks for playing!")
# 	else:
# 		print("Invalid input!")


			
# ╭┬───┐
# ││         │
# ││    ╭─┴─╮
# ││    │x_x  │
# ││    ╰─┬─╯
# ││       ╭┼╮
# ││       │││
# ││      ╭┴╮
# ││      │  │
# ││     
# ││
# ╧╧═══════════