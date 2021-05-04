km = int(input('\033[1;36;41mDigite a distância da viagem: '))
vc = 0.5
vl = 0.45
if km <= 200:
    print("O valor da sua passagem é R${:.2f}".format((km)*vc))
else:
    print('O valor da sua passagem será R${:.2f}'.format((km)*vl))