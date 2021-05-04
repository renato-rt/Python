n = str(input('\033[1;31;44mDigite seu nome completo: ')).strip().upper()
nome = n.split()
print('\033[mSeu primeiro nome é: {}.'.format(nome[0]))
print('Seu último nome é: {}.'.format(nome[len(nome)-1]))