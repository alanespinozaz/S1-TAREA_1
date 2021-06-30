
# """ Determinar si un número entero proporcionado por el usuario es primo. 
# Un número primo es un entero que no tiene más divisores que él mismo y la unidad.  """



class Ejemplo14:
    def __init__(self):
        pass
    def evaluarprimo(self):
        divisor, num, res= 0,0,0
        primo = True
        divisor = 2
        num = int(input("ingrese el numero:"))
        while divisor < num:
            res = num/2
            if res<0:
                divisor = divisor+1
                print("f")
            if primo == True:
                print("numero:",num,"no es primo:")
        else: 
            print("numer:",num,"no es primo:")
                
                   
eje14 = Ejemplo14()
eje14.evaluarprimo()            
    