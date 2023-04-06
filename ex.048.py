s = 0
for j in range(1, 501, 2):
    print(j)
    if j % 3 == 0:
        s = s + j
print('O soma de todos esses números multiplos de 3 é {}'.format(s))