from random import randint
pc = randint(1,10)
cont = 0
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
while True:
    jogador = str(input('Par ou ímpar?')).lower()
    if jogador != 'par' and jogador != 'impar':
        print('Opção inválidade, tente novamente')
        jogador = str(input('Par ou ímpar?'))
    if jogador == 'par':
        número = int(input('Escolha o seu número:'))
        print('-='*14)
        print(f'Eu escolhi {pc} e você escolheu {número}')
        soma = pc + número
        print(f'Total {soma}')
        if soma % 2 == 0:
            print(f'{soma} é um número par')
            print('Você ganhou jogador')
            cont += 1
        else:
            print('Você perdeu jogador')
            break
    if jogador == 'impar':
        número = int(input('Escolha o seu número:'))
        print(f'Eu escolhi {pc} e você escolheu {número}')
        soma = pc + número
        print(f'Total {soma}')
        if soma % 2 == 0:
            print('Você perdeu jogador')
            break
        else:
            print('Você ganhou jogador')
            cont+= 1
if cont == 1:
    print('Você só ganhou de mim uma vez jogador')
elif cont == 0:
    print('Você não ganhou nenhuma de mim')
else:
    print(f'Você ganhou de mim {cont} vezes')