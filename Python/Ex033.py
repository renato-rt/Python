n1 = int(input('\033[1;0;0mDigite o primeiro valor: '))
n2 = int(input('Digite o segundo valor:  '))
n3 = int(input('Digite o terceiro valor: '))
if n1 > n2 and n1 > n3:
    print('O maior número é {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior número é {}'.format(n2))
else:
    print('O maior número é {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor número é {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor número é {}'.format(n2))
else:
    print('O menor número é {}'.format(n3))