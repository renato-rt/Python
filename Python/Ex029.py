v = int(input('\033[4;33;42mDigite a velocidade do carro: \033[m'))
lim = 80
m = 7
km = (v-lim)
if v > lim:
    print('\033[1;30;41mVocê será multado em R${:.2f}.\033[m'.format(km*m))
else:
    print('Parabéns você dirige com atenção!')