#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

numero_entero = 5
if numero_entero > 0:
    print("El número es mayor que cero.")
elif numero_entero < 0:
    print("El número es menor que cero.")
else:
    print("El número es igual a cero.")



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

variable1 = 5
variable2 = "Hola"
if type(variable1) == type(variable2):
    print("Las variables son del mismo tipo de dato.")
else:
    print("Las variables son de tipos diferentes.")



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} es par.")
    else:
        print(f"{i} es impar.")



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(6):
    print(f"{i} elevado a la potencia 3 es {i**3}.")



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

numero_entero = 7
for _ in range(numero_entero):
    print("Iteración.")



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

numero_factorial = 5
if (numero_factorial > 0 and (type(numero_factorial) == int)):
    factorial = 1
    while numero_factorial > 0:
        factorial *= numero_factorial
        numero_factorial -= 1
    print(f"El factorial es: {factorial}")
else:
    print(f'La variable no puede usarse como factorial')


# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

contador = 0
while contador < 3:
    for i in range(3):
        print(f"Contador: {contador}, i: {i}")
    contador += 1



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

for i in range(3):
    contador = 0
    while contador < 3:
        print(f"Contador: {contador}, i: {i}")
        contador += 1




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

for num in range(2, 31):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

for num in range(2, 31):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

# La optimización se basa en eliminar una variable booleana y una condición dentro del bucle, 
#        lo que reduce la cantidad de operaciones
#         y hace que el código sea más claro y eficiente.


# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

numero = 99
while numero <= 300:
    numero += 1
    if (numero % 12 != 0):
        continue
        
    print(numero)
    



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

while True:
    entrada = input("Ingrese un número (o 'q' para salir): ")
    if entrada == 'q':
        break
    try:
        numero = int(entrada)
        if es_primo(numero):
            print("Es primo.")
        else:
            print("No es primo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
numero = 100
while numero <= 300:
    if numero % 3 == 0 and numero % 6 == 0:
        print(f"El primer número divisible por 3 y múltiplo de 6 es: {numero}")
        break
    numero += 1



# %%
