#Reajuste de 15% no salário

salario = float(input('Digite seu salário'))
print('Seu novo salário com um aumento de 15% será {}'.format(salario + (salario * 0.15)))

#Ou

salario = float(input('Digite seu salário'))
print('Seu novo salário com um aumento de 15% será {}'.format(salario + (salario * 15 /100)))

#Ou 

salario = float(input('Digite seu salário'))
aumento = salario + (salario * 0.15)
print('Seu novo salário com um aumento de 15% será {}'.format(aumento))

#Ou 

salario = float(input('Digite seu salário'))
aumento = salario - (salario * 15 / 100)
print('Seu novo salário com um aumento de 15% será {}'.format(aumento))