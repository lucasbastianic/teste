#Analisando a possível formação de um triângulo

a = float(input('Qual o tamanho do primeiro lado?'))
b = float(input('Qual o tamanho do segundo lado?'))
c = float(input('Qual o tamanho do terceiro lado?'))


if a + b > c and a + c > b and b + c > a:
    print('Você consegue formar um triângulo')
    if a == b and a == c:
        print('Seu triângulo é equilátero')
    elif a != b and a != c and b != c :
        print('Seu triângulo é escaleno')
    else:
        print('Seu triãngulo é isóceles')
else:
    print('Você não consegue formar um triângulo')
