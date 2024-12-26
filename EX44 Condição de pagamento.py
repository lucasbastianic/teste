#Calculando o valor de acordo com a condição de pagamento

valor = int(input('Qual o valor do produto?   '))
pagamento = str(input('Qual será o método de pagamento? \n 1. Dinheiro/Cheque \n 2. Cartão a vista \n 3. 2x no cartão \n 4. 3x ou mais  '))

if pagamento == 'Dinheiro' or pagamento == 'Cheque':
    print('O valor do pagamento será {}R$'.format(valor - (valor * 10 /100)))
elif pagamento == 'Cartão a vista':
    print('O valor do pagamento será {}R$'.format(valor - (valor * 5 /100)))
elif pagamento == '2x no cartão':
    print('O valor do pagamento será {}R$'.format())
else:
    print('O valor do pagamento será {}R$'.format(valor + (valor * 20 /100)))
