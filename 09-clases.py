
class OperasBas:
    #Ejercicio de propiedades 

    #public num1=0 #num1=0
    #private  num2=0 #_num2=0

    num1=0
    _num2=0
    res=0



    #Declaracion del constructor

    def _init_(self, num1, um2):
        self.num1=num1
        self.um2=um2

    #declaracion de metodos de la clase 

    def suma(self):
         self.res=self.num1+self.um2
         print("La suma es: {}".format(self.res))

    def resta(self):
         self.res=self.num1+self.um2
         print("La suma es: {}".format(self.res))


def main():
    obj=OperasBas(3,4)
    obj.suma()

if __name__=="_main_":
    main()


