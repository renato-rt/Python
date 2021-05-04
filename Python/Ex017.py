import math
co = float(input('\033[1;25;1mDigite o valor do cateto oposto: '))
ca = float(input('\033[m4Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa é {:.2f}.'.format(math.hypot(co, ca)))