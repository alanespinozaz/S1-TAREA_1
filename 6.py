# """  1. Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa, 
#  sabiendo que cuando las horas de trabajo exceden de 40, el resto  se consideran horas extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8;  
#  si las horas extras exceden de 8 se pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto al triple. """
 
 
class Tarea:
     def __init__(self):
         pass
     def calculoPago(self):
        ht, he, het = 0,0,0 
        ph,  phe, pt = 0,0,0
        
        ht = int(input("Ingrese horas trabajadas:  "))
        ph = float(input("Ingrese valor x hora:  "))
        if ht > 40: # debe ser 41 para calcular las horas extras
          print("En proceso de calculo...")
          he = ht - 40
          if he > 8:
             het = he - 8
             he=8
             phe = ph * 2 * he + ph * 3 * het
          else:
               phe = ph * 2 * he 
          pt = ph*40 +phe   
          
        else:
            pt = ph * ht
            
        print("El pago total de horas trabajadas: ", pt)
        
tarea = Tarea()
tarea.calculoPago()
