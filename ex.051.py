print('-='*20)
print('     OS 10 TERMOS DE UMA PA')
print('-='*20)
primeiro = int(input('Primeiro termo:'))
ra = int(input('Razão:'))
d = primeiro + (10 - 1)  * ra
for c in range(primeiro, d, ra):
    print(c, end= '-')