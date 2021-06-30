# """  Dado como dato la calificación de un alumno en un examen, 
#  escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario. """


class Ejemplo4:
    def __init__(self):
        pass
    
    def aporepro(self):
        cal = float(input("Ingrese su Nota final:  "))
        if cal >= 7:
            print("Felicitaciones usted aprobo el curso {} ".format(cal))   
        else:
            print("Usted ha Reprobado el curso {} ".format(cal))
        
eje4 = Ejemplo4()
eje4.aporepro()