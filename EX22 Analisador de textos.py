#Transformando texto
 
nome = str(input('Qual seu nome?'))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(" ", ""))))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {}'.format(separa[0], 
len(separa[0])))

#Ou

nome = str(input('Qual seu nome?'))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {}'.format(separa[0], 
len(separa[0])))