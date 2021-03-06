n = float(input('Quanto em dinheiro você tem na sua carteira? '))
dolar = (n/3.27)
print('Com R${} você pode comprar US${:.2f}'.format(n, dolar))