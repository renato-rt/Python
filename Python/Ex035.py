print('\033[1;2;0m-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('\033[30mDigite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento:  '))
r3 = float(input('Digite o terceiro segmento: \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo: ')