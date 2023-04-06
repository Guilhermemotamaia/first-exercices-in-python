from time import sleep
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual a sua opção?'))
    if opção == 1:
        print('A soma entre {} e {} e igual a {}'.format(n1, n2, n1 + n2))
    elif opção == 2:
       print('A multiplicação entre {} e {} e {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior valor é {}.'.format(n1, n2, maior))
    elif opção == 4:
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opção ==5:
        print('Finalziando...')
    else:
        print('Opção inválida, tente novamente.')
    print('-='*12)
    sleep(2)
print('Fim do programa.')
