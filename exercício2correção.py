kj = 20
while kj != 0:
    tabuada = int(input('digite o numero desejado para a tabuada'))
    print('Tabuada do' + str(tabuada))
    for i in range(0, 11):
        result = tabuada * i
        print(str(i) + 'x' + str(tabuada) + '=' + str(result))
    kj = int(input('desejar ver outra tabuada? 0 - nao ou 1 - sim'))






