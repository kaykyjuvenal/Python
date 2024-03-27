#Arquivos
def existencia(item, lista, coluna):
    for i in range(len(lista)):
        if item == lista[i][coluna]:
            return True
        else:
            return False

def abrir_arquivo(nomearq, matriz):
    arquivo = open(nomearq, 'r', encoding='utf8')
    for linha in arquivo:
        linha = linha.replace('\n', '')
        dados = linha.split(',') and linha.split(';')
        matriz.append(dados)
    return matriz

def busqueporclube(club,matriz):
    listaporclube = []
    for i in range(len(matriz)):
        if club == matriz[i][10]:
            listaporclube.append(matriz[i])
    return listaporclube

def busqueporpais(pais, matriz):
    listaporpais = []
    for i in range(len(matriz)):
        if pais == matriz[i][19]:
            listaporpais.append(matriz[i])
    return listaporpais

def exibirdados(matriz):
    for i in range(1, len(matriz)):
        print(matriz[i])

def valormaior(coluna):
    lista = []
    valormax = 0
    ivalormax = 0
    for i in range(len(lista)):
        if lista[i][coluna] >= valormax:
            valormax = lista[i]
            ivalormax = i
def menortempodeclube(matriz):
    anoteste = 0
    mesteste = 0
    diateste = 0
    nomemaior = ''
    lista = []
    for i in range(len(matriz)):
        if i != 0 and matriz[i][16] != '':
            ano = int(matriz[i][16][0:4])
            mes = int(matriz[i][16][6:7])
            dia = int(matriz[i][16][8:10])
            if anoteste < ano:
                anoteste = ano
                if mesteste < mes:
                    mesteste = mes
                    if diateste < dia:
                        diateste = dia
                        nomemaior = fifa[i][0]
                        lista.append(anoteste)
                        lista.append(mesteste)
                        lista.append(diateste)
                        lista.append(nomemaior)
                        return lista
def maiortempodeclube(matriz):
    anoteste = 2022
    mesteste = 12
    diateste = 31
    lista = []
    nomemenor = []
    nome = []
    for i in range(len(matriz)):
        if i != 0 and matriz[i][16] != '':
            ano = int(matriz[i][16][0:4])
            mes = int(matriz[i][16][6:7])
            dia = int(matriz[i][16][8:10])
            if anoteste > ano:
                anoteste = ano
                if mesteste > mes:
                    mesteste = mes
                    if diateste > dia:
                        diateste = dia
                nomemenornovo = Fifa22[i][0]
                nomemenor.append(nomemenornovo)
                nome = nomemenor[5:9]
    lista.append(anoteste)
    lista.append(mesteste)
    lista.append(diateste)
    lista.append(nome)
    return lista
def dadosespecificos(lista):
    for i in range(len(lista)):
        if lista[i][16][0:4] != 0 and lista[i][16] != '':
            listanova = []
            ano = float(lista[i][16][0:4])
            mes = int(lista[i][16][6:7])
            dia = int(lista[i][16][8:10])
            valoremmilhao = int(lista[i][4]) / 1000000
            listanova.append(lista[i][0])
            listanova.append(str(valoremmilhao) + ' Milhões')
            listanova.append(lista[i][6])
            tempodeblubeemanos = float(2022 - ano)
            listanova.append(tempodeblubeemanos)
            listadefinitiva.append(listanova)
    return listadefinitiva
def listagemclube(matriz):
    for i in range(len(matriz)):
        if matriz[i][16][0:4] != 0 and matriz[i][16] != '':
            lista = []
            listanova = []
            ano = float(lista[i][16][0:4])
            mes = int(lista[i][16][6:7])
            dia = int(lista[i][16][8:10])
            listanova.append(lista[i][0])
            listanova.append(lista[i][4])
            listanova.append(lista[i][6])
            tempodeblubeemanos = float(2022 - ano)
            listanova.append(tempodeblubeemanos)
            listadefinitiva.append(listanova)
def buscaporliga(liga,matriz):
    listaporliga = []
    for i in range(len(matriz)):
        if liga == matriz[i][11]:
            listaporliga.append(matriz[i])
    return listaporliga
def chamarmenu():
    print('Menu Fifa')
    print('0 - Sair')
    print('1 - Carregar os Dados.')
    print('2 - Listagem por Clube.')
    print('3 - Listagem total.')
    print('4 - Qual o valor de cada time em atletas ?')
    print('5 - Qual time possui o maior numero de brasileiros ?')
    print('6 - Qual é a contratação mais recente ?')
    print('7 - Qual o ano que teve mais contratações? ')
    print('8 - Classificação dos jogadores pela idade ?')
    print('9 - Quais os tres jogadores que estão a mais tempo em seus clube?')
    print('10 - Digite um nome para dados detalhados.')
    print('11 - Qual o país que tem mais jogadores na categoria "Fim de carreira" ?')
    print('12 - Média dos atletas de acordo com a liga.')
    print('13 - Digite o clube e descubra qual o melhor jogador dele. ')


fifa = 'KaykyFlávioJuvenalFifa22.csv'
Fifa22 = []
opcao = -1
listaporclube = []
muitojovem = []
jovem = []
adulto = []
fimdacarreira = []

chamarmenu()
while opcao != 0:
    opcao = int(input('Qual a sua opção?'))
    if opcao == 1:
        fifa = abrir_arquivo(fifa,Fifa22)
        print('Os dados foram carregados')
    if len(Fifa22) != 0:
        if opcao == 2:
            #A listagem sera feita por clubes para evitar erros
            clube = input('Selecione um clube para facilitar a busca: ')
            listaporclube = busqueporclube(clube,Fifa22)
            exibirdados(listaporclube)
        if opcao == 3:
            exibirdados(Fifa22)
        if opcao == 4:
            valorfinal = 0
            lista = []
            soma = 0
            clube = input('Qual o clube a ser calculado?')
            clubesoma = busqueporclube(clube, Fifa22)
            for i in range(len(clubesoma)):
                soma = soma + int(clubesoma[i][4])
            valorfinal = str(soma / 1000000) + ' Milhões de euros'
            print(valorfinal)
        if opcao == 5:
            dicFifa = {}
            valormax = 1
            ivalormax = 0
            valor = []
            for i in range(len(Fifa22)):
                if i != 0 and i != "":
                    if Fifa22[i][10] not in dicFifa:
                        dicFifa[Fifa22[i][10]] = 1
                    if Fifa22[i][19] == 'Brazil':
                        dicFifa[Fifa22[i][10]] += 1
            lista = list(dicFifa.values())
            for j in range(len(lista)):
                if lista[j] > valormax:
                    valormax = lista[j]
                    ivalormax = j
            valor = list(dicFifa.keys())[ivalormax]
            print('O clube com o maior numero de brasileiros é: ' + str(valor))
            #Todos os times brasileiros são não licensiados , então todos tem 20 jogadores brasileiros com nomes aleatorios
        elif opcao == 6:
            valor = 0
            valormes = 0
            for i in range(len(Fifa22)):
                dicAnos = {}
                valormax = 1
                ivalormax = 0
                lista = list(dicAnos.values())
                if (Fifa22[i][16][0:4]) not in dicAnos:
                    dicAnos[(Fifa22[i][16][0:4])] = 1
                if (Fifa22[i][16][0:4]) in dicAnos:
                    dicAnos[(Fifa22[i][16][0:4])] += 1
                    valor = list(dicAnos.keys())[ivalormax]
            print('O ano com o maior numero de contratações é: ' + str(valor))

        elif opcao == 7:
            for i in range(len(Fifa22)):
                if i != 0:
                    if int(Fifa22[i][6]) < 22:
                        muitojovem.append(Fifa22[i])
                    if 22 > int(Fifa22[i][6]) < 26:
                        jovem.append(Fifa22[i])
                    if 26 > int(Fifa22[i][6]) < 30:
                        adulto.append(Fifa22[i])
                    if int(Fifa22[i][6]) > 30:
                        fimdacarreira.append(Fifa22[i])

            print('Separação feita com sucesso')
        elif opcao == 8:
            lista = menortempodeclube(Fifa22)
            print(str(lista[0]) + '/' + str(lista[1]) + '/' + str(lista[2]) + ' E o nome do mais recente é: ' + str(lista[3]))
        elif opcao == 9:
            lista = maiortempodeclube(Fifa22)
            print(str(lista[0]) + '/' + str(lista[1]) + '/' + str(lista[2]) + ' E o nome dos com mais tempo nos clubes é: ' + str(lista[3]))
            #nos primeiros termos está adicionando jogadores que mudaram de clube e jogadores que ja jogaram por outros clubes
        elif opcao == 10:
            listadefinitiva = []
            clube = input('Digite o clube a ser procurado')
            lista = busqueporclube(clube, Fifa22)
            listafinal = dadosespecificos(lista)
            exibirdados(listafinal)
        elif opcao == 11:
            paiscommaisnumeros = ''
            paisteste = 0
            listapaises = []
            for i in range(len(fimdacarreira)):
                valor = 0
                if len(fimdacarreira[i][19]) != 0 and fimdacarreira[i][19] != '':
                    if len(fimdacarreira[i][19]) > paisteste:
                        paisteste = len(fimdacarreira[i][19])
                        paiscommaisnumeros = fimdacarreira[i][19]
                        listapaises.append(paisteste)
                        listapaises.append(paiscommaisnumeros)
            print('O país com mais jogadores em fim de carreria é a: ' + str(paiscommaisnumeros))
        elif opcao ==12:
            contadordepessoas = 0
            soma = 0
            media = 0
            liga = input('Qual liga você quer fazer a media ?')
            lista = buscaporliga(liga,Fifa22)
            for i in range(len(lista)):
                    contadordepessoas += 1
                    soma += int(lista[i][6])
            if contadordepessoas != 0:
                media = soma / contadordepessoas
                print('A medía da liga será de: ' + str(round(media)))
            else:
                print('Calculo impossível')

        elif opcao == 13:
            lista = []
            nomemaior = ''
            overallmaior = 0
            clube = input('Qual o clube? ')
            for i in range(len(Fifa22)):
                lista = busqueporclube(clube,Fifa22)
                for j in range(len(lista)):
                    if int(lista[j][3]) > int(overallmaior):
                        nomemaior = lista[j][1]
                        overallmaior = lista[j][3]
                print('O nome do jogador com maior overall do time é: ' + str(nomemaior) + ' E o overall dele será: ' + str(overallmaior))
                break
    else:
        print('Opção 1 não executada')













