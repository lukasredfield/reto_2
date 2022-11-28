import random

class Intentos:

    aciertos = 0
    fallos = 0

class Reto_2:

    eleccion = 0

    def puertas(self):
        lista = ["cabra", "cabra", "auto"]
        diccionario=dict()
        random.shuffle(lista)
        for i in range(1,4):
            diccionario[i]=lista[i-1]

        return diccionario

    def puerta_extra(self):
        lista = ["cabra", "cabra", "cabra", "auto"]
        random.shuffle(lista)
        print(lista)

        diccionario=dict()

        for i in range(1,5):
            diccionario[i]=lista[i-1]

        print(diccionario)

        return diccionario

    def monty_hall(self, diccionario):
        print("monty hall enseña 3 puertas y dice, elige una puerta, en una de ellas se encuentra un auto, y en las otras 2 se encuentra una cabra")
        self.eleccion=random.randrange(1,3)
        for i in range(1,4):
            if(i!=self.eleccion and diccionario[i]!="auto"):
                del diccionario[i]
                break
        print("monty abre la puerta " + str(i) + " y sale una cabra, luego pregunta, queres mantener tu eleccion o preferis cambiar de puerta?")
        return diccionario

    def monty_hall_no_sabe(self, diccionario):
        print("monty hall enseña 3 puertas y dice, elige una puerta, en una de ellas se encuentra un auto, y en las otras 2 se encuentra una cabra")
        self.eleccion=random.randrange(1,3)
        return diccionario

    def monty_hall_puerta_agregada(self, diccionario):
        print("monty hall enseña 4 puertas y dice, elige una puerta, en una de ellas se encuentra un auto, y en las otras 3 se encuentra una cabra")
        self.eleccion=random.randrange(1,4)
        for i in range(1,5):
            if(i!=self.eleccion and diccionario[i]!="auto"):
                del diccionario[i]
                break
        print("monty abre la puerta " + str(i) + " y sale una cabra, luego pregunta, queres mantener tu eleccion o preferis cambiar de puerta?")
        return diccionario

    def eleccion_firme(self, diccionario):
        puerta_elegida = diccionario[self.eleccion]
        if(puerta_elegida=='auto'):
            return True
        else:
            return False

    def cambio_de_eleccion(self, diccionario):
        lista=[]
        for k in diccionario.keys():
            lista.append(k)
        random.shuffle(lista)
        for i in lista:
            if(i!=self.eleccion):
                self.eleccion=i
                break
        puerta_elegida = diccionario[self.eleccion]
        if(puerta_elegida=='auto'):
            return True
        else:
            return False


def juego_sin_ayuda(reintentos):

    intentos=Intentos()
    premio=False

    for i in range(1, reintentos):
        juego=Reto_2()
        puertas=juego.puertas()
        premio=juego.cambio_de_eleccion(juego.monty_hall_no_sabe(puertas))
        if(premio==True):
            intentos.aciertos+=1
        else:
            intentos.fallos+=1
    
    print("consegui el premio " + str(intentos.aciertos) + " veces")
    print("tuve en total " + str(intentos.aciertos) + " aciertos y " + str(intentos.fallos) + " fallos")


def juego(tres_puertas, cambiar_decision, reintentos):
    
    intentos=Intentos()
    puertas=dict()
    premio=False

    if reintentos==1:
        lista1=['auto', 'cabra', 'cabra']
        print(lista1)
        print("supongamos que siempre elijo la puerta numero 1, monty descarta una de las puertas con cabra en este caso la 2")
        print("quedarian la puerta 1 y la 3, si yo cambiara de la 1 a la 3 perderia en este caso")
        lista2=['cabra', 'auto', 'cabra']
        print(lista2)
        print("monty descarta la puerta 3, quedarian la puerta 1 y la 2, si yo cambiara de la 1 a la 2 ganaria")
        lista3=['cabra', 'cabra', 'auto']
        print(lista3)
        print("monty descarta la puerta 2, quedarian la puerta 1 y la 3, si yo cambiara de la 1 a la 3 ganaria")
        print("en conclusion, cambiar de puerta siempre incrementara tus posibilidades de ganar")
        # puertas_restantes=juego.monty_hall(puertas)
        # print(puertas_restantes)

    else:
        for i in range(1, reintentos):
            juego=Reto_2()
            if(tres_puertas==True):
                puertas=juego.puertas()
                if(cambiar_decision==True):
                    premio=juego.cambio_de_eleccion(juego.monty_hall(puertas))
                    if(premio==True):
                        intentos.aciertos+=1
                    else:
                        intentos.fallos+=1
                else:
                    premio=juego.eleccion_firme(juego.monty_hall(puertas))
                    if(premio==True):
                        intentos.aciertos+=1
                    else:
                        intentos.fallos+=1
            else:
                puertas=juego.puerta_extra()
                if(cambiar_decision==True):
                    premio=juego.cambio_de_eleccion(juego.monty_hall_puerta_agregada(puertas))
                    if(premio==True):
                        intentos.aciertos+=1
                    else:
                        intentos.fallos+=1
                else:
                    premio=juego.eleccion_firme(juego.monty_hall_puerta_agregada(puertas))
                    if(premio==True):
                        intentos.aciertos+=1
                    else:
                        intentos.fallos+=1

        print("consegui el premio " + str(intentos.aciertos) + " veces")
        print("tuve en total " + str(intentos.aciertos) + " aciertos y " + str(intentos.fallos) + " fallos")

juego(False, False, 100000)
#juego_sin_ayuda(1000)

#juego(True, True, 1)

