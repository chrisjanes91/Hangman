import random
def hangman(word):
	wrong = 0
	stages = ["",
	"____	",
	"|		",
	"|	 |	",
	"|	 0	",
	"|	/|\	",
	"	/ \ ",
	"|		"
	]
	remaining_letters = list(word)
	board = ["__"] * len(word)
	win = False
	print("Welcome to Hangman")

	while wrong < len(stages) - 1:
		print("\n")
		char = input("Guess a letter or type \'esc\' to quit: ")
		if char == "esc":
			break
		if char in remaining_letters:
			while char in remaining_letters:
				cind = remaining_letters.index(char)
				board[cind] = char
				remaining_letters[cind] = "$"
		else:
			wrong += 1
		print((" ".join(board)))
		e = wrong + 1
		print("\n".join(stages[0 : e]))
		if "__" not in board:
			print("You win!")
			print(" ".join(board))
			win = True
			break

	if not win:
		print("\n".join(stages[0 : wrong]))
		print("You lose! It was {}.".format(word))

words = ["dog", "hat", "running", "boat", "horse", "ball", "book", "tree"]
wordIn = random.randint(0, (len(words) - 1))
chosen = words[wordIn]
hangman(chosen)
