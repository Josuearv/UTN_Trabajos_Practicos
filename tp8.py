"""
#Ejercicio 1
#Definición de la función `digits(num)`
def digits(num):
    #Convierte el número a una cadena para contar los dígitos
    str_num = str(num)
    
    #Verifica si el número es negativo y ajusta la longitud si es necesario
    if "-" in num:
        return len(str_num) - 1  #Resta 1 para excluir el signo negativo
    else:
        return len(str_num)  #Devuelve la longitud de la cadena (número de dígitos)

#Bucle para solicitar al usuario un número entero válido
while True:
    #Solicita al usuario que ingrese un número
    num = input("Ingrese un número: ")
    
    try:
        #Intenta convertir el valor ingresado a un número entero
        int_num = int(num)
        
        #Imprime el número y la cantidad de dígitos utilizando la función `digits(num)`
        print(f"{num} tiene {digits(num)} dígitos")
        
        #Sale del bucle ya que se ingresó un número entero válido
        break
        
    except ValueError:
        #Captura la excepción si el valor ingresado no es un número entero válido
        #Imprime un mensaje de error y continúa solicitando al usuario que ingrese un número
        print("¡ERROR! Solo ingrese números enteros")

#Ejercicio 2
# Definición de la función is_potency que verifica si n es una potencia de b
def is_potency(n, b):
    #Caso base: si n es igual a b, es una potencia de b
    if n == b:
        return True
    #Caso base: si n es menor que b y no divisible por b, no es una potencia de b
    if n < b or n % b != 0:
        return False
    #Llamada recursiva dividiendo n por b
    return is_potency(n // b, b)

#Corroborar que el número ingresado sea un entero
while True:
    try:
        #Entrada de datos desde el usuario
        num1 = input("Ingrese un número: ")
        num2 = input("Ingrese otro número: ")
        #Conversión de las entradas a enteros
        int_num1 = int(num1)
        int_num2 = int(num2)
        #Llamada a la función is_potency para verificar si num1 es potencia de num2
        potency = is_potency(int_num1, int_num2)
        
        #Verificación del resultado y muestra del mensaje correspondiente
        if potency == True:
            print(f"{num1} es potencia de {num2}")
            break
        else:
            print(f"{num1} no es potencia de {num2}")
            break
    
    except ValueError:
        #Captura de errores en caso de que se ingresen valores no válidos
        print("¡ERROR! Ingrese números válidos")

#Ejercicio 3
def positions_of(a, b, index=0, positions=None):
    #Inicializa la lista de posiciones en la primera llamada a la función
    if positions is None:
        positions = []
    
    #Encuentra la próxima ocurrencia de b en a a partir del índice actual
    position = a.find(b, index)
    
    #Si se encontró una ocurrencia, agrega su posición a la lista y busca la siguiente
    if position != -1:
        positions.append(position)
        #Llama recursivamente a la función para encontrar más ocurrencias después de la posición actual
        positions_of(a, b, position + 1, positions)
    
    return positions

#Solicita al usuario dos cadenas de texto
string1 = input("Ingrese una cadena de texto: ")
string2 = input("Ingrese otra cadena: ")

#Llama a la función positions_of y almacena el resultado en la variable result
result = positions_of(string1, string2)

#Imprime las posiciones donde se encontró la segunda cadena en la primera cadena
print(result)

#Ejercicio 4
#Definición de la función even que determina si un número es par
def even(n):
    #Caso base: si n es 1, retorna False (1 no es par)
    if n == 1:
        return False
    else:
        #Llama a la función odd con el argumento n-1 y devuelve su resultado
        return odd(n - 1)

#Definición de la función odd que determina si un número es impar
def odd(n):
    #Caso base: si n es 1, retorna True (1 es impar)
    if n == 1:
        return True
    else:
        #Llama a la función even con el argumento n-1 y devuelve su resultado
        return even(n - 1)

#Bucle para solicitar al usuario un número entero positivo
while True:
    try:
        #Solicita al usuario que ingrese un número y lo convierte a entero
        num = int(input("Ingrese un número entero: "))
        
        #Verifica si el número ingresado es positivo
        if num > 0:
            #Llama a la función even con el número ingresado y verifica si es True (par)
            if even(num) == True:
                print(f"{num} es par")
            else:
                print(f"{num} es impar")
            #Sale del bucle ya que se ingresó un número válido
            break
        else:
            #Si el número ingresado no es positivo, muestra un mensaje de error
            print("¡ERROR! Ingrese solo números enteros positivos")
            
    except ValueError:
        #Si se ingresa algo que no es un número entero, muestra un mensaje de error
        print("¡ERROR! Ingrese solo números enteros positivos")

#Ejercicio 5
#Lista de números
numbers = [1, 4, 6, 2, 3]

#Función recursiva para encontrar el máximo en una lista
def find_max(numbers):
    #Caso base: si la lista tiene un solo elemento, ese es el máximo
    if len(numbers) == 1:
        return numbers[0]
    else:
        #Llama recursivamente a la función con la lista sin el primer elemento
        remaining = find_max(numbers[1:])
        #Compara el primer elemento con el máximo encontrado en la lista restante
        if numbers[0] > remaining:
            return numbers[0]  #Si el primer elemento es mayor, es el nuevo máximo
        else:
            return remaining  #Si el máximo de la lista restante es mayor, sigue siendo el máximo

#Llama a la función find_max con la lista de números y almacena el resultado en la variable result
result = find_max(numbers)

#Imprime el máximo encontrado en la lista
print(result)

#Ejercicio 6
#Definición de la función que repite los elementos de la lista
def repeat_element(my_list, repeater):
    #Caso base: si repeater es 1, devuelve la lista tal cual
    if repeater == 1:
        return my_list
    else:
        new_list = []  #Lista vacía para almacenar los elementos repetidos
        #Itera sobre los elementos de la lista original
        for item in my_list:
            #Extiende la nueva lista con el elemento repetido repeater veces
            new_list.extend([item] * repeater)
        #Llamada recursiva con la nueva lista y repeater decrementado en 1
        return repeat_element(new_list, repeater - 1)

#Inicialización de la lista
my_list = []

#Bucle para ingresar elementos en la lista hasta que se ingrese 0
while True:
    element = input("Ingrese un elemento para la lista, para dejar de agregar ingrese 0: ")
    if element == "0":
        break
    else:
        my_list.append(element)

#Bucle para ingresar la cantidad de repeticiones y corroborar que se ingrese un valor correcto
while True:
    try:
        repeater = int(input("Ingrese la cantidad de veces que desea repetir cada elemento de la lista: "))
        break
    except ValueError:
        print("¡ERROR! Ingrese un número válido")

#Llamada a la función y muestra del resultado
print(repeat_element(my_list, repeater))

#Ejercicio 7
def k(n, p):
    #Caso base: si n es 1, retorna p como resultado
    if n == 1:
        return p
    else:
        #Llamada recursiva: multiplica n por p y agrega el resultado a la llamada recursiva con n - 1
        return n * p + k(n - 1, p)

while True:
    try:
        #Solicita al usuario dos números enteros
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        
        #Inicia el cálculo recursivo llamando a la función k con los números ingresados y muestra el resultado
        print(f"El resultado es {k(num1, num2)}")
        break
    except ValueError:
        #Captura errores si el usuario no ingresa números enteros
        print("¡ERROR! Ingrese números válidos")

#Ejercicio 8
#Definición de la función recursiva pascal que calcula el valor en la fila n y columna k del Triángulo de Pascal
def pascal(n, k):
    #Casos base: los valores en los bordes del Triángulo de Pascal son siempre 1
    if k == 0 or k == n:
        return 1
    else:
        #Llamadas recursivas para calcular el valor en la posición (n, k) sumando los valores de las posiciones (n-1, k-1) y (n-1, k)
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

#Bucle principal para solicitar al usuario la fila y columna del Triángulo de Pascal
while True:
    try:
        #Solicita al usuario el número de fila y columna (números enteros)
        row = int(input("Ingrese el número de fila: "))
        column = int(input("Ingrese el número de columna: "))

        #Verifica que la columna sea menor o igual a la fila para calcular el valor correspondiente en el Triángulo de Pascal
        if column <= row:
            result = pascal(row, column)
            #Muestra el valor en la fila y columna especificadas del Triángulo de Pascal
            print(f"El valor en la fila {row} y columna {column} del Triángulo de Pascal es: {result}")
        else:
            #Muestra un mensaje de error si la columna es mayor que la fila
            print("La columna no puede ser mayor que la fila.")
        break  #Sale del bucle si la entrada es válida
    except ValueError:
        #Captura la excepción si el usuario ingresa algo que no es un número entero
        print("Por favor, ingrese números enteros válidos.")

#Ejercicio 9
#Definición de la función recursiva que genera combinaciones de longitud k
def combinations(my_list, k, prefix=""):
    #Caso base: si la longitud requerida (k) es 0, imprimir la combinación actual
    if k == 0:
        print(prefix)
    else:
        #Para cada elemento en la lista, llamar recursivamente la función con k-1 y el elemento añadido al prefijo
        for i in my_list:
            combinations(my_list, k - 1, prefix + i)

#Lista para almacenar los caracteres ingresados por el usuario
my_list = []
#Variable de control para el bucle principal
validator = True

#Bucle para ingresar caracteres hasta que el usuario ingrese "0"
while True:
    my_string = input("Ingrese un caracter (sin repetir) u oprima 0(cero) para salir: ")
    if my_string == "0":
        validator = False
        break
    else:
        #Verificar si el caracter ya existe en la lista
        if my_string in my_list:
            print("¡ERROR! Ese caracter ya existe en la lista")
        else:
            #Agregar el caracter a la lista
            my_list.append(my_string)

#Bucle para ingresar la longitud de las combinaciones
while True:
    try:
        length = int(input("Ingrese la longitud de las combinaciones: "))
        #Llamar a la función con la lista y la longitud especificada
        combinations(my_list, length)
        break
    except ValueError:
        print("¡ERROR! Ingrese un número válido")

#Ejercicio 10
#Definición de la función sheet_size_A que calcula las dimensiones de una hoja A(N)
def sheet_size_A(n):
    #Caso base: hoja A0
    if n == 0:
        #Retorna las dimensiones de la hoja A0
        return (841, 1189)
    else:
        #Llamada recursiva para obtener las dimensiones de la hoja A(N-1)
        previous_width, previous_length = sheet_size_A(n - 1)
        #Calcula las dimensiones de la hoja A(N) doblando al medio la hoja A(N-1)
        actual_length = previous_width  #El largo de la hoja A(N) es igual al ancho de la hoja A(N-1)
        actual_width = previous_length / 2  # El ancho de la hoja A(N) se reduce a la mitad del largo de la hoja A(N-1)
        #Retorna las dimensiones de la hoja A(N) como una tupla de enteros
        return (int(actual_width), int(actual_length))

#Bucle principal para solicitar al usuario el tipo de hoja y mostrar sus dimensiones
while True:
    try:
        validator = True
        #Bucle interno para validar la entrada del usuario
        while validator:
            #Solicita al usuario el tipo de hoja deseada (número entero)
            sheet_type = int(input("Ingrese de qué tipo de hoja necesita saber el tamaño: Hoja A"))
            if sheet_type < 0:
                #Si el valor ingresado es negativo, muestra un mensaje de error
                print("¡ERROR! El valor debe ser mayor que 0 (cero)")
            else:
                #Si el valor ingresado es válido, calcula las dimensiones y muestra el resultado
                result = sheet_size_A(sheet_type)
                print(f"La hoja A{sheet_type} mide {result[0]} X {result[1]}mm")
                validator=False #Validator cambia su valor a False para salir del bucle interno
        break  #Sale del bucle principal si la entrada es válida
    except ValueError:
        #Captura la excepción si el usuario ingresa algo que no es un número entero
        print("¡ERROR! Ingrese un número válido")
"""