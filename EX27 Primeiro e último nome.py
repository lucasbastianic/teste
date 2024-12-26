#Primeiro e último nome

nome = str(input('Qual seu nome?'))
divisao = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}.'.format(divisao[0], divisao[-1]))