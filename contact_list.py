import csv

class Contact:

	def __init__(self, name, phone, email):
		self._name = name
		self._phone = phone
		self._email = email

class ContactBook:

	def __init__(self):
		self._contacts = []

	def add_contact(self, name, phone, email):
		# print('Nombre: {}, \nTelefono: {}, \nCorreo: {}, \n'.format(name, phone, email))
		contact = Contact(name, phone, email)
		self._contacts.append(contact)
		self._save()

	def show_all(self):
		for contact in self._contacts:
			self._print_contacts(contact)

	def show_contact(self, contact_name):
		for contact in self._contacts:
			if contact._name.lower() == contact_name:
				self._print_contacts(contact)
		# else:
		# 	self._not_found()

	def delete(self, name):

		print('\n Contacto a eliminar: \n')
		for index, contact in enumerate(self._contacts):
			if contact._name.lower() == name.lower():
				self.show_contact(name)
				delete_option = str(input('''
				Confirmar eliminicación de contacto:

						[s]i
						[n]o

					''').lower())

			if delete_option == 's':
				print('** BORRANDO CONTACTO **')
				del self._contacts[index]
				self._save()
				break

			if delete_option == 'n':
				print('** OPERACIÓN CANCELADA  **')
				break

	def search(self, name):
		self.show_contact(name)

	def update(self, name):
		for contact in self._contacts:
			if contact._name.lower() == name.lower():

				option = str(input('''
					¿Qué desea actualizar?

						[n]ombre
						[t]elefono
						[c]orreo
						[to]do

					''').lower())

				if option == 'n':
					print('** ACTUALIZAR NOMBRE **')

					new_name = str(input('Ingrese el nuevo nombre del contacto \n'))
					contact._name = new_name

					print('Actualizando...')
					self.show_contact(new_name)
					self._save()
					break

				if option == 't':
					print('** ACTUALIZAR TELEFONO **')

					new_phone = str(input('Ingrese el nuevo telefono del contacto \n'))
					contact._phone = new_phone

					print('Actualizando...')
					self.show_contact(contact._name)
					self._save()
					break

				if option == 'c':
					print('** ACTUALIZAR CORREO **')

					new_email = str(input('Ingrese el nuevo correo del contacto \n'))
					contact._email = new_email

					print('Actualizando...')
					self.show_contact(contact._name)
					self._save()
					break

				elif option == 'to':
					print('** ACTUALIZAR TODA LA INFORMACIÓN **')

					new_name = str(input('Ingrese el nombre del contacto \n'))
					new_phone = str(input('Ingrese el telefono del contacto \n'))
					new_email = str(input('Ingrese el correo del contacto \n'))

					contact._name = new_name
					contact._phone = new_phone
					contact._email = new_email

					print('Actualizando...')
					self.show_contact(new_name)
					self._save()
					break

				else:
					self.update()
					break

			# else:
			# 	self._not_found()
			# 	break

		else:
			self._not_found()

	def _not_found(self):
		print('---*---*---*---*---*---')
		print('CONTACTO NO ENCONTRADO')
		print('---*---*---*---*---*---')

	def _print_contacts(self, contact):
		print('---*---*---*---*---*---*---*---*---')
		print('Nombre: {}'.format(contact._name))
		print('Telefono: {}'.format(contact._phone))
		print('Correo: {}'.format(contact._email))
		print('---*---*---*---*---*---*---*---*---')

	def _save(self):
		with open('contacts.csv', 'w') as f:
			writer = csv.writer(f)
			writer.writerow( ('name', 'phone', 'email') )

			for contact in self._contacts:
				writer.writerow( (contact._name, contact._phone, contact._email) )

def main():

	contact_book = ContactBook()

	with open('contacts.csv', 'r') as f:
		reader = csv.reader(f)
		for index, row in enumerate(reader):
			if index == 0 or len(row) == 0:
				continue

			contact_book.add_contact(row[0], row[1], row[2])
			# contact_book.add_contact(name, phone, email)

	while True:
		option = str(input('''
			Ingrese una opción:

				[a]ñadir contacto
				[ac]tualizar contacto
				[b]uscar contacto
				[e]liminar contacor
				[l]istar contactos
				[s]salir

			''').lower())

		if option == 'a':
			print('** AÑADIR CONTACTO **')

			name = str(input('Ingrese el nombre del contacto \n'))
			phone = str(input('Ingrese el telefono del contacto \n'))
			email = str(input('Ingrese el correo del contacto \n'))

			contact_book.add_contact(name, phone, email)

		if option == 'ac':
			print('** ACTUALIZAR CONTACTO **')

			name = str(input('Ingrese nombre de contacto a actualizar \n'))

			contact_book.update(name)

		if option == 'b':
			print('** BUSCAR CONTACTO **')

			name = str(input('Ingrese nombre de contacto a buscar \n'))

			contact_book.search(name)

		elif option == 'e':
			print('** ELIMINAR CONTACTO **')

			name = str(input('Ingrese nombre de contacto a eliminar \n'))

			contact_book.delete(name)

		elif option == 'l':
			print('** LISTAR CONTACTO **')
			contact_book.show_all()

		elif option == 's':
			print('Saliendo...')
			break

		else:
			main()

if __name__ == '__main__':
	print('B I E N V E N I D O A T U S C O N T A C T O S')
	print('*** -> Organizador de Contactos <- ***')
	main()
