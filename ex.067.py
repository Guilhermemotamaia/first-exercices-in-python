from time import sleep
while True:
    n = int(input('Qual tabuado você quer aprender?'))
    if n == 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
        sleep(0.4)
print('Volte sempre!')