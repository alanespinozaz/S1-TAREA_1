# """ Diseñe un pseudocódigo para calcular la suma y producto de N números enteros,
# utilizando un bucle controlado por centinela """
 
class Ejemplo13():
    def __init__(self):
        pass
    
    def sumprocenti (self):
        sum=0
        prod=1
        num= int(input("Ingrese cualquier numero para realizar calculos: "))
        while num >= 0:
            
            num= int(input("Escriba el numero: "))
            if num <=  -1:
                 break
           
            sum= sum+num
            prod= prod*num
            print("El total de la suma es: ",sum)
            print("El total del producto es: ", prod)
            
            
        if num <=  -1:
         print("Gracias")
            
       
        
eje13= Ejemplo13()
eje13.sumprocenti()