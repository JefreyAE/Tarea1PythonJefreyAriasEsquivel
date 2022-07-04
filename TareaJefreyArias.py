import random

#Ejercicio 1-7
lista = [1,2,3,-4,-5,6,7,-8,-9]
pos = 0
for val in lista:
    if val < 0:
        lista[pos] = 0
    pos += 1
print(lista)

#Ejercicio 2-8

dimAleat = random.randint(5,10)
rangoAleat = range(dimAleat)
listaBase = []
print(f'Debes ingresar {dimAleat} números')

for l1  in rangoAleat:
    n = input('Ingresa un número, y presiona Enter: ')
    listaBase.append(n)

listaPar = []
listaImpar = []

indice = 0
for val in listaBase:

    if (indice % 2) == 0:
        listaPar.append(val)
    else:
        listaImpar.append(val)
    indice += 1

print(listaBase)
print(listaPar)
print(listaImpar)

#Ejercicio 3-9

x = range(1,4)
cuadrados = []
for val in x:
    cuadrados.append(val **2)

print(cuadrados)

#Ejercicio 4-10

listaNormal = []
listaInversa = []

for val in range(0,9):
    listaNormal.append(random.randint(1,10))

idr = len(listaNormal) - 1
while (idr >= 0):
  listaInversa.append(listaNormal[idr])
  idr -=  1

print(listaNormal)
print(listaInversa)

#Ejercicio 5-11

def sumaEnt(list):
    suma = 0
    for val in list:
        suma += val
    return suma
lista = list(range(5,10))

resultado = sumaEnt(lista)
print(f'La lista: {lista}')
print(f'La suma del contenido de la lista es de: {resultado}')


#Ejercicio 6-13

list = [30,6,11,4,1,10,20,63,100,80,77,45,95,26]

inicial = 0
dif = 0
cont = 0
cercano = 0
difAnt = 0
for val in list:

    if cont == 0:
        inicial = list[0]
    else:
        dif = abs(inicial - val)
        difAnt = abs(inicial - cercano)
        if dif < difAnt:
            cercano = val

    cont +=1

print(cercano)