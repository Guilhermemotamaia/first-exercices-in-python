num = cont = soma = 0
num = int(input('Digite um número [999 para parar]:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]:'))
print('Acabou')
print('Você digitou {} números e a soma foi {}'.format(cont, soma))