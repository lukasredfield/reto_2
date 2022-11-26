import random

# puerta_1=''
# puerta_2=''
# puerta_3=''

# Problema_de_Monty_Hall = {
#     puerta_1:'',puerta_2:'',puerta_3:''
# }

# for i in range(100000):

#     desenlace = random.choice(['cabra','cabra','auto'])
#     input('Monty Hall dice: Elige una puerta!:')

desenlace = random.choice(['cabra','cabra','auto'])

def juego():   

    desenlace = random.choice(['cabra','cabra','auto'])

    for detras_de_la_puerta in desenlace:
        puerta_elegida = input('Monty Hall dice: Elige una puerta!: Puerta 1\
            Puerta 2\
                Puerta 3')

        if detras_de_la_puerta is True:
            desenlace = detras_de_la_puerta
            print('Y detras de la puerta hay...', detras_de_la_puerta)


juego()

#print(desenlace)


#     input('Monty Hall dice: Elige una puerta!:')


