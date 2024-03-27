
def cadastrocliente(matriz, nome, fatura):
    lista = []
    lista.append(nome)
    lista.append(fatura)
    matriz.append(lista)
    return matriz
def cadastrardoce(matriz, doce , valor, categoria):
    lista = []
    lista.append(doce)
    lista.append(valor)
    lista.append(categoria)
    matriz.append(lista)
    return matriz
def cadastrarvendas(matriz, faturamento ,doceComprado, qDoce, clicompra):
    lista = []
    lista.append(faturamento)
    lista.append(doceComprado)
    lista.append(qDoce)
    lista.append(clicompra)
    matriz.append(lista)
    return matriz
def existencia(matriz,item,coluna):
    for i in range(len(matriz)):
        if item == matriz[i][coluna]:
            return True
        else:
            return False
    return False
def busquecategoria(categoria,matriz):
    listaporcategoria = []
    for i in range(len(matriz)):
        if categoria == matriz[i][2]:
            listaporcategoria.append(matriz[i][0])
    return listaporcategoria
def busquepornome(nome,matriz):
    listapornome = []
    for i in range(len(matriz)):
        if nome == matriz[i][3]:
            listapornome.append(matriz[i])
    return listapornome
def busquecategoriadetalhe(categoria, matriz):
    listaporclube = []
    for i in range(len(matriz)):
        if categoria == matriz[i][2]:
            listaporclube.append(matriz[i])
    return listaporclube
def exibirdados(matriz):
    for i in range(1, len(matriz)):
        print(matriz[i])
def produtomaiscaro(matriz):
    lista = []
    numeroteste = 0
    nome = ''

    for i in range(len(matriz)):
        valores = int(matriz[i][1])
        if numeroteste < valores:
            numeroteste = valores
            nome = matriz[i][0]
            print('entrei')
    lista.append(numeroteste)
    lista.append(nome)

    return lista
def carregarMenu():
    print('======Menu=======')
    print('1 - Cadastro de Doces')
    print('2 - Listar por categorias')
    print('3 - Cadatrar cliente')
    print('4 - Listar Clientes')
    print('5 - Registrar uma venda')
    print('6 - Listas todas as vendas')
    print('7 - Apagar um doce')
    print('8 - Listar produto mais caro ')
    print('9 - listar todas as vendas do cliente selecionado')
    print('10 - Pagamento de Fatura')
opcao = -5
cadDoce = []
cadCliente = []
cadVendas = []
dicValores = {}
contadorcategoria = 0
contadordevezes = 0
carregarMenu()
while opcao != 0:
    opcao = int(input("digite opção desejada: "))
    if opcao == 1:
        doce = input("Nome do doce: ")
        if existencia(cadDoce, doce, 0) is True:
            print("Nome ja cadastrado, escolha outro nome")
            opcao = 1
        else:
            valor = float(input("Valor de doce: "))
            if valor < 10:
                print("Valor muito baixo, insira um novo valor")
                opcao = 1
            else:
                cat = input("Categoria de doce: ")
                for i in range(len(cadDoce)):
                    if cat not in cadDoce[i][2]:
                        contadorcategoria = contadorcategoria + 1
                cadastrardoce(cadDoce, doce, valor,cat)
                print("doce cadastrado com sucesso!")
    elif opcao == 2:
        while contadorcategoria != contadordevezes:
            categoria = input('Qual a categoria ?')
            lista = busquecategoria(categoria, cadDoce)
            print(lista)
            contadordevezes += 1
            if contadorcategoria == contadordevezes:
                break

    elif opcao == 3:
        nome = input("digite o nome do cliente: ")
        if existencia(cadCliente, nome, 0) is True:
            print("Nome já foi cadastrado")
        else:
            cadastrocliente(cadCliente, nome, 0)
    elif opcao == 4:
        print("Os clientes são: ")
        for i in range(len(cadCliente)):
            print(cadCliente)
    elif opcao == 5:
        valortotal = 1
        clienteCompra = input("Cliente que faz a compra: ")
        if existencia(cadCliente, clienteCompra, 0) is False:
            print("Cliente não cadastrado")
        else:
            qtdComprada = int(input("Numero de itens comprados: "))
            for i in range(qtdComprada):
                doceComprado = input("doce comprado: ")
                if existencia(cadDoce, doceComprado, 0) is False:
                    print("O doce  não foi cadastrado")
                    break
                else:
                    print("Preços dos Doces")
                    for k in range(len(cadDoce)):
                        print(cadDoce[k])
                quantidade = int(input("Quantas unidades de doces foram adquiridas: "))
                for j in range(len(cadDoce)):
                    if doceComprado == cadDoce[j][0]:
                        valortotal = quantidade * cadDoce[j][1]
                    for e in range(len(cadCliente)):
                        if clienteCompra == cadCliente[e][0]:
                            cadCliente[e][1] += valortotal
                            print(valortotal)
                cadastrarvendas(cadVendas,valortotal,doceComprado,quantidade,clienteCompra)
    elif opcao == 6:
        for i in range(len(cadVendas)):
            print('Vendas Realizadas:' + str(cadVendas[i]))
    elif opcao == 7:
        nomeApagado = input('Qual o nome á ser apagado')
        if existencia(cadDoce,nomeApagado,2) is True:
            print('Ja foi cadastrado a venda do produto')
        else:
            for i in range(len(cadDoce)):
                if cadDoce[i][0] == nomeApagado:
                    cadDoce[i].pop()
                    cadDoce[i].pop()
                    cadDoce[i].pop()
        print(cadDoce)
    elif opcao == 8:
        balas = busquecategoriadetalhe('bala',cadDoce)
        lista = produtomaiscaro(balas)
        print('O nome do doce mais caro na categoria bala é: ' + str(lista[1]) + ' e o valor mais alto é: ' + str(lista[0]))
    elif opcao == 9:
        nomecliente = input('Qual o nome do cliente?')
        lista = busquepornome(nomecliente,cadVendas)
        exibirdados(lista)
    elif opcao == 10:
        fatura = 0
        for i in range(len(cadVendas)):
            if cadDoce[i][3] not in dicValores.keys():
                dicValores[cadVendas[i][3]] = cadVendas[i][1]
            else:
                dicValores[cadVendas[i][3]] += cadVendas[i][1]
        print('A fatura a ser paga é: ' + str(dicValores))
        nomeCliente = input('Qual o nome do cliente? ')
        if nomeCliente not in dicValores:
            print('Cliente sem compra ativa')
        else:
            fatura = float(input('Qual o valor que será pago?'))
            dicValores[nomeCliente] -= fatura
        print('ele pagou: ' + str(fatura) + ' Sobrando: ' + str(dicValores[nomeCliente]))

