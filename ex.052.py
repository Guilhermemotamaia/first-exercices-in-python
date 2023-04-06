n = int(input('Digite um número:'))
tot = 0
for c in range (1, n +1):
    if n % c == 0:
        print('\033[1:33m', end= '')
        tot += 1
    else:
        print('\033[m', end='')
    print(c, end= ' ')
print('\33[m\nO número {} foi dividido {} vezes'.format(n, tot))
if tot == 2:
    print(' Por isso ele e um número primo')
else:
    print('Por isso ele nao é primo!')