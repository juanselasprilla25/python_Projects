
import random

IMAGENES_AHORCADO = ['''

    +---+
    |   |
        |
        |
        |
        |
  	=========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
 	=========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
	=========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
	=========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
	=========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
	=========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
	=========''']

WORDS = [
	'ahorcado',
	'computador',
	'television',
	'cargador',
	'comida'
]

LETTER_LIST = []

def used_letter(letter):

	LETTER_LIST.append(letter)
	print('')
	print('LETRAS YA USADAS: \n')
	print(LETTER_LIST)


def random_word():
	random_index = random.randint(0, len(WORDS) - 1)
	return WORDS[random_index]

def display_board(hidden_word, tries):
	print(IMAGENES_AHORCADO[tries])
	print('')
	print(hidden_word)
	print('')
	print('--- * --- * --- * --- * --- * ---')

def ahorcado():
	word = random_word()
	hidden_word = ['-'] * len(word)
	tries = 0

	while True:
		display_board(hidden_word, tries)
		input_letter = str(input("Ingresa una letra: \n"))

		if len(input_letter) != 1:
			print('')
			print(' ** {} ** NO es una letra, intenta de nuevo'.format(input_letter))
			tries += 1

		else:
			used_letter(input_letter)
			letter_indexes = []
			for index in range(len(word)):
				if word[index] == input_letter:
					letter_indexes.append(index)

			if len(letter_indexes) == 0:
				tries += 1

				if tries == 6:
					display_board(hidden_word, tries)
					print('')
					print('PERDISTE! La palabra correcta es ** {} **'.format(word))
					break

			else:
				for found_index in letter_indexes:
					hidden_word[found_index] = input_letter

				letter_indexes = []

			try:
				hidden_word.index('-')
			except ValueError:
				print('')
				print('GANASTEE! La palabra correcta es ** {} **'.format(word))
				break

if __name__ == '__main__':
	print("B I E N V E N I D O S    A    A H O R C A D O S")
	ahorcado()
