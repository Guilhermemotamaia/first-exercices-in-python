# EX 46
#from time import sleep
#for c in range(10, 0, -1):
   # print(c)
    #sleep(1)
#print('\033[1:33mFOGOOOOOOOOOO\033[m!!!')]
# EX 47
#for c in range(2,51, 2):
    #print(c, end= ' ')
# EX 48
#tot = 0
#cont = 0
#for c in range(1, 501, 2):
  #  if c % 3 == 0:
     #   tot += c
     #   cont += 1
#print(tot, cont)
#tabuada = int(input('Qual número você quer aprender?'))
#for c in range(1, 11):
    #print('{} x {} = {}'.format(tabuada, c, tabuada * c))
#   EX 50
#cont = 0
#tot = 0
#for c in range(1,7):
  #  n = int(input('Digite o {}º número:'.format(c)))
   # if n % 2 == 0:
       # cont += 1
      #  tot += n
#print('Você informou {} números pares totalizando {}'.format(cont, tot))
# EX 51
#print('-='*20)
#print('\033[1:33m10 TERMOS DE UMA PA\033[m')
#print('-='*20)
#fist = int(input('Primeiro termo:'))
#razao = int(input('Razão:'))
#decimo = fist + (10 - 1) * razao
#for c in range(fist, decimo + razao, razao):
    #print(c, end= ' ')
#   EX 52
#n = int(input('Digite um número:'))
#tot = 0
#for c in range(1, n + 1):
 #   print(c, end= '-> ')
  #  if n % c == 0:
    #    print('\033[1:33m,', end= ' ')
     #   tot += 1
  #  else:
     #   print('\033[m', end= '')
#print('\033[m\nO númeroe {} ele foi dividido {} vezes.'.format(n, tot))
#if tot == 2:
   # print('Por isso ele é um número primo!')
#else:
  #  print('Por isso ele não é um \033[1:31mnúmero primo\033[m')
nome = str(input('Digite um frase:')).strip()
name = nome.split()
junto = ''.join(name)
inverso = junto[::-1]
if inverso == junto:
    print(junto, inverso)
    print('E um polimedro')
else:
    print(junto, inverso)
    print('Não é um polimedro')
