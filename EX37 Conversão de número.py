#Convertendo um número de acordo com o usuário 

n1 = int(input('Qual o número desejado?'))
conv = str(input('Qual conversão você deseja? 1.binário 2.octal 3.hexagonal'))

if conv == 'binário':
    print('Seu número ficou dessa forma {}.'.format(bin(n1)))
elif conv == 'octal':
    print('Seu número ficou dessa forma {}.'.format(oct(n1)))
else:
    print('Seu número ficou dessa forma {}.'.format(hex(n1)))