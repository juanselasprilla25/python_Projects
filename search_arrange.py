# ARREGLAR EL CÓDIGO ******

class node(object):
	"""docstring for node"""
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

class binary_tree(object):
	"""docstring for binary_tree"""
	def __init__(self, root):
		self.root = node(root)


a = [2, 5, 1, 0, 8, 10, 1, 22, 15, 14, 3, 20]
n_a = {}

for pos in range(len(a) - 1):

	# print(' {} , {}'.format(a[pos], a[pos + 1]))
	print('\n')
	print('iteración : {}'.format(pos))

	if a[pos + 1] == a[pos]:
		n_a = a[pos]
	elif a[pos + 1] > a[pos]:
		print('Número menor: {}'.format(a[pos]))
		print('Número mayor: {}'.format(a[pos+1]))

		print('Posición número menor en n_a: {}'.format(pos))
		print('Posición número mayor en n_a: {}'.format(pos+1))

		n_a[pos] = a[pos]
		n_a[pos + 1] = a[pos + 1]
	else:
		print('Número menor: {}'.format(a[pos + 1]))
		print('Número mayor: {}'.format(a[pos]))

		print('Posición número menor en n_a: {}'.format(pos))
		print('Posición número mayor en n_a: {}'.format(pos + 1))

		n_a[pos] = a[pos + 1]
		n_a[pos + 1] = a[pos]

print('\n')
print(a)
print(n_a)
