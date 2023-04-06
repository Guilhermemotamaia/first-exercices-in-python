print('\033[1:34mLoja do Baratão\033[m')
while True:
    nome = str(input('Nome do produto?'))
    preço = int(input('Valor do produto:'))
    res = ''
    while res != 's' and res != 'n':
        res = str(input('Quer continuar?')).strip().lower()[0]

    if res =='n':
        break
