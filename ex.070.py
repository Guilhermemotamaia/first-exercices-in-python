totgasto = tot1000 = 0
menor = cont = 0
barato = ''
print('\033[1:34mLoja do Baratão\033[m')
while True:
    nome = str(input('Nome do produto?'))
    preço = float(input('Valor do produto:'))
    cont += 1
    totgasto += preço
    if preço > 1000:
        tot1000 +=1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    res = ''
    while res != 's' and res != 'n':
        res = str(input('Quer continuar?')).strip().lower()[0]
    if res == 'n':
        break
print(f'Gasto total R${totgasto:.2f}')
print(f'Quantidade de produtos acima de R$1000: {tot1000}')
print(f'O produto mais barato foi a {nome} que custa R${menor:.2f} ')