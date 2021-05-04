sal = int(input('\033[1;23;32mDigite o valor do salário: '))
if sal <= 1250:
    aum = (sal*15/100)+sal
else:
    aum = (sal*10/100)+sal
print('O novo valor do salário será R${:.2f}'.format(aum))