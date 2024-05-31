import random

def select_word():
	words=["Manish","Dev","Rajiv","Ravi","Om"]
	return random.choice(words)

def display_word(word,guess_letter):
	display=""
	for letter in word:
		if letter in guess_letter:
			display += letter
		else:
			display += '_'
	return display

def hangman():
	word=select_word()
	guess_letter=[]
	worng_guess=0
	max_wrong_guess=6

	print("Welcome To A Hangman Game !")
	print(display_word(word,guess_letter))

	while "_" in display_word(word,guess_letter) and worng_guess < max_wrong_guess:
		guess=input('Guess A Letter :- ').lower()

		if len(guess) !=1 or not guess.isaplha():
			print("Please Enter A Single Letter.")
			continue

		if guess in guess_letter:
			print("You Already Gussed It Before ")
			continue

		guess_letter.append(guess)

		if guess not in word:
			worng_guess += 1
			print("Incorrect You Have {} Attempt Left. ".format(max_wrong_guess-worng_guess))

		print(display_word(word,guess_letter))

	if "_" not in display_word(word,guess_letter):
		print('Congratulations {} '.format(word))
	else:
		print('Sorry,You Ran Out Of Attempt The Word Was {}.'.format(word))

	if __name__ == "__main__":
		hangman()
