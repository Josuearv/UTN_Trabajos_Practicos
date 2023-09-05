#ejericicio.1-2
"""
años=int(input("Ingrese años del computador: "))

if años < 0:
    print("[ERROR:] El valor ingresado no puede ser negativo.")
elif años <= 2:
    print("El computador es nuevo.")
else:
    print("El computador es viejo.")
"""
#ejercicio.3
"""
nombre_persona1=input("Ingrese nombre de la primer persona: ")
nombre_persona2=input("Ingrese nombre de la segunda persona: ")

inicial_persona1=nombre_persona1[0].lower()
inicial_persona2=nombre_persona2[0].lower()

if inicial_persona1 == inicial_persona2:
    print("Concidencia.")
else:
    print("No hay coincidencia.")
"""
#ejercicio.4
"""
print("ELEJI TU CANDIDATO")
voto=input(("A: Partido ROJO\nB: Partido VERDAD\nC: Partido AZUL: "))
voto=voto.upper()
if voto == "A":
    print("Usted ha votado por el partido [ROJO].")
elif voto == "B":
    print("Usted ha votado por el partido [VERDAD].")
elif voto == "C":
    print("Usted ha votado por el partido [AZUL].")
else:
    print("[ERROR:] Opcion errónea.")
"""
#ejercicio.5
"""
letra=input("Ingrese una letra: ")
letra=letra.upper()
vocales=("A","E","I","O","U")

if len(letra) != 1:
    print("[ERROR:] No se pudo procesar el dato.")
elif letra in vocales:
    print(f"{letra} Es vocal.")
else:
    print(f"{letra} No es vocal.")
"""
#ejercicio.6
"""
anio=int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
"""
#ejercicio.7
"""
num1=float(input("Ingrese el numero 1: "))
num2=float(input("Ingrese el numero 2: "))
num3=float(input("Ingrese el numero 3: "))

if num1 < num2 and num1 < num3:
    print(f"{num1} es menor que {num2} y {num3}.")
elif num2 < num1 and num2 < num3:
    print(f"{num2} es menor que {num1} y {num3}.")
else: 
    print(f"{num3} es menor que {num1} y {num2}.")
"""
#ejercicio.8
"""
nombre_usuario=input("Ingrese su nombre de usuario: ")
password=input("Ingrese su contraseña: ")

if nombre_usuario == "Gwenevere" and password == "excalibur":
    print("Usuario y contraseña correctos.Puede ingresar a Camelot.")
else:
    print("[ACCESO DENEGADO] El usuario o la contraseña son incorrectos.")
"""
#ejercicio.9
"""
nombre=input("Ingrese su nombre: ")
sexo=input("Ingrese su sexo (Femenino/Masculino):  ")

if (sexo.upper() == "F" and nombre.lower() < "m") or (sexo.upper() == "M" and nombre.lower() > "n"):
    print("Usted pertenece al grupo A")
else:
    print("Usted pertenece al grupo B")
"""
#ejercicio.10
"""
edad=int(input("Ingresa tu edad: "))

if edad < 4 and edad > 0:
    print("Tu ingreso es sin costo.")
elif edad >= 4 and edad < 18:
    print("El costo de entrada es de: $500.")
elif edad >= 18:
    print("El costo de entrada es de $1000.")
else:
    print("[ERROR:] El valor ingresado no es valido.")
"""
#ejercicio.11
"""

print("Seleccione la opcion que desea.")
print("1-Pizza Vegetariana\n2-Pizza Tradicional")
tipo_pizza=int(input())

if tipo_pizza == 1:
    print("Seleccione los ingredientes.")
    print("1-Pimiento\n2-Tofu")
    ing_veg=int(input())
    if ing_veg == 1:
        print("La pizza seleccionada es vegetariana y sus ingredientes son: mozzarella,tomate y pimiento.")
    elif ing_veg ==2:
        print("La pizza seleccionada es vegetariana y sus ingredientes son: mozzarella,tomate y tofu.")
    else:
        print("[ERROR:] No existe esa opcion.")   
elif tipo_pizza == 2:
    print("Seleccione los ingredientes.")
    print("1-Peperoni\n2-Jamón\n3-Salmón")
    ing_comun=int(input())
    if ing_comun == 1:
        print("La pizza seleccionada es tradicional y sus ingredientes son: mozzarella,tomate y peperoni.")
    elif ing_comun == 2:
        print("La pizza seleccionada es tradicional y sus ingredientes son: mozzarella,tomate y jamón.")
    elif ing_comun == 3:
        print("La pizza seleccionada es tradicional y sus ingredientes son: mozzarella,tomate y salmón.")
    else:
        print("[ERROR:] No existe esa opcion.")  
else:
    print("[ERROR:] No existe esa opcion.")   
"""
#ejercicio.12
"""
anio_actual=int(input("Ingrese el año actual: "))
anio_x=int(input("Ingrese un año cualquiera: "))
diferencia_anios=abs(anio_actual-anio_x)
if anio_actual > anio_x:
    print(f"Pasaron {diferencia_anios} años desde {anio_x} a {anio_actual}.")
elif anio_actual < anio_x:
    print(f"Faltan {diferencia_anios} años para llegar de {anio_actual} hasta {anio_x}.")
else:
    print(f"No hay años de diferencia entre {anio_actual} y {anio_x}.")
"""
#ejercicio.13
"""
num1=int(input("Ingrese primer numero: "))
num2=int(input("Ingrese segundo numero: "))

if num1 <= 0 or num2 <= 0:
    print("[ERROR:] No se pueden ingresar valor negativos o nulos.")
else:
    if num1 > num2:
        mayor=num1
        menor=num2
    else:
        mayor=num2
        menor=num1

if mayor % menor == 0:
    print(f"{mayor} es multiplo de {menor}")
else:
    print(f"{mayor} no es multiplo de {menor}")
"""
#ejercicio.14
"""
print("Ecuacion: (a x + b = 0)")
a=int("Ingresa el valor de a: ")
b=int("Ingresa el valor de b: ")

if a == 0:
    if b == 0:
        print("La ecuacion tiene infinitas soluciones (todos los numeros son solucion.)")
    else:
        print("La ecuacion no tiene solucion.")
else: 
    x = -b / a
    print(f"La solucion de la ecuacion {a}x +{b} = 0 es x = {x}.")
"""
#ejercicio.15
"""
import math

print("Ingrese la opcion que desea")
print("T) Calcular area de un triangulo.\nC) Calcular el area de un ciruculo.")
triangulo_circulo=input().lower()

if triangulo_circulo == "t":
    altura=float(input("Ingresa la altura del triangulo:"))
    base=float(input("Ingresa la base del triangulo:"))
    print(f"El area del triangulo es: {(base*altura)/2}")
elif triangulo_circulo == "c":
    
    pi=math.pi
    radio=float(input("Ingresa el radio del circulo: "))
    print(f"El area del circulo es: {pi*(radio**2)}")
else:
    print("[ERROR:] La opcion ingresada es erronea (elije T/t para triangulo o C/c para circulo).")
"""
#ejercicio.16
"""
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))

print("Seleccione una operacion para realizar con los numeros ingresados.")
operacion=int(input("1-Suma\n2-Multiplicacion\n3-Resta\n4-Division: "))
if operacion == 1:
    print(f"El resultado de la operacion es: {num1+num2}")
elif operacion == 2:
    print(f"El resultado de la operacion es: {num1*num2}")
elif operacion == 3:
    print(f"El resultado de la operacion es: {num1-num2}")
elif operacion == 4:
    print(f"El resultado de la operacion es: {num1/num2}")
else:
    print("[ERROR:] La opcion ingresada no es valida. ")
"""
#ejercicio.17
"""
dia_semana=input("Ingresa un dia de la semana: ").lower()
otros_dias=("martes","miercoles","jueves")

if dia_semana == "lunes":
    print("Arranco la tortura.")
elif dia_semana == "viernes":
    print("Ultimo dia de tortura, buen finde.")
elif dia_semana == "sabado" or dia_semana == "domingo":
    print("Disfruta tus dias de descanso.")
elif dia_semana in otros_dias:
    print("Tranquilo cada dia falta menos para el finde.")
else:
    print("[ERROR:] El dia ingresado no es valido.")
"""
#ejercicio.18
"""
horas_trabajadas=float(input("Ingrese el dia de horas trabajadas en el mes: "))
salario_hora=float(input("Ingrese su salario por hora: "))

if horas_trabajadas <= 48:
    print(f"Total horas trabajadas: {horas_trabajadas} horas.")
    print(f"Sueldo total: ${horas_trabajadas*salario_hora}.")
else:
    salario_horas_extra=(horas_trabajadas-48)*salario_hora*0.10
    salario_total=horas_trabajadas*salario_hora+salario_horas_extra
    print(f"Total horas trabajadas: {horas_trabajadas} horas.")
    print(f"Total horas extra: {horas_trabajadas-48} horas.")
    print(f"Sueldo total: ${salario_total}.")
"""
#ejercicio.19
"""
compra=float(input("Ingrese la cantidad de lapices a comprar: "))
if compra < 1000:
    print(f"El total de su compra es de: ${compra*60}")
else:
    descuento=(compra*60)*0.07
    precio_final=(compra*60)-descuento
    print("Con la compra de mas de 1000 lapices obtuvo un descuento del 7%.")
    print(f"El total de su compra es de: ${precio_final}")
"""
#ejercicio.20

nota1=float(input("Ingresa la primer nota: "))
nota2=float(input("Ingresa la segunda nota: "))
nota3=float(input("Ingresa la tercer nota: "))
nota4=float(input("Ingresa la cuarta nota: "))

suma_notas=nota1+nota2+nota3+nota4
promedio=suma_notas/4

if promedio >= 6:
    print(f"Aprobaste con un promedio de {promedio}")
else:
    print(f"Desaprobaste con un promedio de {promedio}")