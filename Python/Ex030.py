n = int(input('\033[7;37;40mDigite um número: \033[m'))
r = n % 2
if r==0 and n!=0:
    print('Esse número é par!')
elif n==0:
    print('Esse não é um número válido!')
else:
    print('Esse número é ímpar!')
