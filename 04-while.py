''' Ejemplo 1

x=0

while x<10:
    print(x)
    x=x+1

'''

'''  Practica operaciones de multipliacacion de a x b utilizando sumas 
a=3
b=4
salida: 3+3+3+3=12

'''

a = int(input("Ingresa el primer valor: "))
b = int(input("Ingresa el segundo valor: "))

resultado = 0
contador = 0
salida = ""

while contador < b:
    resultado = resultado + a  
    if contador < b - 1:
        salida = salida + f"{a}+"
    else:
        salida = salida + f"{a}"
    contador = contador + 1  

print(f"salida: {salida}={resultado}")

