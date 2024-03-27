#Rendimentos do taxi
kj = 1
while kj != 2:
    medidorinicio = int(input("qual a medida inicial do odometro"))
    medidorfim = int(input('qual a medição final do odometro'))
    litros = int(input("qual a quantidade de combustivel gasto no dia todo"))
    total = int(input('qual o valor final recebido pelas corridas'))
    varkm = medidorfim - medidorinicio
    eficiencia = round(varkm/litros)
    valorkm = 2.5/eficiencia
    lucrototal = round(total - (varkm * valorkm))
    mensagemfinal = ('o lucro diario foi ' + str(lucrototal) + ' carro fez ' + str(eficiencia) + "km/l")
    if lucrototal <= 100.00:
        print(mensagemfinal + "o lucro foi inferior a mate de R$ 100.00, o desempenho deve ser melhorado")
    else:
        print(mensagemfinal)
    kj = int(input("reiniciar o programa ? 1 - não e 2 - não"))

