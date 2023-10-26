#1
class Persona:
    def __init__(self, name='', age=None, dni=''):
        self.__name = name
        self.__age = age
        self.__dni = dni

    # Setters y getters con validación de datos
    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Error: El name debe ser una cadena de caracteres.")

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            print("Error: La age debe ser un número entero positivo.")

    def get_age(self):
        return self.__age

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self.__dni = dni
        else:
            print("Error: El DNI debe ser una cadena de 9 caracteres.")

    def get_dni(self):
        return self.__dni

    def show(self):
        print(f"name: {self.__name}, age: {self.__age}, DNI: {self.__dni}")

    def is_old(self):
        return self.__age >= 18


# Ejemplo de uso:
# Crear una persona
persona1 = Persona()
persona1.set_name("Juan")
persona1.set_age(25)
persona1.set_dni("123456789")

# Mostrar los datos de la persona
persona1.show()

# Verificar si la persona es mayor de age
print("¿Es mayor de age?", persona1.is_old())


#2
class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.__titular = titular  # El titular debe ser un objeto de la clase Persona
        self.__cantidad = cantidad

    # Setters y getters con validación de datos
    def setTitular(self, titular):
        if isinstance(titular, Persona):
            self.__titular = titular
        else:
            print("Error: El titular debe ser un objeto de la clase Persona.")

    def getTitular(self):
        return self.__titular

    def setCantidad(self, cantidad):
        if isinstance(cantidad, (int, float)):
            self.__cantidad = cantidad
        else:
            print("Error: La cantidad debe ser un número.")

    def getCantidad(self):
        return self.__cantidad

    def show(self):
        print(f"Titular: {self.__titular.get_name()}, Cantidad: {self.__cantidad}")

    def ingress(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("Error: La cantidad a ingresar debe ser un número positivo.")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
        else:
            print("Error: La cantidad a retirar debe ser un número positivo.")


# Ejemplo de uso:
# Crear una persona para ser titular de la cuenta
persona_titular = Persona("Juan", 30, "123456789")

# Crear una cuenta e asociarle un titular
cuenta1 = Cuenta(persona_titular, 1000.0)

# Mostrar los datos de la cuenta
cuenta1.show()

# Ingresar dinero en la cuenta
cuenta1.ingress(500.0)
cuenta1.show()

# Retirar dinero de la cuenta
cuenta1.retirar(200.0)
cuenta1.mostrar()

#3

class Tringule:
    # Constructor para inicializar los lados del triángulo
    def __init__(self, l1=0, l2=0, l3=0):
        self.__l1 = l1  
        self.__l2 = l2
        self.__l3 = l3

    # Métodos para establecer y obtener el lado 1
    def set_l1(self, l1):
        if isinstance(l1, (int, float)):
            self.__l1 = l1
        else:
            print("Error: La longitud debe ser un número.")

    def get_l1(self):
        return self.__l1

    # Métodos para establecer y obtener el lado 2
    def set_l2(self, l2):
        if isinstance(l2, (int, float)):
            self.__l2 = l2
        else:
            print("Error: La longitud debe ser un número.")

    def get_l2(self):
        return self.__l2
    
    # Métodos para establecer y obtener el lado 3
    def set_l3(self, l3):
        if isinstance(l3, (int, float)):
            self.__l3 = l3
        else:
            print("Error: La longitud debe ser un número.")

    def get_l3(self):
        return self.__l3

    # Método para mostrar los lados del triángulo
    def show(self):
        print(f"Lado 1: {self.__l1}, Lado 2: {self.__l2}, Lado 3: {self.__l3}")

    # Método para identificar el lado más largo del triángulo
    def long_side(self):
        if self.__l1 > self.__l2 and self.__l1 > self.__l3:
            print('El lado más largo del triángulo es:', self.__l1)
        elif self.__l2 > self.__l3 and self.__l2 > self.__l1:
            print('El lado más largo del triángulo es:', self.__l2)
        elif self.__l3 > self.__l1 and self.__l3 > self.__l2:
            print('El lado más largo del triángulo es:', self.__l3)
        else:
            print('Todos los lados son iguales')

    # Método para identificar el tipo de triángulo
    def type_triangle(self):
        if self.__l1 == self.__l2 and self.__l2 == self.__l3:
            print('Es un triángulo equilátero')
        elif (self.__l1 == self.__l2 and self.__l3 != self.__l1) or (self.__l2 == self.__l3 and self.__l1 != self.__l3) or (self.__l1 == self.__l3 and self.__l1 != self.__l2):
            print('Es un triángulo isósceles')
        elif self.__l1 != self.__l2 and self.__l2 != self.__l3:
            print("Es un triángulo escaleno")

       
#4

class Agenda:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        # AAñade un contacto a la agenda
        contact = {'name': name, 'phone': phone, 'email': email}
        self.contacts.append(contact)
        print(f'Contact {name} added.')

    def list_contacts(self):
        # Muestra la lista de contacto
        print('List of contacts:')
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def search_contact(self, name):
        # Buscar un contacto por nombre
        for contact in self.contacts:
            if contact['name'] == name:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                return
        print(f"Contact {name} not found.")

    def edit_contact(self, name):
        #Editar un contacto con el nombre
        for contact in self.contacts:
            if contact['name'] == name:
                new_name = input('New name: ')
                new_phone = input('New phone: ')
                new_email = input('New email: ')
                contact['name'] = new_name
                contact['phone'] = new_phone
                contact['email'] = new_email
                print(f'Contact {name} edited.')
                return
        print(f"Contact {name} not found.")

    def close_agenda(self):
        # Close the agenda
        print('Agenda closed.')


my_agenda = Agenda()

while True:
    print('\nMenu:')
    print('1. Add contact')
    print('2. List contacts')
    print('3. Search contact')
    print('4. Edit contact')
    print('5. Close agenda')

    option = input('Select an option: ')

    if option == '1':
        name = input('Name: ')
        phone = input('Phone: ')
        email = input('Email: ')
        my_agenda.add_contact(name, phone, email)
    elif option == '2':
        my_agenda.list_contacts()
    elif option == '3':
        name = input('Name to search: ')
        my_agenda.search_contact(name)
    elif option == '4':
        name = input('Name to edit: ')
        my_agenda.edit_contact(name)
    elif option == '5':
        my_agenda.close_agenda()
        break
    else:
        print('Invalid option. Please try again.')




