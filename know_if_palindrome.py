
def palindrome():
	reverse_word = []

	reverse_word = word[::-1]

	if reverse_word == word:
		print("La palabra '{}' SI es un palindromo".format(word))
	else:
		print("La palabra '{}' NO es un palindromo".format(word))

	# print(reverse_word)

#--------------------

if __name__ == '__main__':
	word = input("Ingresa una palabra: \n")

	palindrome()

