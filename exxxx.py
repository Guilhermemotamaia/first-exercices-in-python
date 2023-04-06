somaidade = 0
médiaidade = 0
maioridade = 0
nomevelho = ''
tot = 0
for c in range(1, 5):
    print('-='*10, '{}º pessoa'.format(c),'-='*10)
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo M/F:')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mn':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
       maioridade = idade
       nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        tot += 1

mediaidade = somaidade / 4
print('A média de idade é {:.2f}'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho, maioridade))
if tot != 1:
    print('Tem {} mulheres com menos de 20 de idade'.format(tot))
else:
    print('Tem apenas 1 mulher com menos de 20 anos')
