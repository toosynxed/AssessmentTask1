import os
import random
os.system('clear')
word_choices = ['apple', 'banana', 'cherry', 'date', 'elderberry']
word = random.choice(word_choices)
word = 'cherry' #just here to ensure that during testing, all variables remain the same
word_in_list_form = list(word)
print(f"word in list form {word_in_list_form}")
#topick = list(word)
length_of_chosen_word = len(word)
display_letters = []
display_letters = word_in_list_form
for i in range(0,length_of_chosen_word):
	display_letters[i] = '_'	
already_guessed = []
correct_score = 0
chn = 0
picked = 0
strike = 0
underscore_display_letters = []
underscore_display_letters = ' '.join(display_letters)
while correct_score < length_of_chosen_word:
	not_in_word_counter = 0
	print(f"Letters Remaining: {underscore_display_letters}")	
	letter = input("\nPick a letter: ").lower()
	if len(letter) != 1 or letter.isalpha() == False:
		os.system('clear')
		print(f'Please input a valid letter.\n')
	else:
		length_of_chosen_letters = len(already_guessed)
		for n in range(0,length_of_chosen_letters):		
			if letter == already_guessed[n]:
				os.system('clear')
				print(f"Already chosen, pick again\n\nYou have: {strike} strikes\n")
				break	
			elif letter != already_guessed[n]:
				not_in_word_counter = not_in_word_counter	+ 1		
		if not_in_word_counter == length_of_chosen_letters:
			already_guessed.append(letter)
			picked = 0
			for i in range(0,length_of_chosen_word):
				if letter == word[i]:				
					display_letters[i] = letter
					underscore_display_letters = ' '.join(display_letters).upper()
					correct_score = correct_score + 1
					picked = 1
					os.system('clear')	
					print("Good Job!")
					print("You have selected a correct letter!")
					print()
					print(f"You have: {strike} strikes!\n")
			if picked == 0:
				os.system('clear')
				print("Uh Oh!")
				print(f"It seems that the letter '{letter.upper()}', is not in the word")
				strike = strike + 1
				print(f"\nYou have: {strike} strikes!")
				print()
				if strike >= length_of_chosen_word and correct_score <= length_of_chosen_word:
					print(f'Unlucky! \nIt seems that you have not guessed the word in time! \nTry again!')
					print(f'The word was: {word.upper()}')
					break
if correct_score >= length_of_chosen_word:
	print("Congrats!")
	print("You managed to guess the word correctly!")
	print('')
	print(f"The word was: {word.upper()}")
	print()