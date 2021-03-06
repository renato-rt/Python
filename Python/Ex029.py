v = int(input('Digite a velocidade do carro: '))
lim = 80
m = 7
km = (v-lim)
if v > lim:
    print('Você será multado em R${:.2f}.'.format(km*m))
else:
    print('Parabéns você dirige com atenção!')