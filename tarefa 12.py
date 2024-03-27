# exercicio do triangulo- 12
#numeros inteiros, verificando se ele seria tres valores possiveis , definir se eles ser]ao equiáteros, isósceles ou
#escaleno
A = int (input('digite o lado A: '))
B = int (input('digite o lado B: '))
C = int (input('digite o lado C: '))

#int - numeros inteiros
#float- Numeros decimais
#string - texto
#sempre secelecionar a variavel
if (A < B + C) and (B < A + C) and (C < A + B) :
    print ('É possivel formar triangulo!')
    #verificar se é equilatero
    if A == B and B == C:
        print ('É um triangulo equilatero')
    elif ( A == B or B == C  ):
        print ('É um triangulo Isósceles')
    else:
        print ('É um triangulo escaleno')
else:
    print ('não é possivel formar um triangulo!')
    #sempre dois pontos no final3
