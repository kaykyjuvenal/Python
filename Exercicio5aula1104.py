print("Fibonacci até o valor 500")
termo = 0
parar = 500
a = 1
b = 1
print(a)
print(b)
while termo <= (parar - termo):
    termo = a + b
    b = a
    a = termo
    print(termo)
