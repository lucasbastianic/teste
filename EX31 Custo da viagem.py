#Calculando o custo da viagem

km = int(input('Qual o KM da viagem?'))
if km <= 200:
    print('O custo da viagem será {} R$'.format(km * 0.5))
else:
    print('O custo da viagem será {} R$'. format(km * 0.45))