def cadastrarCliente(name,age,matriz):
    lista = [name,age]
    matriz.append(lista)
def cadastrarDestino(name,value,minimumvalue,matriz):
    lista = [name,value,minimumvalue]
    matriz.append(lista)
    valor = lista.count(nome)

def cadastrarViagem(name,destine,value, matriz):
        lista = [name,destine,value]
        matriz.append(lista)
def exebirdados(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
def existir(par1, matriz, coluna):
    for i in range(len(matriz)):
        if par1 == matriz[i][coluna]:
            return True
    return False
def criarMenu():
    print('0 - Sair')
    print('1 - cadastrar')
    print('2 - Cadastrar Destino')
    print('3 - Cadastrar Viagem')
    print('4 - Listar viagens já salvas - Não está em funcionamento')
    print('5 - Listar os dados completos')
opcao = -1
clientes = []
Destino = []
Viagem = []
nomeArquivo = 'clientes.txt'
nomeArquivoReport = 'clientesvoltando.txt'
while opcao != 0:
    criarMenu()
    opcao = int(input('Qual a sua opção'))
    if opcao == 1:
        nome = input('Digite o nome: ')
        idade = int(input('Digite a idade'))
        existire = existir(nome,clientes,0)
        if existire is False:
            if idade >= 18:
                cadastrarCliente(nome, idade, clientes)
            else:
                print('Cadastro impossível')
    elif opcao == 2:
        nome = input('Digite o nome: ')
        valorDaDiaria = float(input('Qual o valor da diaria'))
        numeroMinimoViagem = int(input('Quam o numero minimo de diárias?'))
        cadastrarDestino(nome,valorDaDiaria,numeroMinimoViagem,Destino)
    elif opcao == 3:
        nome = input('Digite o nome: ')
        existire = existir(nome,clientes,0)
        if existire is True:
            destino = input('Digite o seu destino: ')
            existire = existir(destino,Destino,0)
            if existire is True:
                numeroDiarias = int(input('Numero de diarias: '))
                cadastrarViagem(nome,destino,numeroDiarias,Viagem)

            else:
                print('Destino não cadastrado')
        else:
            print('Cliente não cadastrado.')

    elif opcao == 4:
        print('não consegui')
    elif opcao == 5:
        exebirdados(clientes)
        if len(clientes) == 0:
            print('Clientes não cadastrados')
    elif opcao == 6:
        print('não consegui')


