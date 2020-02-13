def run():
	print("hola primera línea ejecutada")

if __name__ == '__main__':
	run()


class someone:
	def __init__(self, name_f, age_f):
		self.name = name_f
		self.age = age_f

	def say_hi(self):
		print("Hola, mi nombre es {} y mi edad es {}".format(self.name, self.age))

p1 = someone("juan", 25)

p1.say_hi()

print("hola")

name = input("Di algo: \n")
print(name)
print("La cadena que ingresó es:\n", name)

for a in range(30):
 		print(a)

s = "juan"

for letras in s:
	print(letras)

print('')
