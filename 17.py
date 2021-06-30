class Ejemplo17:
    def __init__(self):
        pass

    def Examenes(self):

        exa1= float(input("Ingrese la nota del examen 1: "))
        exa2= float(input("Ingrese la nota del examen 2: "))

        if exa1 > 79 and exa2 > 79:
            print("Aceptado")
        else:
            print("Rechazado")

eje17 = Ejemplo17()
eje17.Examenes()
