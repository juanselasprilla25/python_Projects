# "aabbcddee"
# "abcdefghijabcdefghijk"
# "jjuuaann&"

def verify_sequence(char_sequence):
	seen_letters = {}

	for index, letter in enumerate(char_sequence):
		if letter not in seen_letters:
			seen_letters[letter] = (index, 1)
		else:
			seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

	final_letters = []
	for key, value in seen_letters.items():
		if value[1] == 1:
			final_letters.append( (key, value[0]) )

	not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

	if not_repeated_letters:
		return not_repeated_letters[0][0]
	else:
		return '*'

if __name__ == '__main__':

	char_sequence = str(input('Escribe una secuencia de caracteres: \n'))

	result = verify_sequence(char_sequence)

	if result == '*':
		print('\n')
		print('Todos los caracter ingresados se repiten.')
	else:
		print('\n')
		print('El primer caracter no repetido es: {}'.format(result))


