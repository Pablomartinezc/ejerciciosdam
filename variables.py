import re
from sys import argv

#Ejercicios Tipos

#Ejercicio 1
nombre = "Juan Perez"

balance = 53.44



print("Hola %s. Tu balance es de %f $ " % (nombre,balance))


#Ejercicio 2
float_1 = 345.5

print(str(float_1))


#Ejercicio 3
num1 = 345
str1 = "Hola"
float1 = 456.1

print(len(str(num1)))
print(len(str1))
print(len(str(float1)))


#Ejercicio 4
cadena = "buenas  "

print(cadena.rstrip())

print(cadena.rsplit(", "))

print(cadena.lower())

print(cadena.upper())

print(cadena.find("a"))

print(cadena.index("b"))

print(cadena.startswith("buenas"))

#Ejercicio 5
quijote = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."

conteo = re.findall(r"a", quijote)

for conteo in enumerate(conteo):
    print(conteo)

#Ejercicios Entrada

#Ejercicio 1,2,3
prompt = '> '

mancha = input(prompt)
texto = input(prompt)

print ("En un lugar de la %s, de cuyo nombre no quiero %s"% (mancha, texto))
print ("Vive un caballero.")
print ("Escriba el nombre del caballero")
nombrecaballero = input(prompt)

print ("Correcto, el caballero %s" % (nombrecaballero))

print("Escriba un numero")

numeroescrito = input(prompt)
numeroescrito = str(numeroescrito)

print("El numero escrito es %s " % numeroescrito)

#Ejercicios Listas

#Ejercicio 1

fruits = ["apple", "banana", "cherry"]
print(fruits[1])


fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi" 

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")


fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Ejercicio 2

asignaturas = ["Matematicas", "fisica", "quimica", "historia", "lengua"]
print(asignaturas)

#Ejercicio 3

asignaturas = ["Matematicas", "fisica", "quimica", "historia", "lengua"]
for asignaturas in asignaturas:
    print("Yo estudio :", asignaturas)


#Ejercicio 4

set1 = set(["Matematicas","quimica", "historia", "lengua"])

print("Escribe el nombre de una asignatura para saber si esta en el set")

asignatura = input(prompt)

print(asignatura in set1)

#Ejercicio 5

listanumero = [1,2,3]
listanumero.append(1)
listacadenas = ["hola","mundo"]
listacadenas.append("adios")

#Ejercicio 6 

setA = {"Jake", "John", "Eric"}
setB = {"John", "Jill"}

print(setA.difference(setB))


#Ejercicios Estructuras de control


#Ejercicio 1

a = 50
b = 10
if a > b:
  print("Hello World")

a = 50
b = 10
if a != b:
  print("Hello World")


a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")


a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

c = 20
d = 30

if a == b and  c == d:
  print("Hello")

if a == b or c == d:
  print("Hello")


if 5 > 2:
  print("Five is greater than two!")



if 5 > 2: print("Five is greater than two!")

print("Yes") if 5 > 2 else print("No")

#Ejercicio 2

print("Por favor indique su edad")

edad = input(prompt)
edad = int(edad)
if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


#Ejercicio 3

contraseña = "hola"

print("indique su contraseña")

contraseñaescrita = input(prompt)

if contraseña != contraseñaescrita:
    print("contraseña incorrecta")
else:
    print("Contraseña correcta")

#Ejercicio 4

print("Indique un numero")

numero = input(prompt)

numero = int(numero)

if numero % 2 == 0:
    print('El número', numero, 'es par.')
else:
    print('El número', numero, 'es impar.')


#Ejercicio 5

print("Escriba el primer numero")
num1 = input(prompt)
num1 = int(num1)
print("Escriba el segundo numero")
num2 = input(prompt)
num2 = int(num2)

if num1 / num2 == 0:
    print("Error el resultado da 0")
else:
    print("El resultado es: ", num1/num2)


#Ejercicios bucles

#Ejercicio 1

i = 1
while i < 6:
  print(i)
  i += 1


i = 1
while i < 6:
  if i == 3:
    break
  i += 1



i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)



i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#Ejercicio 2

print("Escriba un numero")
num = input(prompt)
num = int(num)

while num > 0:
    print(num)
    num -=1


#Ejercicio 3
print("Introduzca un numero")
num = input(prompt)
num = int(num)

for i in range(1, num+1, 2):
    print(i, end=", ")


#Ejercicio 4

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")


#Ejercicio 5

palabra = "salir"
texto =""
while texto != palabra:
    texto = input("Escriba salir para terminar el programa: ")
print("Confirmado salir")



#Ejercicios bucles + datos

#Ejercicio 1

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
puntuacion = []
for asignatura in asignaturas:
    punt = input("¿Qué nota has sacado en " + asignatura + "?")
    puntuacion.append(punt)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + puntuacion[i])



#Ejercicio 2

premiados = []
for i in range(6):
    premiados.append(int(input("Introduce un número ganador: ")))
premiados.sort()
print("Los números ganadores son " + str(premiados))

#Ejercicio 3

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobadas = []
for asignatura in asignaturas:
    score = float(input("¿Qué nota has sacado en " + asignatura + "?"))
    if score >= 5:
        aprobadas.append(asignatura)
for asignatura in aprobadas:
    asignaturas.remove(asignatura)
print("Tienes que repetir " + str(asignaturas))

#Ejercicio 4


palabra = input("Introduce una palabra: ")
alreves = palabra
palabra = list(palabra)
alreves = list(alreves)
alreves.reverse()
if palabra == alreves:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

#Ejercicio 5

palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales: 
    times = 0
    for letter in palabra: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")



#Ejercicio 6

diccionario = {}
palarbas = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palarbas.split(','):
    key, value = i.split(':')
    diccionario[key] = value
phrase = input('Introduce una frase en español: ')
for i in phrase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')

#Ejercicio 7

facturas = {}
recaudado = 0
pendiente = 0
more = ''
while more != 'T':
    if more == 'A':
        key = input('Introduce el número de la factura: ')
        cost = float(input('Introduce el coste de la factura: '))
        facturas[key] = cost
        pendiente += cost
    if more == 'P':
        key = input('Introduce el número de la factura a pagar: ')
        cost = facturas.pop(key, 0)
        recaudado += cost
        pendiente -= cost
    print('Recaudado:', recaudado)
    print('Pendiente de cobro: ', pendiente)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')

#Ejercicios ficheros

#Ejercicio 1

numero = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(numero) + '.txt'
f = open(file_name, 'w')
for i in range(1, 11):
    f.write(str(numero) + ' x ' + str(i) + ' = ' + str(numero * i) + '\n')
f.close()

#Ejercicio 2

numero = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(numero) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', numero)
else:
    print(f.read())






























