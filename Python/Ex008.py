m = int(input('\033[2;1;33mUma distância em metros: '))
print('''A medida de {}m corresponde a
{}km
{}hm
{}dam
{}dm
{}cm
{}mm'''.format(m, (m/1000), (m/100),(m/10), (m*10), (m*100), (m*1000)))