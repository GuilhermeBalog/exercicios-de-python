sexo = str(input('Digite o Sexo [F ou M]: ')).strip().upper()
while sexo not in 'FM':
    sexo = str(input('Dados inválidaos. Por favor, use apenas F ou M: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))
