import math
ang = int(input('Digite o valor do ângulo: '))
print('''O ângulo de {:.1f} tem o SENO de {:.2f}
O ângulo de {:.1f} tem o COSSENO de {:.2f}
O ângulo de {:.1f} tem a TANGENTE de {:.2f}'''.format(ang, math.sin(math.radians(ang)), ang, math.cos(math.radians(ang)), ang, math.tan(math.radians(ang))))