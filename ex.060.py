from time import  sleep
n = int(input('Digite um número para calcular o seu fatorial:'))
c = n
f = 1
print('Calculando fatorial de {}! ...'.format(n))
sleep(1)
while c > 0:
    print('{}'.format(c), end= ' ')
    print('x' if c > 1 else ' = ', end= ' ')
    f *= c
    c -= 1
print('{}'.format(f))