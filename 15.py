""" Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N 
y calcular el resultado de la siguiente serie: """


class Ejemplo15:
    def __init__(self):
        pass
    def numentero(self):
      t = 1
      c1 = 1
      cont = 1
      c2 = 2
      n=int(input("ingrese un numero"))
      while n<2:
        print("El numero debe ser mayor a 1")
        n=int(input("intente de nuevo:"))
      while cont<n:
        if c2%2==0:
          t=t-(1/(c1+1))
        else:
         t=+(1/(c1+1))
         c1=c1+1
         c2=c2+1
         cont=cont+1
        print(t)    
        
        
eje15 = Ejemplo15() 
eje15.numentero()     
