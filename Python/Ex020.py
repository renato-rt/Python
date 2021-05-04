from random import shuffle
n1 = str(input('\033[1;20;44mDigite o nome do primeiro aluno: '))
n2 = str(input('\033[mDigite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: {}.'.format(lista))