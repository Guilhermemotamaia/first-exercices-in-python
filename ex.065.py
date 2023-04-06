cont = soma = maior = menor = 0
res = 'Ss'
while res in 'Ss':
    num = int(input('Digite um número:'))
    res = str(input('Quer continuar?[S/N]')).strip()
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            num = menor
    media = soma / cont
print('\033[1:33mQuantidade de número: {}\033[m'.format(cont))
print('\033[1:34mSoma dos número: {}\033[m'.format(soma))
print('\033[1:32mMédia da soma dos números: {}\033[m'.format(media))
print('\033[1:31mMaior número: {}'.format(maior))
print('\033[1:31mMenor número: {}'.format(menor))
