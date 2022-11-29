import random

class Intentos:
    autos = 0
    cabras = 0

class Monty_Hall:

    mi_eleccion = 0

    def tres_puertas(self):
        """este metodo retorna las 3 puertas con sus premios mezclados aleatoriamente"""
        premios = ["cabra", "cabra", "auto"]
        puertas=dict()
        random.shuffle(premios)
        for numeros in range(1,4):
            puertas[numeros]=premios[numeros-1]

        return puertas

    def cuatro_puertas(self):
        """este metodo retorna las 4 puertas con sus premios mezclados aleatoriamente"""
        premios = ["cabra", "cabra", "cabra", "auto"]
        puertas=dict()
        random.shuffle(premios)
        for numeros in range(1,5):
            puertas[numeros]=premios[numeros-1]

        return puertas

    def juego_original(self, puertas):
        """este metodo descarta una de las 3 puertas mientras no sea la que elegi y mientras no tenga el auto, luego retorna las 2 puertas restantes"""
        print("monty hall enseña 3 puertas y dice: Elige una puerta! En una de ellas se encuentra un auto, y en las otras 2 se encuentra una cabra")
        self.mi_eleccion=random.randrange(1,3) 
        """Ahí se produjo la elección del concursante"""
        for numero_de_puerta in range(1,4):
            if(numero_de_puerta!=self.mi_eleccion and puertas[numero_de_puerta]!="auto"):
                del puertas[numero_de_puerta]
                print("monty abre la puerta " + str(numero_de_puerta) + " y sale una cabra, luego pregunta: ¿Querés mantener tu eleccion o preferis cambiar de puerta?")
                break
        return puertas
        

    def juego_con_cuatro_puertas(self, puertas):
        """este metodo descarta una de las 4 puertas mientras no sea la que elegi y mientras no tenga el auto, luego retorna las 3 puertas restantes"""
        print("monty hall enseña 4 puertas y dice, elige una puerta, en una de ellas se encuentra un auto, y en las otras 3 se encuentra una cabra")
        self.mi_eleccion=random.randrange(1,4)
        for numero_de_puerta in range(1,5):
            if(numero_de_puerta!=self.mi_eleccion and puertas[numero_de_puerta]!="auto"):
                del puertas[numero_de_puerta]
                print("monty abre la puerta " + str(numero_de_puerta) + " y sale una cabra, luego pregunta, queres mantener tu eleccion o preferis cambiar de puerta?")
                break
        return puertas

    def juego_sin_ayuda_de_monty(self, puertas):
        """este metodo no descarta puertas, solo elige una la puerta"""
        print("monty hall enseña 3 puertas y dice, elige una puerta, en una de ellas se encuentra un auto, pero no sabe en cual")
        self.mi_eleccion=random.randrange(1,3)
        return puertas

    def primera_eleccion(self, puertas):
        """recibo por parametro las puertas restantes y la primera eleccion, si encuentra el auto devuelve True, caso contrario, False"""
        if(puertas[self.mi_eleccion]=='auto'):
            return True
        else:
            return False

    def cambio_de_eleccion(self, puertas):
        """recibo las puertas restantes, las mezclo y elijo la primer puerta que sea diferente a mi primer eleccion, luego compruebo si gane el auto"""
        numeros_de_las_puertas_restantes=[]
        for numeros_de_puertas in puertas.keys():
            numeros_de_las_puertas_restantes.append(numeros_de_puertas)
        random.shuffle(numeros_de_las_puertas_restantes)
        for numero_de_puerta in numeros_de_las_puertas_restantes:
            if(numero_de_puerta!=self.mi_eleccion):
                self.mi_eleccion=numero_de_puerta
                break
        if(puertas[self.mi_eleccion]=='auto'):
            return True
        else:
            return False



def juego_sin_descarte(reintentos):
    """este es el juego en el que monty no sabe donde esta el auto, por ende no descarta ninguna puerta"""
    intentos=Intentos()
    auto=False

    for intentos_de_juego in range(1, reintentos):
        monty_hall=Monty_Hall()
        puertas=monty_hall.tres_puertas()
        auto=monty_hall.cambio_de_eleccion(monty_hall.juego_sin_ayuda_de_monty(puertas))
        if(auto==True):
            intentos.autos+=1
        else:
            intentos.cabras+=1
    
    print("consegui el auto " + str(intentos.autos) + " veces")
    print("tuve en total " + str(intentos.autos) + " aciertos y " + str(intentos.cabras) + " fallos")
    print("da igual si cambio o no de elección, el numero de puertas es el mismo, por ende no modifica mis probabilidades")


def jugar(tres_puertas, cambiar_decision, reintentos):
    """recibo un booleano para jugar con 3 (True) o 4 puertas (False), otro booleano para jugar manteniendo (False) o cambiando (True) mi decision y el numero de veces a jugar (?)"""
    
    intentos=Intentos()
    puertas=dict()
    auto=False

    if reintentos==1:
        """si se juega 1 sola vez, se enseña la logica de las probabilidades del juego"""
        posibilidad_1=['auto', 'cabra', 'cabra']
        print(posibilidad_1)
        print("supongamos que siempre elijo la puerta numero 1, monty descarta una de las puertas con cabra en este caso la 2")
        print("quedarian la puerta 1 y la 3, si yo cambiara de la 1 a la 3 perderia en este caso")
        print()
        posibilidad_2=['cabra', 'auto', 'cabra']
        print(posibilidad_2)
        print("monty descarta la puerta 3, quedarian la puerta 1 y la 2, si yo cambiara de la 1 a la 2 ganaria")
        print()
        posibilidad_3=['cabra', 'cabra', 'auto']
        print(posibilidad_3)
        print("monty descarta la puerta 2, quedarian la puerta 1 y la 3, si yo cambiara de la 1 a la 3 ganaria")
        print("en conclusion, gane 2 veces al cambiar de puerta, cambiar de puerta siempre incrementara tus posibilidades de ganar")

    else:
        for intentos_de_juego in range(1, reintentos):
            monty_hall=Monty_Hall()
            if(tres_puertas==True):
                puertas=monty_hall.tres_puertas()
                if(cambiar_decision==True):
                    auto=monty_hall.cambio_de_eleccion(monty_hall.juego_original(puertas))
                    if(auto==True):
                        intentos.autos+=1
                    else:
                        intentos.cabras+=1
                else:
                    auto=monty_hall.primera_eleccion(monty_hall.juego_original(puertas))
                    if(auto==True):
                        intentos.autos+=1
                    else:
                        intentos.cabras+=1
            else:
                puertas=monty_hall.cuatro_puertas()
                if(cambiar_decision==True):
                    auto=monty_hall.cambio_de_eleccion(monty_hall.juego_con_cuatro_puertas(puertas))
                    if(auto==True):
                        intentos.autos+=1
                    else:
                        intentos.cabras+=1
                else:
                    auto=monty_hall.primera_eleccion(monty_hall.juego_con_cuatro_puertas(puertas))
                    if(auto==True):
                        intentos.autos+=1
                    else:
                        intentos.cabras+=1

        print("consegui el auto " + str(intentos.autos) + " veces")
        print("tuve en total " + str(intentos.autos) + " aciertos y " + str(intentos.cabras) + " fallos")


if __name__=='__main__':
    jugar(True, True, 100000) # En esta función se juega el Problema de Monty Hall con las reglas de los distintos escenarios planteados en el reto 1 y sus respectivas resoluciones.

    juego_sin_descarte(1000) # En este escenario Monty Hall no elimina puertas y se puede ver cómo se acierta al auto el 33% de las veces.

    jugar(True, True, 1) #Acá se llama al juego original con un solo intendo, mostrando la lógica de este y como siempre se tiene más posibilidades de acertar el auto cambiando de elección.

