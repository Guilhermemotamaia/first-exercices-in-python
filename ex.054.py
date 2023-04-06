from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(7):
    n = int(input('Em que ano a {}º pessoa nasceu?:'.format(c +1 )))
    idade = atual - n
    if idade >= 18:
        totmaior += 1
    else:
       totmenor += 1
print('A todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E {} pessoas menores de idade '.format(totmenor))