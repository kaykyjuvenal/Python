quantidadedecarros = int(input('Digite a quantidade de carros vendidos '))

comissao = 0
contador = 0
modelomaiscaro = 0
precomaiscaro = 0
somavalorcarros= 0

for i in range(quantidadedecarros):
    print('Dados do carro # ' ) + (i + 1)
    modelo = input('digite o modelo do carro: ')
    preco = float(input('digite o preço do carro'))
    #calculo da comissão
    if preco <= 10000:
        comissão = comissão + preco * 0.10
    else:
        comissão = comissão + preco * 0.11

    #calculo do mais caro
    if preco > precomaiscaro:
        precomaiscaro = preco
        modelomaiscaro = modelo
    # A quantidade de carros que custam mais que R$20.000,00 e menos que R$30.000,00
    if 20000 > preco < 30000:
        print("quantidade de carros nessa faixa : " + str(contador))
        contador = contador + 1

    #Preço medio
    somavalorcarros = somavalorcarros + preco
    media = somavalorcarros/quantidadedecarros
    print('A comissão total é de : ' + str(comissão))
    print(' a media da soma sera : ' + str (media))




