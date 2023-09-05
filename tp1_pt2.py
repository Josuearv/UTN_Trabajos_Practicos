#Trabajo Práctico N°1 (parte2)


#Ejercicio 1
base=float(input("Ingrese el valor de la base del rectangulo: "))
altura=float(input("Ingrese el valor de la altura del rectacgulo: "))

perimetro=2*(base+altura)
area=base*altura

print("El perimetro del rectángulo es de", perimetro, "cm; el area es de", area, "cm2.")

#Ejercicio 2
cat1=float(input("Ingrese el valor del primer cateto: "))
cat2=float(input("Ingrese el valor del segundo cateto: "))

suma_cat=cat1**2+cat2**2
hipotenusa=suma_cat**1/2

print("El valor de la hipotenusa es de", hipotenusa)

#Ejercicio 3
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))

suma=num1+num2
resta=num1-num2
div=num1/num2
mult=num1*num2

print("El resultado de la suma entre ambos números es", suma)
print("El resultado de la resta entre ambos números es", resta)
print("El resultado de la división entre ambos números es", div)
print("El resultado de la multipllicación entre ambon números es", mult)

#Ejercicio 4
grados_f=float(input("Ingrese la temperatura en grados Fahrenheit para convertirlos a grados Celsius: "))

grados_c=(grados_f-32)*5/9

print(grados_f, " grados Fahrenheit equivalen a", grados_c, " grados Celsius")

#Ejercicio 5
#   Punto a) En primer lugar, la variable es una letra mayúscula (lo cual no es un error pero si una mala práctica.
#           En segúndo lugar, no esta definida la variable "nombre"
#           En tercer lugar, la función "input" soporta un solo argumente y aquí se le están pasando 2
nombre=input("¿Cual es tu nombre?")
a=input("¿Cual es tu canción favorita?")
print("La canción favorita de", nombre, "es", a)

#   Punto b) No se especifica el tipo de fato que se ingresa por lo tanto no se pueden realizar operaciones matemáticas
precio=float(input("Precio:"))
total=precio+(precio*0.1)
print(total)

#   Punto c) En el print no se engloba el texto de salida entre comillas ("")
edad=int(input("Edad:"))
print("Tu edad es", edad)

#   Punto d) 
edad=int(input("Edad:"))
print("Veamos si tu edad es 18...", edad)

#Ejercicio 6
num1=float(input("Ingrese el primer número:"))
num2=float(input("Ingrese el segundo número:"))
num3=float(input("Ingrese el tercer número:"))

media=(num1+num2+num3)/3

print("La media entre", num1,",", num2,"y", num3, "es", media)

#Ejercicio 7
minutos_recibidos=int(input("Ingrese la cantidad de minútos que desea convertir:"))
hora=int(minutos_recibidos/60)
minutos_convertidos =minutos_recibidos%60
print(f'la conversion de los {minutos_recibidos} es {hora} horas y {minutos_convertidos} minutos')

#Ejercicio 8
sueldo_base = input('Digite su sueldo base: ')
valor_venta1 = int(input('Digite el valor de la primera venta: '))*0.1
valor_venta2 = int(input('Digite el valor de la segunda venta: '))*0.1
valor_venta3 = int(input('Digite el valor de la tercera venta: '))*0.1

sueldo_total = sueldo_base+valor_venta1+valor_venta2+valor_venta3

print(f'Su sueldo total en este mes sera de: {sueldo_total}')

#Ejercicio 9
precio=float(input("Ingrese el valor del producto:"))

descuento=precio*0.15
precio_final=precio-descuento

print("El valor final que tendrá que pagar es", precio_final)

#Ejercicio 10
nota_parcial_1=float(input("Ingrese la nota del primer parcial: "))
nota_parcial_2=float(input("Ingrese la nota del segundo parcial: "))
nota_parcial_3=float(input("Ingrese la nota del tercer parcial: "))
promedio_parcial=(nota_parcial_1+nota_parcial_2+nota_parcial_3)/3
porcentaje_parcial=promedio_parcial*0.55

nota_examen_final=float(input("Ingrese la nota del exámen final: "))
porcentaje_examen=nota_examen_final*0.3

nota_trabajo_final=float(input("Ingrese la nota del trabajo final: "))
porcentaje_trabajo=nota_trabajo_final*0.15

nota_final=porcentaje_examen+porcentaje_parcial+porcentaje_trabajo
print("La nota final es", nota_final)

#Ejercicio 11
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese un segundo número: "))

print(f'la distancia entre {num1} y {num2} es de {abs(num1-num2)}')

#Ejercicio 12
num=float(input("Ingrese un número: "))

raiz_cuadrada=(num)**1/2
raiz_cubica=(num)**1/3

print("La raiz cuadrada de", num, "es", raiz_cuadrada, "y la raiz cubica es", raiz_cubica)

#Ejercicio 13

num=input("Ingrese el numero que quiere invertir : ")
print(f'el numero {num} invertido es: {num[-1:-len(num)-1:-1]}')

#Ejercicio 14
a=float(input("Ingrese un número para la variable A: "))
b=float(input("Ingrese un número para la variable B: "))

c=b
b=a
a=c

print("La variable A ahora vale", a)
print("La variable B ahora vale", b)

#Ejercicio 15

# Obtener la hora de partida y el tiempo de viaje en segundos
hora_partida = int(input("Hora de partida (HH): "))
minuto_partida = int(input("Minuto de partida (MM): "))
segundo_partida = int(input("Segundo de partida (SS): "))
tiempo_viaje = int(input("Tiempo de viaje en segundos (T): "))

# Calcular el tiempo total en segundos de la hora de partida y el tiempo de viaje
tiempo_total_partida = hora_partida * 3600 + minuto_partida * 60 + segundo_partida
tiempo_llegada = tiempo_total_partida + tiempo_viaje

# Calcular las horas, minutos y segundos de llegada
hora_llegada = tiempo_llegada // 3600
minuto_llegada = (tiempo_llegada % 3600) // 60
segundo_llegada = tiempo_llegada % 60

# Imprimir la hora de llegada
print(f"Hora de llegada: {hora_llegada:02d}:{minuto_llegada:02d}:{segundo_llegada:02d}")

#Ejercicio 16
nombre=str(input("Ingrese su nombre: "))
apellido1=str(input("Ingrese su primer apellido: "))
apellido2=str(input("Ingrese su segudno apellido: "))

i1=nombre[0]
i2=apellido1[0]
i3=apellido2[0]

print("Sus iniciales son", i1, i2, i3)

#Ejercicio 17
usuario=str(input("Ingrese su nombre: "))
print("Ahora estás en la matrix,", usuario)

#Ejercicio 18
costo_cena=float(input("Ingrese de cuanto fue el valor de la cena: "))

servicio=costo_cena*(6.2/100)
propina=costo_cena*(10/100)
monto_final=costo_cena+servicio+propina

print("El monto final a pagar es de", monto_final)

#Ejercicio 19
dia=int(input("Ingrese el día de su nacimiento (en número): "))
mes=int(input("Ingrese el mes de su nacimiento (en número): "))
ano=int(input("Ingrese el año de su nacimiento: "))

print(dia,"/", mes, "/", ano)

#Ejercicio 20
fecha=int(input("Ingrese su fecha de nacimiento (en números y sin espacios): "))
print(fecha)

#Ejercicio 21

km_por_litro = float(input("Kilómetros por litro de combustible: "))
capacidad_tanque = float(input("Capacidad del tanque en litros: "))
km_totales = float(input("Kilómetros totales del viaje: "))


litros_necesarios = km_totales / km_por_litro
tanques_necesarios = litros_necesarios / capacidad_tanque


print(f"Para el viaje de {km_totales} km, necesitarás {tanques_necesarios:.2f} tanques de combustible.")

