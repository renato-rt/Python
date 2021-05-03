n = float(input('\033[3;32;23mQuanto em dinheiro você tem na sua carteira? '))
dolar = (n/3.27)
print('Com R${} você pode comprar US${:.2f}'.format(n, dolar))