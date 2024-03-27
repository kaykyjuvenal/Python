print("Fatoriais")
kj = 1
while kj != 2:
    entradadonumero = int(input("qual o numero que deja ser calculadora"))
    numero = 1
    final = 1

    while entradadonumero >= numero:
        final = final * numero
        numero = numero + 1

    print("Fatorial de " + str(entradadonumero) + " será " + str(final))
    kj = int(input('desejar ver outra Fatoração? 1 - nao ou 1 - sim'))








