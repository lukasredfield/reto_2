import random


desenlace = random.choice(['cabra','cabra','auto'])

def Problema_de_Monty_Hall():  

    puerta_1=''
    puerta_2=''
    puerta_3='' 

    puertas = random.shuffle([puerta_1,puerta_2,puerta_3]) 

    #puertas = random.choice(['cabra','cabra','auto'])

    Dic_Problema_de_Monty_Hall = {
    1 : puerta_1, 2: puerta_2,3 : puerta_3
}


    for detras_de_la_puerta in desenlace:
        puerta_elegida = input('Monty Hall dice: Elige una puerta!:    Puerta 1\
            Puerta 2\
                Puerta 3:')

        if detras_de_la_puerta is True:
            desenlace = detras_de_la_puerta
            print('Y detras de la puerta hay...', detras_de_la_puerta)


puerta_1='cabra'
puerta_2='cabra'
puerta_3='auto' 

puertas = random.shuffle([puerta_1,puerta_2,puerta_3]) 

# puerta_1=''
# puerta_2=''
# puerta_3='' 
# puertas = [puerta_1,puerta_2,puerta_3]

# puertas = random.choice(['cabra','cabra','auto'])

print(puertas)


#     input('Monty Hall dice: Elige una puerta!:')


# for i in range(100000):

#     desenlace = random.choice(['cabra','cabra','auto'])
#     input('Monty Hall dice: Elige una puerta!:')