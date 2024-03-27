from random import randint
lista = []
quantidadeelementos = 0

while quantidadeelementos < (30):
    numero = randint(1, 100)
    existe = False #Para não repitir

    for j in range(len(lista)):
        if lista[j] == numero:
            existe = True
            break
    if existe == False:
        lista.append(numero)
        quantidadeelementos = quantidadeelementos +1

print(lista)
print('O tamanho da lista será de: ' + str(len(lista)) + ' elementos')