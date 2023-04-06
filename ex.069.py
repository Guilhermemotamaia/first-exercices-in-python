maioridade = conthomem = contmu20 = 0
while True:
    sexo = str(input('Sexo [M/F]:')).lower()
    while sexo != 'm' and sexo != 'f':
        sexo = str(input('Sexo [M/F]:')).lower()
    idade = int(input('idade:'))
    if sexo == 'm':
        conthomem += 1
        conthomem += 1
    if idade >= 18:
        maioridade += 1
    if sexo == 'f':
        if idade < 20:
            contmu20 += 1

    print('-'*15)
    c = str(input('Quer continuar? [S/N]:'))
    while c != 's' and c != 'n':
        c = str(input('Quer continuar? [S/N]:'))
    if c == 'n':
        break
    print('-' * 15)
print('FIm do programa')
print(f'Quantidade de pessoas maior de idade: {maioridade}')
print(f'Quantidade de homens cadastrados: {conthomem}')
print(f'Quantidade de mulheres com menos de 20 anos: {contmu20}')
