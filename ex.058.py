print('-='*5,'Vamos jogar jogador?','-='*5)
print('Escolhi um número de 1 a 50')
print('Vamos vê em quantas tentativas você acerta?')
from random import randint
computador = randint(1, 10)
acertou = False
cont = 0
while not acertou:
    jogador = int(input('qual o seu {}º palpite:'.format(cont + 1)))
    if jogador > computador:
        print('Tento outra vez! É um número menor.')
        cont += 1
    if jogador < computador:
        print('Tente outra vez! É um número maior.')
        cont += 1
    if jogador == computador:
        acertou = True
        print('Parabés, você acertou!')
print('Foram {} tentativas'.format(cont + 1))