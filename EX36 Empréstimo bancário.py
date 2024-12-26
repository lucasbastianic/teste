#Calculando se é possível realizar um empréstimo bancário

valor = float(input('Qual o valor da casa?'))
salario = float(input('Qual seu salário?'))
tempo = int(input('Em quantos anos você pretende pagar a casa?'))

tempo_mes = tempo * 12
prest = valor / tempo_mes
maxpag = salario * 30 / 100

if maxpag <= prest:
    print('Parabéns, seu financiamento foi aprovado')

print('Seu financiamento não foi aprovado')

