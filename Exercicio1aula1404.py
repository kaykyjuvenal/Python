
contadorluxo = 1
quantidadedeprodutos = 0
preco = 1
nomedoproduto = 0
precodoproduto = 0
categoria = ' '
cont = 0
quantidadeluxo = 0
somaluxo = 0
precomaiscaro = 0
nomemaiscaro = 0
contadormaiscaro = 0
contadorpreco = 0
nomemaisbarato = 0
precomaisbarato = 0
while preco != 0:
    nomedoproduto = input('Qual o nome do produto ?')
    precodoproduto = int(input('qual o preço do produto ? '))
    cont = cont + 1
    quantidadedeprodutos = int(input('qual a quantidade de produtos ?'))
    categoria = input('qual a categoria de produto ')
    if categoria == 'L' or categoria == 'l' and preco < 2000:
        contadorluxo = contadorluxo + 1


    if categoria == 'L' or 'l':
        quantidadeluxo = quantidadeluxo + 1
        somaluxo = somaluxo + preco

    if quantidadedeprodutos < 50 and preco > precomaiscaro:
        precomaiscaro = preco
        nomemaiscaro = nomedoproduto
        contadormaiscaro = contadormaiscaro + 1
    if preco > 100 and preco < 200:
        contadorpreco = contadorpreco + 1
    if categoria == 'C'or 'c' and precomaisbarato > preco:
        precomaisbarato = preco
        nomemaisbarato = nomedoproduto

print('a quantidade de produtos de luxo será ' + str(contadorluxo))
if quantidadeluxo >0:
    media = somaluxo/quantidadeluxo
    print('A media de preços de luxo será: ' + str(media))
    print('Produto mais caro com qtdd < 50: ' + nomemaiscaro)
    percentual = (contadorpreco / cont) * 100
    print('Percentual de prod com preco entre 100 e 200 = ' + str(percentual))
    print('produto comum mais barato :' + nomemaiscaro)


