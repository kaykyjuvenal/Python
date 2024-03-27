#exercicio 5
from random import randint
idade = 0
contadorquantidade = 0
lista50p = []
jovens120 = 0
idosos60 = 0
contadorpessoas10 = 0
idosos7079 = 0
idosos6069 = 0
idosos80mais = 0
idade049 = 0
idosos5059 = 0

while contadorquantidade != 50:
    contadorquantidade += 1
    idade = randint(0, 100)
    lista50p.append(idade)
    if contadorquantidade == 50:
        break
for i in range(len(lista50p)):
    if 1 < lista50p[i] < 20:
        jovens120 += 1
    elif lista50p[i] > 60:
        idosos60 += 1
    if lista50p[i] < 10:
        contadorpessoas10 += 1
    elif 0 < lista50p[i] < 49:
        idade049 += 1
    elif 50 < lista50p[i] < 59:
        idosos5059 += 1
    elif 60 < lista50p[i] < 69:
        idosos6069 += 1
    elif 70 < lista50p[i] < 79:
        idosos7079 += 1
    elif lista50p[i] > 80:
        idosos80mais += 1
percentual = idosos60 / contadorquantidade * 100
percentualjovem = contadorpessoas10 / contadorquantidade * 100
calculoporcentagem = (idade049 * 0 + idosos5059 * 1.3 + idosos6069 * 3.6 + idosos7079 * 8 + idosos80mais * 14.8) / contadorquantidade
print(lista50p)
print('População de jovens será de: ' + str(jovens120) + ' Pessoas')
print('Quantidade de elementos da lista: ' + str(len(lista50p)) + ' Elementos')
print('O percentual de idosos acima de 60 anos: ' + str(round(percentual)) + '%')
print('O percentual de pessoas com menos de 10 anos que não tem risco de morte: ' + str(round(percentualjovem)) + '%')
print('A porcentagem será de: ' + str(idade049) + (' Pessoas com 1% de mortalidade,') + str(idosos5059) + (' Com uma porcentagem de 1,3% de mortalidade,') + str(idosos6069) + (' Com uma porcentagem de 3,6% de mortalidade,') + str(idosos7079) + (' Com uma porcentagem de 8% de mortalidade, ') + str(idosos80mais) + (' Com uma porcentagem de 14,8% de mortalidade.'))
print('A soma das porcentagens sera de: ' + str(round(calculoporcentagem, 2)) + '%')


