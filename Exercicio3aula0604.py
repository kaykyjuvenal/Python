from random import randint
nmr = -1
contador = 0
while nmr !=50:
    nmr = randint(0,100)
    print(nmr)
    if nmr % 2 == 0:
        contador = contador + 1
        print('quantidade de pares ' + str (contador))









