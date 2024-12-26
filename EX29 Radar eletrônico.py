#Calculo de multa

velocidade = int(input('Qual a velocidade do seu carro?'))
if velocidade <= 80:
    print('Pode seguir viagem')
else:
    print('Reduza a velocidade, você foi multado, sua multa custará {},00 R$' .format((velocidade - 80)*7))