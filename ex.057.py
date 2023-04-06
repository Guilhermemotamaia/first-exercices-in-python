sexo = str(input('Informe o seu sexo [M/F]:')).lower().strip()[0]
while sexo not in 'mf':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo:')).strip().lower()[0]
print('sexo {} registrado com sucesso'.format(sexo))