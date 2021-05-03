p = float(input('\033[2;43;2mQual o preço do produto? \033[m'))
print('O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f}'.format(p, p-(p*5/100)))