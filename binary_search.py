

def search(num_list, num_to_find, lower_limit, upper_limit):

	if lower_limit > upper_limit:
		return False

	limit = (upper_limit + lower_limit)//2

	if num_to_find == num_list[limit]:
		print('Número encontrado en posición {}'.format(limit))
		return True
	elif num_to_find > num_list[limit]:
		# print('El límite de búsqueda superior es {}'.format(upper_limit))
		# print('El límite de búsqueda inferior es {}'.format(lower_limit))
		return search(num_list, num_to_find, limit + 1 , upper_limit)
	elif num_to_find < num_list[limit]:
		# print('El límite de búsqueda superior es {}'.format(upper_limit))
		# print('El límite de búsqueda inferior es {}'.format(lower_limit))
		return search(num_list, num_to_find, lower_limit, limit - 1)

if __name__ == '__main__':

	num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	num_to_find = int(input('Ingresa el número a buscar: \n'))

	# print('Tu número a buscar es {}'.format(num_to_find))

	found = search(num_list, num_to_find, 0, len(num_list) - 1)

	if found is True:
		print('El número ingresado: "{}" se encuentra en la lista'.format(num_to_find))
	else:
		print('El número ingresado: "{}" no se encuentra en la lista'.format(num_to_find))
