#Verificando se um aluno foi aprovado

n1 = float(input('Qual sua primeira nota?   '))
n2 = float(input('Qual sua segunda nota?   '))

media = (n1+n2) / 2

if media < 5:
    print('Você foi reprovado!')
elif media >= 5 and media <= 6.9:
    print('Você ficou de recuperação')
else:
    print('Você foi aprovado!')