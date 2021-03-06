d = int(input('Quantos dias o carro foi alugado?'))
km = int(input('Quantos km foram rodados no carro?'))
print('O total a pagar é R${:.2f}'.format((d*60)+(km*0.15)))