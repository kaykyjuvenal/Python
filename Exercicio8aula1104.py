print("Idades ")
n = int(input('qual a quantidade de pessoas que vão pertencer ao grupo ? '))
numerodepessoas = 1
soma = 0
while numerodepessoas <= n :
    idade = int(input('qual a idade do ' + str(numerodepessoas) + 'º individuo '))
    numerodepessoas = numerodepessoas + 1
    soma = idade + soma
media = round(soma/n, 2)
if media <= 25:
    print('A media das idades será: ' + str(media) + 'a turma será jovem')
elif 26 <= media <= 60:
    print('A media das idades será: ' + str(media) + 'a turma será adulta')
else:
    print('A media das idades será ' + str(media) + 'a turma será idosa')




