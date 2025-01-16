''' For recorrer listas'''

range(20)   #Va generar una lista del 0 al 9


'''Ejercicio 1'''
for  i in range(20):
    print(i)  #Va generar una lista del 0 al 9


''' Practica Tabla de multiplicacion'''

num = int(input("Ingresa un número "))

print(f"Tabla de multiplicar del {num}:")
for i in range(11):  
    resultado = num * i
    print(f"{num} x {i} = {resultado}")


