#Calculando IMC

peso = float(input('Qual seu peso?   '))
altura = float(input('Qual sua altura?   '))

imc = peso / altura ** 2

if imc < 18.5:
    print('Abaixo do peso, seu IMC é {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso ideal, seu IMC é {:.2f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Sobrepeso, seu IMC é {:.2f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Obesidade, seu IMC é {:.2f}'.format(imc))     
else:
    print('Obesidade mórbida') 