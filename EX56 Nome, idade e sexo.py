#Mostrando dados da diversidade

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range (0,4):
    nome = str(input('Qual seu nome?   '))
    idade = int(input('Qual sua idade?   '))
    sexo = str(input('Qual o sexo?   '))
    somaidade += idade
    if p == 1 and sexo == 'masculino':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'masculino' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'mulher' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade /4 
print('A média de todas as idades é {}'.format(mediaidade))
print('O homem mais velho tem {} anos'.format(maioridadehomem))
print('Existem {} garotas com menos de 20 anos'.format(totmulher20))
print('O nome do mais vélho é {}'. format(nomevelho))