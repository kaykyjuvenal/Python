opcao = -1
listanome = []
listaprova = []
listatrabalho = []
listafrequencia = []
listamedia = []
listamediamaior8 = []
media = 0
frequencia = 0
nome = 0

while opcao != 0:
    print('Menu')
    print('0 - sair')
    print('1 - Cadastrar')
    print('2 - Listar aluno')
    print('3 - Calulo da media')
    print('4 - Dado o nome do aluno, dar a media final')
    print('5 - criar uma lista com o nome de todos os alunos que tiveram média maior que 8')
    print('6 - Status Final')

    opcao = int(input('Digite a opcao'))
    if opcao == 1:
        nome = input('Qual é seu nome? ')
        prova = float(input('Qual é a sua nota da prova'))
        trabalho = float(input('Qual a nota do trabalho'))
        frequencia = int(input('Qual a sua frequencia? '))
        listafrequencia.append(frequencia)
        listaprova.append(prova)
        listanome.append(nome)
        listatrabalho.append(trabalho)
        media = 0.7 * prova + 0.3 * trabalho
        listamedia.append(media)
    elif opcao == 2:
        for i in range(len(listafrequencia)):
            print('Aluno #' + str(i + 1))
            print('nome: ' + listanome[i])
            print('nota prova: ' + str(listaprova[i]))
            print('nota trabalho ' + str(listatrabalho[i]))
            print('frequencia: ' + str(listafrequencia[i]))
    elif opcao == 3:
        for i in range(len(listafrequencia)):
            print('Aluno #'+str(i+1))
            print('nome: ' + listanome[i])
            print('nota prova: ' + str(listaprova[i]))
            print('nota trabalho ' + str(listatrabalho[i]))
            print('media: ' + str(listamedia[i]))
    elif opcao == 4:
        existe = True
        nome = input('Digite o nome do aluno: ')
        for i in range(len(listanome)):
            if nome == listanome[i]:
                print('Media: ' + str(listamedia[i]))

        if existe == False:
            print('Aluno não cadastrado')
    elif opcao == 5:
        for i in range(len(listamedia)):
            if listamedia[i] > 8:
                listamediamaior8.append(listanome[i])
    elif opcao == 6:
        for i in range(len(listamedia)):
            if listamedia[i] >= 6 and listafrequencia[i] >= 75:
                print(str(listanome[i] + ' Voce foi Aprovado!'))
            elif 6 > listamedia[i] >= 4 and listafrequencia[i] >= 75:
                print(str(listanome[i] + ' Você esta qualificado para fazer a IFA !'))
            elif listamedia[i] < 4 or listafrequencia[i] < 75:
                print(str(listanome[i]) + ' Você foi reprovado!')

