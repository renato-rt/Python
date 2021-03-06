s = float(input('Qual é o salário do funcionário? '))
print('Um funcionário que ganhava R${:.2f} com 15% de aumento agora ganhará R${:.2f}.'.format(s, s+(s*15/100)))