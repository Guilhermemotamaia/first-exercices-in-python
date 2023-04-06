cont = somador = 0
print('Digite 99 para parar o programa')
while True:
    n = int(input('Digite um número:'))
    if n == 99:
        break
    cont += 1
    somador += n
print(f'Foram {cont} números')
print(f'A soma dos números e {somador}')