c = int(input('\033[1;20;30mInforme a temperatura em °C: \033[m'))
print('A temperatura {:.1f}°C representa {:.1f}?F'.format(c, 32+(c*9/5)))