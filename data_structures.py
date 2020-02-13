# ******************************
# SETS

a = set([1, 2, 3, 4])
b = set([4, 5, 6, 7])

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))

print(1 in a)
print(1 in b)

print(4 in a)
print(4 in b)

# ******************************
# Dictionary comprehension - list comprehension

even = [num for num in range(1, 31) if num % 2 == 0]
print(even)

odd = [num for num in range(1, 31) if num % 2 != 0]
print(odd)

squares_list = [num**2 for num in range(1, 11)]
print(squares_list)

squares_dict = {num: num**2 for num in range(1, 11)}
print(squares_dict)

# ******************************
# Error managment

countries = {
	'colombia': 50,
	'mexico': 122,
	'argentina': 43,
	'chile': 18,
	'peru': 31
}

while True:
	 country = str(input('Escribe el nombre de un país: \n')).lower()

	 try:
	 	print('La población de {} es de {} millones de personas '.format(country, countries[country]))
	 except KeyError as e:
	 	print('No se tiene la información de la población de {} '.format(country))


