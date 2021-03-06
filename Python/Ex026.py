frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes.'.format(frase.count('a')))
print('Em que posição aparece a primeira vez a letra a: {}'.format(frase.find('a')+1))
print('Em que posição aparece a última vez a letra a: {}'.format(frase.rfind('a')+1))