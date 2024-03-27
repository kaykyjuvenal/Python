print("Numero de termos ")

n = int(input('digite o valor de n :'))
numerador = 1
denominador = 1
serie = 's = 1'
soma = 0

for i in range (n):
    print(numerador)
    print(denominador)
    soma = soma + numerador/denominador
    termo = str(numerador) + '/' + str(denominador)
    print(termo)
    numerador = numerador + 1
    denominador = denominador + 2
    if (i+1) == n:
        serie = serie + termo + "+"
    else:
        serie = serie + termo + '='

print(serie + str(round(soma, 3)))











