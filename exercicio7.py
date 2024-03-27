listaopcao1 = []
listaopcao2 = []
listauniao = []
listainterseccao = []
opcao = -1
listamult = []

print('Menu')
print('0 - Sair')
print('1 - Carregar dados da lista 1')
print("2 - Carregar primeiro dado da lista 2")
print('3 - Exibir Listas ')
print('4 - Lista União ')
print('5 - Lista intersecção')
print('6 - Maior valor das duas listas e somar com os elementos da primeira')
print('7 - Multiplique os termos')
print('8 - Apagar tudo')

while opcao != 0:
    opcao = int(input('Digite um nome'))
    if opcao == 1:
        if len(listaopcao1) < 5:
            numero = int(input('Qual o numero: '))
            listaopcao1.append(numero)
        else:
            print('5 Numeros já foram cadastrados')
    elif opcao == 2:
        numero = int(input('Digite o primeiro numero da lista 2: '))
        listaopcao2.append(numero)
        for i in range(4):
            novonumero = listaopcao2[i] * 2
            listaopcao2.append(novonumero)
    elif opcao == 3:
        print('Conteudo da lista: ' + str(listaopcao1))
    elif opcao == 4:
        print('Lista União')
        for i in range(len(listaopcao1)):
            existe = False
            for k in range(len(listauniao)):
                if listauniao[k] == listaopcao1[i]:
                    existe = True
            if existe == False:
                listauniao.append(listaopcao1[i])
        for i in range(len(listaopcao2)):
            listauniao.append(listaopcao2[i])
            existe = False
            for k in range(len(listauniao)):
                if listauniao[k] == listaopcao2[i]:
                    existe = True
    elif opcao == 5:
        print('Lista intersecção')
        for i in range(len(listaopcao1)):
            for k in range(len(listaopcao2)):
                if listaopcao1[i] == listaopcao2[k]:
                    existe = False
                    for j in range(len(listainterseccao)):
                        if listaopcao1[i] == listainterseccao[j]:
                            existe = True
                    if existe == False:
                            listainterseccao.append(listaopcao1[i])
    elif opcao == 6:
        print('Maior Valor')
        maior = -1
        for i in range(len(listaopcao1)):
            if listaopcao1[i] > maior:
                maior = listaopcao1[i]
        for j in range(len(listaopcao2)):
            if listaopcao2[j] > maior:
                maior = listaopcao2[j]
        print('O maior valor é ' + str(maior))
        for k in range (len(listaopcao1)):
            listaopcao1[k] + maior
    elif opcao == 7:
        if len(listaopcao1) == len(listaopcao2):
            for i in range(len(listaopcao2)):
                listamult.append(listaopcao1[i] * listaopcao2[i])
        else:
            print('Nao é possível fazer a multiplicacao')
        print(listamult)
    elif opcao == 8:
        listaopcao1 = []
        listaopcao2 = []
        listainterseccao = []
        listauniao = []





