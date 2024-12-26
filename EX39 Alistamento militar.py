#Analisando a idade de uma pessoa

idade = int(input('Qual sua idade?   '))

if idade < 18:
    print('Ainda restam {} anos pra você se alistar!'.format(18-idade))
elif idade == 18:
    print('Você já pode se alistar')
else:
    print('Você está {} anos atrasados para se alistar.'.format(idade - 18))