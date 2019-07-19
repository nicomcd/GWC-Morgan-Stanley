import random

# A list of words that
potential_words = ["Hello", "world", "fire"]

word = random.choice(potential_words)

# # Use to test your code:
# # print(word)
#
# Converts the word to lowercase
word = word.lower()
#
# Make it a list of letters for someone to guess
current_word = list(word) # TIP: the number of letters should match the word
# print(current_word)
# Some useful variables
guesses = []#stores the peivous guesses
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")
#checking that guess is a  string letter and that the current guess is a new guess
	if guess.isalpha() and len(guess) == 1 and guess not in guesses:
		guesses.append(guess)
		if guess in current_word:
			print("you guessed a letter correctly")
			#our guess is right
		else:
			#your guess is wrong
			fails += 1
			print("you guessed incorrectly")
	else:
		print(f"invaild answer:{guess}")
		#not vaild input


		# check if the guess is valid: Is it one letter? Have they already guessed it?

		# check if the guess is correct: Is it in the word? If so, reveal the letters!

	# print(current_word)


	print("You have " + str(maxfails - fails) + " tries left!")
	display = ""
	winning = ""
	for i in current_word:
			if i in guesses:
				display += i + " "
				winning+=i
				# print(i)
			else:
				display += "_ "
				# print("_")
	print(display)
	if winning == word:
		print ("you won")
		exit(0)
print(f"you have lost the word was {word}")
