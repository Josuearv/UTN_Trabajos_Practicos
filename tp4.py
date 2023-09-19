"""
1) Create a while loop with the following characteristics:

• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x.

"""
x=0
saltos = (4,6,10) #lista de numeros a saltar
while x<=30:

    if x != 15 and x not in saltos: #la impresion de cualquier numero que no cumpla esas cndiciones
        print(f'The value of the loop is: {x}')
    elif x==15:#si se cumple esta condicion deja un mensaje y termina el programa
        print(f'The execution of the loop was broken when x was {x}')
        break
    elif x in saltos:#si el numero esta dentro de la tupla deja un mensaje de que se salto ese numero
        print(f'The value {x} of x was skipped')
    x+=1

#2)Escribe un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.

letras = input('Digite la linea, deje en blanco para finalizar: ').strip(' ') #coloco el metodo strip para eliminar los espacios vacios del pricnipio y final 
lineas = []#Para guardar las lineas
while letras != '':
    lineas.append(letras)
    letras = input('Digite la linea, deje en blanco para finalizar: ').strip(' ')
else:#cuando el while sea falso se ejecuto lo que esta dentro del else
    if letras == '' and len(lineas)==0:#Si no se ingreso desde el principio algo devuelve este mesnaje
        print('No digito ninguna linea')
    else:#en el caso contrario recorre la lista y le hace un upper
        for i in lineas:
            print(i.upper())
"""
3).	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos

Ejemplo de una entrada:
D 200
D 200
R 100
D 50
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería:
350

"""

operacione = input('Digite la operacion con el formaro de "operacion valor", recordando que R es retirar y D depositar, deje en blanco para finalizar: ').strip(' ') #coloco el metodo strip para eliminar los espacios vacios del pricnipio y final 
operaciones = []#Para guardar las operaciones
total = 0

while operacione != '':
    operaciones.append(operacione)
    operacione = input('Digite la linea, deje en blanco para finalizar: ').strip(' ')
else:#cuando el while sea falso se ejecuto lo que esta dentro del else
    if operacione == '' and len(operaciones)==0:#Si no se ingreso desde el principio algo devuelve este mesnaje
        print('No digito ninguna operacion')
    else:#en el caso contrario recorre la lista y le hace un upper
        for i in operaciones:
            bitacora= i.split(' ')[0].upper() #divido por el espacio y selecciono el primer elemento devido al formato dado corresponde a la bitacora
            valor = int(i.split(' ')[1])# se divide por espacio y se selecciona el valor
            if bitacora == 'D':
               total+=valor
            else:
               total-=valor
        print(total)


"""
4)Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
Imprimir la cantidad total de números primos ingresados.
Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.
"""

numero = int(input('Digite un numero primo recuerde que un numero primo es aquel que solo se divide entre el mismo y el 1, digite cero para terminar:'))
numeros_primos = []
primo = True

while numero != 0:
    if numero == 1:
        print('Nota: Recuerda que un numero primo es mayor a 1')
        continue
    for i in range(2,numero):

        if numero%i==0 and i!=1 and i!=numero:
            primo = False
            break
        else: 
            primo= True
    if primo==True:
        numeros_primos.append(numero)
    numero = int(input('Digite un numero primo recuerde que un numero primo es aquel que solo se divide entre el mismo y el 1:'))
else:
    print(f'El numero de total de primos ingresados es de {len(numeros_primos)}')
    
"""
5.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

"""
age1 = input('Ingrese un primer año: ')
age2 = input('Ingrese el siguiente año: ')
for i in range(age1,age2+1):

    if i%4==0 and i%10==0 and not i%100==0:
        print(i)
    elif i%400==0:
        print(i)
    else:
        continue




#Ejercicio 6
for i in range(1,21):
       if i%2==0:
               print(i)
       else:
           continue

#Ejercicio 7
numbers=[7,8,1,9]
num=int(input("Ingrese un número para saber si se encuentra en la lista: "))

for i in numbers:
   if num==i:
       print(f"El número {num} si se encuentra en la lista")
       break
   else:
       continue

#Ejercicio 8
print(f"¡BIENVENIDO! A continuación verá las diferentes opciones de menú\n1- Milanesa con puré\n2- Tarta de jamón y queso\n3- Ñoquis con tuco\n0- Salir")
option=1
account=0
count=[]
while option!=0:
   option=int(input("Ingrese una opción: "))
   if option==0:
       break
   elif option==1:
       print("Milanesas con pure: $1200")
       account+=1200
       count.append(1)
   elif option==2:
       print("Tarta de jamón y queso: $1400")
       account+=1400
       count.append(2)
   elif option==3:
       print("Ñoquis con tuco: $1500")
       account+=1500
       count.append(3)
   else:
       print("¡ERROR! Ingrese una opción válida")
print(f"Usted ha pedido los siguientes menús: {count}\nLa cuenta total es de ${account}")
