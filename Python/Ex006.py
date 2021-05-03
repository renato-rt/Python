n = int(input('\033[2;33;4mDigite um número: '))
print('''O dobro de {} é {}
O triplo de {} é {}
A raiz quadrada de {} é {:.0f}'''.format(n, (n*2), n, (n*3), n, (n**(1/2))))