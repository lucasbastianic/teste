#Calculando o reajuste salárial

salario = float(int('Digite seu salario'))
if salario <= 1250:
    print('Seu novo salário será {}R$'.format(salario + (salario * 15 / 100)))
else:
    print('Seu novo salário será {}R$'.format(salario + (salario * 10 / 100)))