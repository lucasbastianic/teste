#Separando um número 

n1 = int(input('Qual seu número?'))
m = (n1 // 1000) % 10
c = (n1 // 100) % 10
d = (n1 // 10) % 10
u = n1 % 10

print('Analisando o número...')
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))