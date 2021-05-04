d = int(input('\033[1;21;3mQuantos dias o carro foi alugado? \033[m'))
km = int(input('Quantos km foram rodados no carro?'))
print('O total a pagar é R${:.2f}'.format((d*60)+(km*0.15)))