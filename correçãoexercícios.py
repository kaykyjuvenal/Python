contpares = 0
numero = -1
soma = 0
while numero !=0:
    numero = int(input('digite um numero: '))
    if numero%2 == 0:
        soma = soma + numero #acumulação de valores ou como contador
        contpares = contpares + 1
print('Calculo: ')
media = soma / contpares
print('a media é : ' + str(media))








