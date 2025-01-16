import os



'''Ejercicio 1'''
'''
def funcion1():
    print("Hola, soy la funcion 1")

def funcion2():
    print("Hola, soy la funcion 2")

def run():
    funcion1()
    funcion2()
    
run()'''

'''El run() es como el main'''




'''Ejercicio 2 Practica'''


def funcion1():
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    suma = num1 + num2
    print(f'Resultado: {suma}')


def funcion2():
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    resta = num1 - num2
    print(f'Resultado: {resta}')


def funcion3():
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    multiplicacion = num1 * num2
    print(f'Resultado: {multiplicacion}')


def funcion4():
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    if num2 != 0:
        division = num1 / num2
        print(f'Resultado: {division}')
    


def run():
    while True:  
        print('Menú:')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Salir')
        opcion = int(input('Elige una opción: '))
        
        if opcion == 1:
            funcion1()
        elif opcion == 2:
            funcion2()
        elif opcion == 3:
            funcion3()
        elif opcion == 4:
            funcion4()
        elif opcion == 5:
            print("¡Salir :) !")
            break  
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    run()



