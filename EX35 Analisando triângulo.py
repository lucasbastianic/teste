#Analisando a possível formação de um triângulo

a = float(input('Qual o tamanho do primeiro lado?'))
b = float(input('Qual o tamanho do segundo lado?'))
c = float(input('Qual o tamanho do terceiro lado?'))

if a + b > c and a + c > b and b + c > a:
    print('Você consegue formar um triângulo')
else:
    print('Você não consegue formar um triângulo')