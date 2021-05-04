from time import sleep
from random import randint
print('\033[1;34;47m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('\033[1;34;47m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
user = int(input('Em qual número estou pensando? '))
print('Processando...')
sleep(1)
lista = randint(0, 5)
if user == lista:
    print('Parabéns você acertou!!!')
else:
    print('Lamento, eu pensei no número {}, tente outra vez.'.format(lista))