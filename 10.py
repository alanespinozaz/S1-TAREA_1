
class Ejemplo10:
    def __init__(self):
        pass

    def sumaCuadradaos(self):
        acu=0
        cont=1
        n=0

        while cont < 101 :
            n=(cont)**2 
            acu+=n
            cont=cont+1
        print(acu)

eje10 = Ejemplo10()
eje10.sumaCuadradaos()
