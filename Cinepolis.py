class Cinepolis:

    def __init__(self):
        self.boletos = []  

    def calcular_descuento(self, cantidad_boletos, usa_tarjeta):
        precio_boletos = cantidad_boletos * 12  # 12 es el precio de los boletos

        if cantidad_boletos > 5:
            descuento = precio_boletos * 0.15
        elif 3 <= cantidad_boletos <= 5:
            descuento = precio_boletos * 0.10
        else:
            descuento = 0

        total = precio_boletos - descuento

        if usa_tarjeta:
            total = total * 0.10

        return total

    def mostrar_menu_principal(self):
        print("\n   Menú Principal ") 
        print("1. ¿Quieres comprar? ---- Ingresa el numero 1")
        print("2. Terminar ---- Ingresa el numero 2")

    def mostrar_menu_pago(self, nombre):
        print(f"\n Pago para el cliente  {nombre} ")  
        print("1. Pagar con tarjeta CINECO ------Ingresa 1")
        print("2. Pagar en efectivo---------Ingresa 2")

    def realizar_compra(self):
        nombre = input("Ingresa tu nombre: ")
        personas = int(input("¿Cuántas personas vienen contigo?: "))
        boletos = int(input("¿Cuántos boletos van a comprar?: "))

        while boletos > 7 * personas:
            print(f"No puedes comprar más de {7 * personas} boletos.")
            print("1. Cambiar la cantidad de boletos")
            print("2. Cambiar la cantidad de personas")
            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                boletos = int(input("Ingresa la nueva cantidad de boletos: "))
            elif opcion == 2:
                personas = int(input("Ingresa la nueva cantidad de personas: "))
            else:
                print("Opción inválida, intenta de nuevo.")

        while True:
            self.mostrar_menu_pago(nombre)
            opcion_pago = int(input("Selecciona una opcion del menu: "))

            if opcion_pago == 1:
                usa_tarjeta = True
                total = self.calcular_descuento(boletos, usa_tarjeta)
                print(f"Total a pagar con tarjeta CINECO: ${total:.2f}")
                self.boletos.append((nombre, total))
            elif opcion_pago == 2:
                usa_tarjeta = False
                total = self.calcular_descuento(boletos, usa_tarjeta)
                print(f"Total a pagar en efectivo: ${total:.2f}")
                self.boletos.append((nombre, total))
            else:
                print("Intenta de nuevo")
                continue

            print("Ingresa 4 para salir y guardar compra")
            salir_opcion = int(input("Selecciona una opción: "))
            if salir_opcion == 4:
                self.guardar_compras()
                print("Compra guardada")
                return


  # Guardar compras en un archivo

    def guardar_compras(self):
        archivo = open("compras_cinepolis.txt", "w")  
        archivo.write("Nombre\tTotal\n")  # \t es para separar un espacio grande en el lado 
        archivo.write("-----------------------------\n") 
        
        for nombre, total in self.boletos:  # Recorrer lista de boletos
            archivo.write(nombre + "\t$" + str(round(total, 2)) + "\n")  
            
        archivo.close()  # Cerrar archivo txt

# Mostrar las compras guardadas   

    def mostrar_tabla_compras(self):
        print("\nCompras de Boletos")
        archivo = open("compras_cinepolis.txt", "r")  # La r es para lectura
        print(archivo.read())  # Muestra el contenido en la terminal
        archivo.close()

        
        total_general = 0
        for nombre, total in self.boletos:
            total_general += total
        
        print(f"\nTotal de todos los boletos: ${round(total_general, 2)}")


    def iniciar(self):
        while True:
            self.mostrar_menu_principal()
            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                self.realizar_compra()
            elif opcion == 2:
                self.guardar_compras()
                self.mostrar_tabla_compras()
                print("Hasta luego")
                break
            else:
                print("Intenta de nuevo")

if __name__ == "__main__":
    cinepolis = Cinepolis()
    cinepolis.iniciar()
