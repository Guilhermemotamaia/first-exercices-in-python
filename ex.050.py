soma = 0
cont = 0
for c in range(6):
    x = int(input('digite um número:'))
    if x % 2 == 0:
        soma += x
        cont += 1
print('Você informou {} e a soma foi {}'.format(cont, soma))

