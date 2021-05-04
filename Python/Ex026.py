frase = str(input('\033[1;30;40mDigite uma frase: ')).strip().lower()
print('\033[mA letra A aparece {} vezes.'.format(frase.count('a')))
print('Em que posição aparece a primeira vez a letra a: {}'.format(frase.find('a')+1))
print('Em que posição aparece a última vez a letra a: {}'.format(frase.rfind('a')+1))