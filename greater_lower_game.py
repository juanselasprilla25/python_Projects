
import random

def play():
	random_num = random.randint(0, 50)
	found = False

	while not found:
		input_num = int(input("Ingresa un número: \n"))

		if(input_num == random_num):
			print("Número Correcto!!")
			found = True
		elif(input_num>random_num):
			print("El número es más pequeño")
		else:
			print("El número es más grande")


if __name__ == '__main__':
	play()
